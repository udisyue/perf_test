#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <hiredis.h>

using namespace std;

int main(int argc, char **argv) {
    unsigned int j;
    redisContext *c;
    redisReply *reply;
    const char *hostname = "10.39.136.23";
    int port = 5234;

    struct timeval timeout = { 1, 500000 }; // 1.5 seconds
    c = redisConnectWithTimeout(hostname, port, timeout);
    if (c == NULL || c->err) {
        if (c) {
            cout << "Connection error: " << c->errstr << endl;
            redisFree(c);
        } else {
            cout << "Connection error: can't allocate redis context" << endl;
        }
        exit(1);
    }

    /* Try a GET and two INCR */
    reply = (redisReply* )redisCommand(c,"GET d_4878444870360874461");
    // cout << reply->str << endl;
    freeReplyObject(reply);

    /* Disconnects and frees the context */
    redisFree(c);

    return 0;
}
