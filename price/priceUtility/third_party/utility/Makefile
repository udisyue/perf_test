
BASE_DIR=/home/baijie.cai/git_only/base
CXX=g++
CXXFLAGS=-Wall -g

INC_DIR=-I./src \
	-I$(BASE_DIR)/third-64/leveldb/include \
	-I$(BASE_DIR)/public/global \
	-I$(BASE_DIR)/public/nshead/output/include \
	-I$(BASE_DIR)/public/mrf/output/include \
	-I$(BASE_DIR)/public/pb-rpc/include \
	-I$(BASE_DIR)/public/pb-rpc/output/include \
	-I$(BASE_DIR)/public/utility/output/include \
	-I$(BASE_DIR)/public/smalltable/output/include \
	-I$(BASE_DIR)/public/configure/output/include \
	-I$(BASE_DIR)/public/sign/output/include \
	-I$(BASE_DIR)/public/ub/output/include \
	-I$(BASE_DIR)/public/comlogext/cronoapd \
	-I$(BASE_DIR)/public/connectpool/output \
	-I$(BASE_DIR)/public/uconv/output/include \
	-I$(BASE_DIR)/lib2-64/dict/include \
	-I$(BASE_DIR)/lib2-64/string/include \
	-I$(BASE_DIR)/lib2-64/ccode/include \
	-I$(BASE_DIR)/lib2-64/ullib/include \
	-I$(BASE_DIR)/lib2-64/bsl/include \
	-I$(BASE_DIR)/third-64/jsoncpp/include \
	-I$(BASE_DIR)/third-64/rapidjson/include \
	-I$(BASE_DIR)/third-64/boost/include \
	-I$(BASE_DIR)/third-64/gtest/include \
	-I$(BASE_DIR)/third-64/gtest/include \
	-I$(BASE_DIR)/third-64/gflags/include \
	-I$(BASE_DIR)/third-64/protobuf/include \
	-I$(BASE_DIR)/quality/autotest/bmock/output/include \
	-I$(BASE_DIR)/third-64/tcmalloc/include \
	-I$(BASE_DIR)/third-64/mongo-client/include \
	-I$(BASE_DIR)/third-64/rapidjson/include/ \

LIB_DIR=-Xlinker "-(" \
	$(BASE_DIR)/public/mrf/output/lib/libmrf.a \
	$(BASE_DIR)/public/pb-rpc/output/lib/libpb-rpc.a \
	$(BASE_DIR)/public/utility/output/lib/libcm_utility.a \
	$(BASE_DIR)/public/smalltable/output/lib/libsmalltable.a \
	$(BASE_DIR)/public/configure/output/lib/libconfig.a \
	$(BASE_DIR)/public/sign/output/lib/libuln_sign.a \
	$(BASE_DIR)/public/spreg/output/lib/libspreg.a \
	$(BASE_DIR)/public/nshead/output/libnshead.a \
	$(BASE_DIR)/public/ub/output/lib/libub.a \
	$(BASE_DIR)/public/ub/output/lib/libub.a \
	$(BASE_DIR)/public/ub/output/lib/libub_client.a \
	$(BASE_DIR)/public/ub/output/lib/libub_aserver.a \
	$(BASE_DIR)/public/ub/output/lib/libubfw.a \
	$(BASE_DIR)/public/ub/output/lib/libub_misc.a \
	$(BASE_DIR)/lib2-64/ccode/lib/libulccode.a \
	$(BASE_DIR)/lib2-64/dict/lib/libuldict.a \
	$(BASE_DIR)/lib2-64/string/lib/libstring.a \
	$(BASE_DIR)/public/ub/output/lib/libub_conf.a \
	$(BASE_DIR)/public/connectpool/output/libconnectpool.a \
	$(BASE_DIR)/lib2-64/ullib/lib/libullib.a \
	$(BASE_DIR)/lib2-64/bsl/lib/libbsl.a \
	$(BASE_DIR)/lib2-64/bsl/lib/libbsl_var.a \
	$(BASE_DIR)/public/uconv/output/libuconv.a \
	$(BASE_DIR)/lib2-64/bsl/lib/libbsl_pool.a \
	$(BASE_DIR)/lib2-64/bsl/lib/libbsl.a \
	$(BASE_DIR)/lib2-64/bsl/lib/libbsl_utils.a \
	$(BASE_DIR)/third-64/gflags/lib/libgflags.a \
	$(BASE_DIR)/quality/autotest/bmock/output/lib/libgmock.a \
	$(BASE_DIR)/third-64/protobuf/lib/libprotobuf.a \
	$(BASE_DIR)/third-64/protobuf/lib/libprotoc.a \
	$(BASE_DIR)/third-64/protobuf/lib/libprotobuf-lite.a \
	$(BASE_DIR)/third-64/tcmalloc/lib/libprofiler.a \
	$(BASE_DIR)/third-64/tcmalloc/lib/libtcmalloc.a \
	$(BASE_DIR)/public/comlogext/cronoapd/libcomlog_cronoapd.a \
	$(BASE_DIR)/third-64/boost/lib/libboost_thread.a \
	$(BASE_DIR)/third-64/boost/lib/libboost_system.a \
	$(BASE_DIR)/third-64/boost/lib/libboost_filesystem.a \
	$(BASE_DIR)/third-64/boost/lib/libboost_date_time.a \
	$(BASE_DIR)/third-64/mongo-client/lib/libmongoclient.a \
	$(BASE_DIR)/op/oped/noah/webfoot/naming-lib/output/lib/libwebfoot_naming.a \
	$(BASE_DIR)/third-64/jsoncpp/libs/linux-gcc-4.4.7/libjson_linux-gcc-4.4.7_libmt.a \
	-lpthread -lcrypto -lrt -ldl \
	-Xlinker "-)"

all : bin/detailKey
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40mall[0m']"
	@echo "make all done"

clean:
	@find . -name "*.o" |xargs -i rm {}
	-@rm -f bin/detailKey
	@echo "clean done"
.phony:clean

# OBJ文件列表
SERVER_OBJS := $(patsubst %.cpp,%.o, $(shell find src -name "*.cpp" |grep -v "main.cpp"))

# 编译cpp文件为OBJ 
%.o:%.cc
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40m$<[0m']"
	$(CXX) $(CXXFLAGS) $(INC_DIR) -c $< -o $@

# 生成目标二进制
bin/detailKey : $(SERVER_OBJS) 
	$(CXX) -o $@ $(CFLAGS) $(INC_DIR) $(CXXFLAGS) \
		src/main.cpp $(SERVER_OBJS) $(LIB_DIR)
