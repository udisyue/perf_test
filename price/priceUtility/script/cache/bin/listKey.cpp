#include <iostream>  
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <stdint.h>
using namespace std;

uint32_t MurmurHash32A(const void* key, int len) {
     static const uint32_t seed = 19820125;
     const uint32_t m = 0x5bd1e995;
     const int r = 24;

     uint32_t h = seed ^ (len * m);

     const uint32_t* data = (const uint32_t *) key;

     while (len >= 4) {
         uint32_t k = *(uint32_t *) data;

         k *= m;
         k ^= k >> r;
         k *= m;

         h *= m;
         h ^= k;

         data += 1;
         len -= 4;
     }
     // Handle the last few bytes of the input array
     const uint8_t* data2 = (const uint8_t*) data;

     switch (len) {
     case 3:
         h ^= static_cast<uint32_t>(data2[2]) << 16;
     case 2:
         h ^= static_cast<uint32_t>(data2[1]) << 8;
     case 1:
         h ^= static_cast<uint32_t>(data2[0]);
         h *= m;
     };

     // Do a few final mixes of the hash to ensure the last few
     // bytes are well-incorporated.

     h ^= h >> 13;
     h *= m;
     h ^= h >> 15;

     return h;
}


int main(int argc,char *argv[])  
{ 
    std::string key_str("");
    uint32_t sign_int = 0;

    // ver_2_ci_20160620_co_20160621_bc_0_cl_0_of_0_adult_num_2_child_num_0#_324748
    if ( argc < 9 ){
        // cout << 1 << endl;
        return 1;
    } else {
        key_str = "ver_" + std::string(argv[1])
                + "_ci_" + std::string(argv[2])
                + "_co_" + std::string(argv[3])
                + "_bc_" + std::string(argv[4])
                + "_cl_" + std::string(argv[5])
                + "_of_" + std::string(argv[6])
                + "_adult_num_" + std::string(argv[7])
                + "_child_num_" + std::string(argv[8])
                + "_" + std::string(argv[9]);
        // cout << "key => " << key_str << endl;
    }

    if (!key_str.empty()){
        sign_int = MurmurHash32A(key_str.data(), key_str.size());
    }
    cout << sign_int;
    return 0;  
}  