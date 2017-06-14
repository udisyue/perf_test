#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <string>
#include "price_types.pb.h"
#include "pbjson.hpp"

using namespace boost;  
using namespace std;  

int main(int argc,char *argv[])  
{ 
    std::string rdsconnection(""), key("");
    if ( argc < 3 ){
        cout << "error";
        exit(1);
    }
    rdsconnection = argv[1];
    key = argv[2];
    // const char *rdsconnection = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235";
    // const char *rdsconnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233";
    // const char *rdsconnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection.c_str(), HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        cout << "error";
        return -1;
    }
    redisReply *rds_reply = NULL;

    const char **p = new const char *[2];
    p[0] = "get";
    p[1] = key.c_str();
    size_t *len = new size_t[2];
    len[0] = 3;
    len[1] = key.size();

    rds_reply = (redisReply *)redisClusterCommandArgv(rds_ctx, 2, p, len);

    delete [] p;
    delete len;

    if (rds_reply == NULL){
        cout << "error";
        exit(1);
    }

    if (rds_reply->type == REDIS_REPLY_STRING
                && rds_reply->len > 0) {
        std::string val(rds_reply->str, rds_reply->len);
        price::DetailOta a_ota;
        // a_ota.ParseFromArray(val.c_str(), val.size());
        a_ota.ParseFromString(val);
        // cout << "======================================" << endl;
        // cout << "ParseFromString : hotel_id = " << a_ota.base_hotel_id()<< endl;
        string a_ota_json;
        pbjson::pb2json(&a_ota, a_ota_json);
        // cout << "pb2json : str = " << a_ota_json.c_str() << endl;
        // cout << "pb2json : size = " << a_ota_json.size() << endl;
        cout << a_ota_json.c_str();
    }
    return 0;  
}
