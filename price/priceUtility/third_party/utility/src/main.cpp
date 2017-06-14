// #ifndef MAIN_TEST_DEFINE_H
// #define MAIN_TEST_DEFINE_H
#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <string>

#include "cm_utility/signature.h"
#include "cm_utility/string_utils.h"
#include "cm_utility/string_splitter.h"
#include "cm_utility/timer.h"

using namespace std;

int main(int argc, char *argv[])
{
    // rid_0_oid_13_hid_324748_mobile_0_ver_2_ci_20160626_co_20160627_bc_0_cl_0_of_0_adult_num_2_child_num_0#
    std::string str("");
    if ( argc < 11 ) {
        // cout << 1 << endl;
        return 1;
    }

    // 10 20958 2 20161003 20161004 0 0 0 2 0#
    str = "rid_0_oid_" + std::string(argv[1])
        + "_hid_" + std::string(argv[2])
        + "_mobile_" + std::string(argv[3])
        + "_ver_" + std::string(argv[4])
        + "_ci_" + std::string(argv[5])
        + "_co_" + std::string(argv[6])
        + "_bc_" + std::string(argv[7])
        + "_cl_" + std::string(argv[8])
        + "_of_" + std::string(argv[9])
        + "_adult_num_" + std::string(argv[10])
        + "_child_num_" + std::string(argv[11]);

    // cout << "str => " << str << endl;
    cm_utility::Signature sig = 
        cm_utility::Signature::create_sign(str.c_str(), str.length());

    uint64_t key = cm_utility::sign_to_uint64(sig.s1(), sig.s2());
    long long int sign_int = 0;
    memcpy(&sign_int, &key, sizeof(key));

    cout << sign_int;
    
    return 0;
}
