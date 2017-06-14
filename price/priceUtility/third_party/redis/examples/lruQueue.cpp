#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <string>
#include "json/json.h"

using namespace boost;  
using namespace std;  

int main(int argc,char *argv[])  
{ 
    std::string rdsconnection("");
    if ( argc < 2 ){
        cout << "error";
        exit(1);
    }
    rdsconnection = argv[1];
    std::vector<std::string> ota_vec;
    ota_vec.push_back("booking");
    ota_vec.push_back("ean");
    ota_vec.push_back("agoda");
    ota_vec.push_back("elong");
    ota_vec.push_back("gta");
    ota_vec.push_back("vetu");
    ota_vec.push_back("ctrip");
    ota_vec.push_back("dida");
    ota_vec.push_back("hotelbeds");
    ota_vec.push_back("dotw");
    ota_vec.push_back("eanpackage");
    ota_vec.push_back("fgt");
    ota_vec.push_back("agodapackage");
    ota_vec.push_back("roomorama");
    ota_vec.push_back("hotelspro");
    ota_vec.push_back("zyx");
    ota_vec.push_back("tourico");
    ota_vec.push_back("miki");
    ota_vec.push_back("travellanda");
    ota_vec.push_back("relux");
    ota_vec.push_back("methabook");
    ota_vec.push_back("haoqiao");
    // const char *rdsconnection = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235";
    // const char *rdsconnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233";
    // const char *rdsconnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection.c_str(), HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        cout << "error";
        return -1;
    }

    Json::Value ota_queue;
    for (size_t i = 0; i < ota_vec.size(); ++i) {
        Json::Value a_ota_queue = Json::Value();
        std::string key = ota_vec[i];
        int32_t value = 0;

        redisReply *rds_reply = NULL;
        rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "LLEN %s", key.c_str());
        if (rds_reply == NULL){
            cout << "error";
            break;
        }
        if (rds_reply->type == REDIS_REPLY_INTEGER) {
            value = rds_reply->integer;
            freeReplyObject(rds_reply);
        }
        a_ota_queue["name"] = Json::Value(key);
        a_ota_queue["len"] = Json::Value(value);
        ota_queue.append(a_ota_queue);
    }
    redisClusterFree(rds_ctx);
    std::string result("");
    Json::FastWriter fast_writer;
    result = fast_writer.write(ota_queue);
    result = result.substr(0, result.length()-1);
    cout << result;
    return 0;  
}
