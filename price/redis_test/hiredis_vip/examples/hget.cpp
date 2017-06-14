#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include <vector>

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


    std::string hash_name(""), key("");
    if ( argc != 3 ){
        cout << "input param : hash_name ,key" << endl;
        exit(1);
    } else {
        hash_name = argv[1];
        key = argv[2];
        cout << "hashTable => " << hash_name << endl;
        cout << "key => " << key << endl;
    }
 
    const char **p = new const char *[3];
    p[0] = "hget";
    p[1] = hash_name.c_str();
    p[2] = key.c_str();
    size_t *len = new size_t[3];
    len[0] = 4;
    len[1] = hash_name.size();
    len[2] = key.size();

    rds_reply = (redisReply *)redisClusterCommandArgv(rds_ctx, 3, p, len);

    delete [] p;
    delete len;

    if (rds_reply == NULL){
        cout << "redis err for rds_reply is NULL" << endl;
        exit(1);
    }

    if (rds_reply->type == REDIS_REPLY_STRING
                && rds_reply->len > 0) {
        // TODO 取8个字节
        std::vector<char> bytes;
        for (int i = 0; i < rds_reply->len; i++){
            // printf("%x ", rds_reply->str[i] & 0xFF);
            bytes.push_back(rds_reply->str[i] & 0xFF);
        } 
        // std::string val(rds_reply->str, rds_reply->len);
        ParseFromString(bytes);
    } else {
        cout << hash_name << "not exists" << endl;
    }
    return 0;  
}  
