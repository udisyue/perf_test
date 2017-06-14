#include<iostream>
#include<hircluster.h>

using namespace std;
/*
#define REDIS_REPLY_STRING 1 //字符串
#define REDIS_REPLY_ARRAY 2    //数组，多个rds_reply，通过element数组以及elements数组大小访问
#define REDIS_REPLY_INTEGER 3    //整型, integer字段
#define REDIS_REPLY_NIL 4    //空，没有数据
#define REDIS_REPLY_STATUS 5    //状态，str字符串以及len
#define REDIS_REPLY_ERROR 6    //错误，同STATUS

typedef struct redisReply {
　　int type;          // 指明返回的类型, REDIS_REPLY_*
　　long long integer; // The integer when type is REDIS_REPLY_INTEGER
　　int len;           // Length of string 
　　char *str;         // Used for both REDIS_REPLY_ERROR and REDIS_REPLY_STRING
　　size_t elements;   // number of elements, for REDIS_REPLY_ARRAY
　　struct redisReply **element; // elements vector for REDIS_REPLY_ARRAY
} redisReply;
*/

int main()
{
    // const char *rdsconnection = "172.21.17.111:5233,172.21.20.128:5233,172.21.21.109:5233,172.21.22.112:5233,10.35.72.153:5233,10.35.41.211:5233,10.35.42.196:5233";
    const char *rdsconnection = "192.168.14.170:7000,192.168.14.170:7001,192.168.14.170:7002,192.168.14.170:7003,192.168.14.170:7004,192.168.14.170:7005";
    redisClusterContext *rds_ctx = redisClusterConnect(rdsconnection, HIRCLUSTER_FLAG_NULL);
    if(rds_ctx == NULL || rds_ctx->err)
    {
        return -1;
    }
    redisReply *rds_reply = NULL;

    // hmset
    rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "hmset %s %s %s %s %s", "cluster_hash_test", "k1", "v1", "k2", "v2");
    if(rds_reply == NULL)
    {
        cout << "rds_reply is null: " << rds_ctx->errstr << endl;
        redisClusterFree(rds_ctx);
        return -1;
    }
    cout << "hmset [type : str] = [" << rds_reply->type << " : " << rds_reply->str << "]" << endl;
    freeReplyObject(rds_reply);

    // hget
    rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "hget %s %s", "cluster_hash_test", "k1");
    if(rds_reply == NULL)
    {
        cout << "rds_reply is null: " << rds_ctx->errstr << endl;
        redisClusterFree(rds_ctx);
        return -1;
    }
    cout << "hmset [type : str] = [" << rds_reply->type << " : " << rds_reply->str << "]" << endl;
    freeReplyObject(rds_reply);

    // hmget
    rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "hmget %s %s %s %s %s %s", "cluster_hash_test", "k0","k1", "k2","k6","k8");
    if(rds_reply == NULL)
    {
        cout << "rds_reply is null: " << rds_ctx->errstr << endl;
        redisClusterFree(rds_ctx);
        return -1;
    }
    cout << "hmget [type] = " << rds_reply->type << endl;
    if (rds_reply->type == REDIS_REPLY_ARRAY) {
        for(int i = 0; i < rds_reply->elements; i++){
            if (REDIS_REPLY_NIL != rds_reply->element[i]->type) {
                cout << "hmget str : " << rds_reply->element[i]->str << endl;
            } else {
                cout << "hmget str : " << "NONEXIST_RDS_KEY" << endl;
            }
        }
    }
    freeReplyObject(rds_reply);

    redisClusterFree(rds_ctx);
    return 0;
}
