#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>

using namespace boost;  
using namespace std;  

int main(int argc,char *argv[])  
{ 
    const char *rdsconnection = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235";
    // const char *rdsconnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233";
    // const char *rdsconnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection, HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        return -1;
    }
    redisReply *rds_reply = NULL;


    std::string key("");
    if ( argc != 2 ){
        cout << "input param : key" << endl;
        exit(1);
    } else {
        key = argv[1];
        cout << "key => " << key << endl;
    }
 
    rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "ttl %s", key.c_str());

    if (rds_reply == NULL){
        cout << "redis err for rds_reply is NULL" << endl;
        exit(1);
    }
  
    cout << "rds_reply->type : " << rds_reply->type << endl;
    cout << "rds_reply->integer: "  <<  rds_reply->integer << endl;

    if (rds_reply->type == REDIS_REPLY_INTEGER
                && rds_reply->integer > 0) {
        long long time_left = rds_reply->integer;
        cout << "time left... "  << time_left << endl;
    } else {
        cout << "no time left." << endl;
    }
    return 0;  
}  
