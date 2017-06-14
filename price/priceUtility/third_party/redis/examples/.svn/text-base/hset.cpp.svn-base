#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <stdint.h>
#include <cstring>
#include <vector>
#include <cmath>

using namespace boost;  
using namespace std;  
const uint16_t MOBILE_MASK  = 0X80;

#pragma pack(push)
#pragma pack(1)
// ota粒度索引版
struct MiniPriceUnit {
    MiniPriceUnit() :
            id(0), price(0), total_price(0) {
    }
    uint16_t id :8;    
    uint32_t price :24;
    uint32_t total_price :24; 
    uint32_t ota_id() const {
        return id & (~MOBILE_MASK);
    }
    bool mobile_only() const {
        return id & MOBILE_MASK;
    }
};

// ota粒度内存版
struct PriceUnit {
    PriceUnit() :
            id(0), price(0), elong_price(0), total_price(0), elong_total_price(0) {
    }
    PriceUnit(uint8_t id, uint32_t price, uint32_t total_price) :
            id(id), 
            price(price), 
            elong_price(price), 
            total_price(total_price),
            elong_total_price(total_price),
            mobile_only(false) {
    }
    uint16_t id;
    uint32_t price;       
    uint32_t elong_price;
    uint32_t total_price;
    uint32_t elong_total_price; 
    bool mobile_only;
    // 带手机专项价的id， 最高位为1
    uint32_t mini_id() const {
        return mobile_only ? id |  MOBILE_MASK: id;
    }
    uint32_t high_price() const {
        return round(price/10.0);
    }
    uint32_t high_elong_price() const {
            return round(elong_price/10.0);
    }
    uint32_t high_total_price() const {
        return round(total_price/10.0);
    }
    uint32_t high_elong_total_price() const {
            return round(elong_total_price/10.0);
    }
};

void SerializeToString(std::vector<PriceUnit>& pu, std::string& output) {
    
    size_t len = pu.size() * sizeof(MiniPriceUnit);
    char cc[len];
    for (uint8_t i = 0; i < pu.size(); ++i) {
        MiniPriceUnit mpu;
        mpu.id = pu[i].mini_id();    // 8 bit
        mpu.price = pu[i].price;     // 24 bit
        mpu.total_price = pu[i].total_price; // 24 bit
        memcpy(cc + sizeof(MiniPriceUnit) * i, (void*) (&mpu),
                sizeof(MiniPriceUnit));
    }
    output.assign(cc, len);

}

int main(int argc,char *argv[])  
{ 
    const char *rdsconnection = "192.168.14.170:7000,192.168.14.170:7001,192.168.14.170:7002,192.168.14.170:7003,192.168.14.170:7004,192.168.14.170:7005";
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
 
    std::vector<PriceUnit> pu;
    PriceUnit pu1(130, 140, 156);
    pu.push_back(pu1);
    PriceUnit pu2(2, 0, 0);
    pu.push_back(pu2);
    std::string data("");
    SerializeToString(pu, data);
    cout << "data size: " << data.size() << endl;
    // 打印存入的字节
    for (int i = 0; i < data.size(); i++){
            printf("%x ", data[i] & 0xFF);                                                                         
    } 

    const char **p = new const char *[4];
    p[0] = "hset";
    p[1] = hash_name.c_str();
    p[2] = key.c_str();
    p[3] = data.c_str();
    size_t *len = new size_t[4];
    len[0] = 4;
    len[1] = hash_name.size();
    len[2] = key.size();
    len[3] = data.size(); 
    /*
    const char **p; 
    p = (const char **)malloc(4 * sizeof(const char *));
    *p = "hset";
    *(p+1) = hash_name.c_str();
    *(p+2) = key.c_str();
    *(p+3) = data.c_str();
    size_t *len;
    len = (size_t *)malloc(4 * sizeof(size_t));
    *len = 4;
    *(len+1) = hash_name.size();
    *(len+2) = key.size();
    *(len+3) = data.size();
    */

    rds_reply = (redisReply *)redisClusterCommandArgv(rds_ctx, 4, p, len);
    // free(p);
    // free(len);
    delete [] p;
    delete len;
    if (rds_reply == NULL){
        cout << "redis err for rds_reply is NULL" << endl;
        exit(1);
    }

    if (rds_reply->type != REDIS_REPLY_ERROR) {
        cout << "ok" << endl;
    }
    return 0;  
}  
