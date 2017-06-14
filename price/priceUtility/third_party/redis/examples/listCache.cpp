#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include "json/json.h"

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

std::string ParseFromString(std::vector<char> &bytes) {
    std::string result("unexists");
    // std::vector<char> 赋值给 char[]
    int bytelen = bytes.size();
    char data[bytelen];
    for(int k = 0; k < bytelen; k ++){
        data[k] = bytes[k];
    }
    size_t ota_num = bytelen * sizeof(char) / sizeof(MiniPriceUnit);
    if (ota_num > 0) {
        Json::Value ota_list;
        for (size_t i = 0; i < ota_num; ++i) {
            MiniPriceUnit mpu;
            memcpy((void*) (&mpu), (void*) (&data[i * sizeof(MiniPriceUnit)]),
                    sizeof(MiniPriceUnit));
            Json::Value a_ota = Json::Value();
            a_ota["ota_id"] = Json::Value(mpu.ota_id());
            a_ota["cash_pay"] = Json::Value(mpu.cash_pay());
            a_ota["mobile_only"] = Json::Value(mpu.mobile_only());
            a_ota["room_pr"] = Json::Value(mpu.price);
            a_ota["pr"] = Json::Value(mpu.total_price);
            a_ota["ts"] = Json::Value(mpu.timestamp);
            ota_list.append(a_ota);
        }
        Json::FastWriter fast_writer;
        result = fast_writer.write(ota_list);
        result = result.substr(0, result.length()-1);
    }
    return result;
}

#pragma pack(pop)

int main(int argc,char *argv[])  
{ 
    std::string rdsconnection(""), hash_name(""), key("");
    if ( argc < 4 ){
        cout << "error";
        exit(1);
    } else {
        rdsconnection = argv[1];
        hash_name = argv[2];
        key = argv[3];
    }
    // const char *rdsconnection = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235";
    // const char *rdsconnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233";
    // const char *rdsconnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection.c_str(), HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        return -1;
    }
    redisReply *rds_reply = NULL;
 
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
        cout << "error";
        exit(1);
    }

    if (rds_reply->type == REDIS_REPLY_STRING
                && rds_reply->len > 0) {
        std::vector<char> bytes;
        for (int i = 0; i < rds_reply->len; i++){
            bytes.push_back(rds_reply->str[i] & 0xFF);
        } 
        cout << ParseFromString(bytes);
    } else {
        cout << "unexists";
    }
    freeReplyObject(rds_reply);
    redisClusterFree(rds_ctx);
    
    return 0;  
}  
