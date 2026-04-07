
import os


# 第二步：导入并验证openslide
import openslide
print("OpenSlide导入成功！")
# （可选）测试读取切片（替换为你的切片路径）
# slide = openslide.OpenSlide("你的切片.svs")
# print(f"切片尺寸：{slide.dimensions}")

# 第三步：导入并验证PyTorch GPU版本
import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"GPU是否可用: {torch.cuda.is_available()}")
print(f"CUDA版本: {torch.version.cuda}")

# 第四步：混合运行（openslide读数据 + PyTorch处理）
# 示例：用PyTorch处理openslide读取的切片数据
import numpy as np
# 模拟切片数据（替代真实读取）
fake_slide_data = np.random.rand(3, 512, 512).astype(np.float32)
# 转PyTorch张量并移到GPU
tensor_data = torch.from_numpy(fake_slide_data).cuda()
print(f"张量是否在GPU上: {tensor_data.is_cuda}")
print("OpenSlide + PyTorch GPU 混合运行成功！")
print(torch.cuda.is_available())
