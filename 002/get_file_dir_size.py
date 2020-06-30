# -*- coding: utf-8 -*-
import os

# 相当于linux系统下，使用df -h ./
# 输出目录下总共size空间大小

# 1G = 1073741824 Bytes
Gi = 1073741824

path = "./"
statvfs = os.statvfs(path)

f_bsize = statvfs.f_bsize
f_blocks = statvfs.f_blocks

path_total_size = float(f_bsize * f_blocks) / Gi

print (path_total_size)