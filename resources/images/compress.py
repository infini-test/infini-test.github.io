# -*- coding:utf-8 -*-
# author: s4zuyf
# date: 2025/4/9 16:32
# software: PyCharm
import os

from PIL import Image


working_dir = r"D:\infini-test.github.io\resources\images"
# 打开图片


filelist = os.listdir(working_dir)
for file in filelist:
    # print(file)
    filepath = os.path.join(working_dir, file)
    if os.path.isfile(filepath):
        print(file)

        img = Image.open(filepath)

        # 保存图片并调整质量
        img.save(file, quality=50)  # quality参数控制压缩质量，范围是1-95