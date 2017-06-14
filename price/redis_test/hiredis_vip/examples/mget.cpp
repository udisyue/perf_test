#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include <vector>
#include <time.h>
#include <stdlib.h>

using namespace boost;  
using namespace std;  

// 详情页查询产品信息
bool detail_find(const std::string& key, std::vector<char> &value, const char *rdsConnection) {


    if (!key.empty()){
        // redis_cluster_context
        const char *rdsConnection = "10.39.135.17:5234,10.39.135.17:5235,10.39.135.17:5236,10.39.135.22:5234,10.39.135.22:5235,10.39.135.22:5236,10.39.136.17:5234,10.39.136.17:5235,10.39.136.17:5236,10.39.136.23:5234,10.39.136.23:5235,10.39.136.23:5236"; 
        redisClusterContext *rds_ctx = redisClusterConnect(rdsConnection, HIRCLUSTER_FLAG_NULL);
        // redisClusterContext *rds_ctx = redisClusterConnect(rdsConnection, HIRCLUSTER_FLAG_ROUTE_USE_SLOTS | HIRCLUSTER_FLAG_ADD_SLAVE);
        // return true;
        if(rds_ctx == NULL || rds_ctx->err){
            cout << "redis init err" << endl;
            return false;
        }
        // redis_cluster_reply
        redisReply *rds_reply = NULL;
        rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "MGET %s %s %s %s %s %s", "d_1533912878423629576", "d_4812715876285198652", "d_4926811811352457775", "d_4981566463920288303", "d_1564568899047961098", "d_4812715876285198652");
        cout << rds_reply << endl;
        // result
        if (rds_reply == NULL){
            cout << "redis err for rds_reply is NULL" << endl;
            redisClusterFree(rds_ctx);
            return false;
        }
        if (rds_reply->type == REDIS_REPLY_STRING
            && rds_reply->len > 0) {
            for (int k = 0; k < rds_reply->len; k++) {
                value.push_back(rds_reply->str[k] & 0xFF);
            }
        }
        freeReplyObject(rds_reply);
        redisClusterFree(rds_ctx);
    }
    // cout << "key=" << key << " value_byte=" << value.size() << endl;
   
    return value.size();
}

long getCurrentTime() {
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}


int main(int argc,char *argv[])  
{ 
    // srand((unsigned)time(NULL));
    // int index = rand()%12;
    long begin_t = getCurrentTime();
    std::vector<char> value;
    detail_find("d_1533912878423629576", value, "10.39.135.17:5235");
    // value.clear();
    // detail_find("d_4812715876285198652", value, "10.39.136.23:5236");
    // value.clear();
    // detail_find("d_4926811811352457775", value, "10.39.136.17:5235");
    // value.clear();
    // detail_find("d_4981566463920288303", value, "10.39.136.23:5236");
    // value.clear();
    // detail_find("d_1564568899047961098", value, "10.39.135.17:5236");
    // value.clear();
    // detail_find("d_4812715876285198652", value, "10.39.136.17:5236");

    long end_t = getCurrentTime();
    cout << "time=" << (end_t - begin_t) << endl;
    return 0;  
}  
