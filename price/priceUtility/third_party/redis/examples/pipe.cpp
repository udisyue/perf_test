#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>

using namespace boost;  
using namespace std;  

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
    // redisClusterAppendCommand(rds_ctx, "set a bb");
    // redisClusterAppendCommand(rds_ctx, "get a");
    redisClusterAppendCommand(rds_ctx, "ZRANGE ean 0 0 WITHSCORES");
    redisClusterAppendCommand(rds_ctx, "ZREMRANGEBYRANK ean 0 0");
    while(redisClusterGetReply(rds_ctx,(void**)&rds_reply) == REDIS_OK) {
        cout << "rds_reply->type: " << rds_reply->type << endl;
        cout << "rds_reply->str: " << rds_reply->str << endl;
        cout << "rds_reply->len: " << rds_reply->len << endl;
        cout << "rds_reply->integer: " << rds_reply->integer << endl;
        cout << "rds_reply->elements: " << rds_reply->elements << endl;
        cout << "------------" << endl;
        if (rds_reply->type == REDIS_REPLY_STATUS) {
            continue;
        }
        freeReplyObject(rds_reply);
    }
    redisCLusterReset(rds_ctx);

    // rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "set a b");
    // rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "get a");

    if (rds_reply == NULL){
        cout << "redis err for rds_reply is NULL" << endl;
        redisClusterFree(rds_ctx);
        exit(1);
    }
    if (rds_reply->type == REDIS_REPLY_STRING
        && rds_reply->len > 0
        && rds_reply->str != NULL) {
        string value(rds_reply->str, rds_reply->len);
        cout << "value: " << value << endl;
    }

    freeReplyObject(rds_reply);
    redisClusterFree(rds_ctx);
    return 0;  
}  
