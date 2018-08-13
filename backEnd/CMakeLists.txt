cmake_minimum_required(VERSION 3.10)
project(newdatabase)

set(CMAKE_CXX_STANDARD 11)

include_directories(./header/)

add_executable(newdatabase main.cpp
        header/interpreter.h
        header/utility.h
        header/bptree/BPlusTree.hpp
        header/bptree/BufferManager.hpp
        header/bptree/constant.h
        header/bptree/vector.hpp
        header/bptree/TreeNode.hpp
        header/key_val/train_info_kv.h
        header/key_val/user_kv.h
        header/constant.h
        header/key_val/train_id_kv.h
        header/key_val/station_kv.h
        header/processor.h
        header/key_val/ticket_kv.h header/key_val/bill_kv.h
        )