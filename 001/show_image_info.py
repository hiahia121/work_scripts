# -*- coding: utf-8 -*-
import json

# 读d文件，data转成string
def _file_data2_str(file_path):
    f = open(file_path, "r")
    str_json = ""
    for line in f:
        line = line.strip()
        str_json += line
    f.close()
    return str_json


# 按照use_count排序，输出uuid和使用频次
def data_str2_items(str_input):
    ret = json.loads(str_input)
    resorted_items = sorted(ret.items(), key=lambda x: x[1]["use_count"])
    for item in resorted_items:
        uuid = item[0]
        use_count = item[1]["use_count"]
        print("%s\t%s" % (uuid, use_count))


if __name__ == "__main__":
    file_path = "./data/images_cache.json"
    str_input = _file_data2_str(file_path)
    data_str2_items(str_input)