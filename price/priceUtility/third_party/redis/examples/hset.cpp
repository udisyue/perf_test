#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>

using namespace boost;  
using namespace std;  

const uint16_t MOBILE_MASK  = 0X80;
const uint16_t CASHPAY_MASK = 0X40;
const uint16_t OTAID_MASK = 0X3F;

#pragma pack(push)
#pragma pack(1)
// ota粒度索引版
struct MiniPriceUnit {

    MiniPriceUnit() :
            id(0), price(0), total_price(0), timestamp(0) {
    }
    uint16_t id :8;           // 供应商ID, 0标识该供应商失效(或不存在)
    uint32_t price :24;       // 原始房价
    uint32_t total_price :24; // 原始税后价
    uint32_t timestamp :32;
    uint32_t ota_id() const {
        return id & OTAID_MASK;
    }
    bool mobile_only() const {
        return id & MOBILE_MASK;
    }
    bool cash_pay() const {
       return id & CASHPAY_MASK;
   }
};

void ParseFromString(std::vector<char> &bytes) {
    // std::vector<char> 赋值给 char[]
    int bytelen = bytes.size();
    char data[bytelen];
    for(int k = 0; k < bytelen; k ++){
        data[k] = bytes[k];
    }
    size_t ota_num = bytelen * sizeof(char) / sizeof(MiniPriceUnit);
    for (size_t i = 0; i < ota_num; ++i) {
        MiniPriceUnit mpu;
        memcpy((void*) (&mpu), (void*) (&data[i * sizeof(MiniPriceUnit)]),
                sizeof(MiniPriceUnit));
        cout << "result => [ id=" << mpu.ota_id() << ", ";
        cout << "mobile=" << mpu.mobile_only() << ", ";
        cout << "cashpay=" << mpu.cash_pay() << ", ";
        cout << "t_pr=" << mpu.total_price << ", ";
        cout << "pr=" << mpu.price << " ,";
        cout << "ts=" << mpu.timestamp << " ]" << endl;
    }
}

// ota粒度内存版
struct PriceUnit {

    PriceUnit() :
            id(0), original_price(0, 0), price(0, 0), timestamp(0) {
    }
    PriceUnit(uint8_t id, std::pair<uint32_t, uint32_t> price,
              uint32_t timestamp, bool mobile_only, bool cash_pay) :
            id(id), original_price(price), price(price),
            timestamp(timestamp), mobile_only(mobile_only), cash_pay(cash_pay) {
    }
    // 供应商ID, 0标识该供应商失效(或不存在)
    uint16_t id;
    // 原始含税价、房价
    std::pair<uint32_t, uint32_t> original_price;
    // elong含税价、房价
    std::pair<uint32_t, uint32_t> price;
    // 更新时间戳
    uint32_t timestamp;
    // 标识手机专享
    bool mobile_only;
    // 现付类型
    bool cash_pay;

    // 带手机专享和现付标识的ota_id
    uint32_t mini_id() const {
        if (mobile_only && cash_pay) {
            return (id | MOBILE_MASK | CASHPAY_MASK);
        } else if (mobile_only && !cash_pay) {
            return (id | MOBILE_MASK);
        } else if (!mobile_only && cash_pay) {
            return (id | CASHPAY_MASK);
        }
        return id;
    }

    std::pair<uint32_t, uint32_t> high_price() const {
        return std::pair<uint32_t, uint32_t>(
            round(price.first/100.0), round(price.second/100.0));
    }
    std::pair<uint32_t, uint32_t> high_origin_price() const {
            return std::pair<uint32_t, uint32_t>(
                round(original_price.first/100.0), round(original_price.second/100.0));
    }
};

void SerializeToString(std::vector<PriceUnit> &pu, std::string& output) {
    size_t len = pu.size() * sizeof(MiniPriceUnit);
    char cc[len];
    for (uint8_t i = 0; i < pu.size(); ++i) {
        MiniPriceUnit mpu;
        mpu.id = pu[i].mini_id();   // 8 bit
        mpu.price = pu[i].price.second;    // 24 bit
        mpu.total_price = pu[i].price.first; // 24 bit
        mpu.timestamp = pu[i].timestamp;
        memcpy(cc + sizeof(MiniPriceUnit) * i, (void*) (&mpu),
                sizeof(MiniPriceUnit));
    }
    output.assign(cc, len);
}

#pragma pack(pop)

int main(int argc,char *argv[])  
{ 
    // const char *rdsconnection = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235";
    // const char *rdsconnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233";
    const char *rdsconnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection, HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        return -1;
    }
    redisReply *rds_reply = NULL;


    std::string hash_name(""), key(""), value("");
    if ( argc != 3 ){
        cout << "input param : hash_name ,key" << endl;
        exit(1);
    } else {
        hash_name = argv[1];
        key = argv[2];
        cout << "hashTable => " << hash_name << endl;
        cout << "key => " << key << endl;
    }
    std::vector<PriceUnit> pus;
    PriceUnit pu(2, 
        std::pair<uint32_t, uint32_t>(12000, 22000),
        1476081285, false, false);
    pus.push_back(pu);
    SerializeToString(pus, value);
 
    const char **p = new const char *[4];
    p[0] = "hset";
    p[1] = hash_name.c_str();
    p[2] = key.c_str();
    p[3] = value.c_str();
    size_t *len = new size_t[4];
    len[0] = 4;
    len[1] = hash_name.size();
    len[2] = key.size();
    len[3] = value.size();

    rds_reply = (redisReply *)redisClusterCommandArgv(rds_ctx, 4, p, len);

    delete [] p;
    delete len;

    if (rds_reply == NULL){
        cout << "redis err for rds_reply is NULL" << endl;
        exit(1);
    }

    cout << "ok." << endl; 
    return 0;  
}  
