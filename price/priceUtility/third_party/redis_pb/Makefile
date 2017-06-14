
BASE_DIR=/home/baijie.cai/ihotel/base/Tags/base_1-0-1_RL/output/
PROTOC=$(BASE_DIR)/third-64/protobuf/bin/protoc
CXX=g++
CXXFLAGS=-Wall -g
PBINC=$(BASE_DIR)/third-64/protobuf/include
PBLIB=$(BASE_DIR)/third-64/protobuf/lib/libprotobuf.a

INC_DIR=-I./src -I./src/third_party/include/redis -I./src/third_party/include/pb2json -I./interface/gen -I${PBINC}
LIB_INC=${PBLIB} ./src/third_party/lib/libhiredis_vip.a -lpthread

all : bin/detailValue
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40mall[0m']"
	@echo "make all done"

stub : interface/gen/price_types.pb.cc
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40mall[0m']"
	@echo "[[1;32;40mGenerated[0m][stub code. Run '[1;32;40mmake[0m' next]"

clean:
	@find . -name "*.o" |xargs -i rm {}
	@find interface/gen -name "*.cc" -o -name "*.h" -o -name "*.cpp" |xargs -i rm {}
	-@rm -f bin/detailValue
	@echo "clean done"
.phony:clean

interface/gen/price_types.pb.cc : interface/price_types.proto
	$(PROTOC) --cpp_out=./interface/gen --proto_path=./interface ./interface/price_types.proto

# OBJ文件列表
PROTO_SRCS := $(shell find interface -name "*.proto")
SERVER_OBJS := $(patsubst %.cpp,%.o, $(shell find src -name "*.cpp" |grep -v "main.cpp"))
PROTO_OBJS := $(patsubst %.cc,%.o, $(shell find ./interface/gen -name "*.cc"))

# 编译cpp文件为OBJ 
%.o:%.cpp $(PROTO_SRCS)
ifeq ($(PROTO_OBJS),)
	$(error "Please [1;32;40mmake stub[0m first")
else
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40m$<[0m']"
	$(CXX) $(CXXFLAGS) $(INC_DIR) -c $< -o $@
endif

%.o:%.cc
	@echo "[[1;32;40mBUILD[0m][Target:'[1;32;40m$<[0m']"
	$(CXX) $(CXXFLAGS) $(INC_DIR) -c $< -o $@

# 生成目标二进制
bin/detailValue : $(SERVER_OBJS) $(PROTO_OBJS) 
	$(CXX) -o $@ $(CFLAGS) $(INC_DIR) $(CXXFLAGS) \
		src/main.cpp $(PROTO_OBJS) $(SERVER_OBJS) $(LIB_INC)
