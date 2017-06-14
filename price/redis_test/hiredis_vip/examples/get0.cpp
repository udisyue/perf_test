#include <iostream>  
#include <boost/date_time.hpp>  
#include "hircluster.h"
#include <malloc.h>
#include <vector>
#include <time.h>

using namespace boost;  
using namespace std;  

// 详情页查询产品信息
bool detail_find(const std::string& key, std::vector<char> &value) {


    if (!key.empty()){
        // redis_cluster_context
        // const char *_rdsConnection = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233"; 
        const char *_rdsConnection = "10.39.135.17:5234,10.39.135.17:5235,10.39.135.17:5236,10.39.135.22:5234,10.39.135.22:5235,10.39.135.22:5236,10.39.136.17:5234,10.39.136.17:5235,10.39.136.17:5236,10.39.136.23:5234,10.39.136.23:5235,10.39.136.23:5236"; 
        // const char *_rdsConnection = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234";
        // const char *_rdsConnection = "10.39.135.17:5234"; 
        // redisClusterContext *rds_ctx = redisClusterConnect(_rdsConnection, HIRCLUSTER_FLAG_NULL);
        // redisClusterContext *rds_ctx = redisClusterConnect(_rdsConnection, HIRCLUSTER_FLAG_ROUTE_USE_SLOTS);
        redisClusterContext *rds_ctx = redisClusterConnect(_rdsConnection, HIRCLUSTER_FLAG_ADD_OPENSLOT);
        if(rds_ctx == NULL || rds_ctx->err){
            cout << "redis init err" << endl;
            return false;
        }
        // redis_cluster_reply
        redisReply *rds_reply = NULL;
        rds_reply = (redisReply *)redisClusterCommand(rds_ctx, "GET %s", key.c_str());

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
    vector<string> keys;
    keys.push_back("d_4764348935293615338");  // located at 192.168.110.128:5233 
    keys.push_back("d_4878444870360874461");  // located at 192.168.110.111:5233
    keys.push_back("d_4840412892005121420");  // located at 10.39.136.23:5233
    keys.push_back("d_1509814246480130570");  // located at 192.168.110.111:5233
    keys.push_back("d_1564568899047961098");  // located at 10.39.136.17:5233
    keys.push_back("d_1838342161887113738");  // located at 10.39.135.17:5233
    keys.push_back("d_1947851467022774794");  // located at 10.39.136.23:5233
    // hget 20170606.3 3905019743  => located at 192.168.110.128:5233
    long begin_t = getCurrentTime();
    vector<string>::iterator it = keys.begin();
    for(; it != keys.end(); ++it) {
        // cout << *it << endl;
        std::vector<char> value;
        detail_find(*it, value);
    }
    long end_t = getCurrentTime();
    cout << "time=" << (end_t - begin_t) << endl;
    return 0;  
}  
