import torch
import sys
import os
print("=== 1. PyTorch 环境验证 ===")
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA是否可用: {torch.cuda.is_available()}")

print("\n=== 2. OpenSlide 环境验证 ===")
try:
    # 注意：以下路径需替换为你的实际解压路径
    openslide_dll_path = r'C:\ProgramData\anaconda3\Library\openslide-bin-4.0.0.11-windows-x64\bin'
    if hasattr(os, 'add_dll_directory'):
        with os.add_dll_directory(openslide_dll_path):
            import openslide
    else:
        import openslide
    print(f"OpenSlide 导入成功！")
    # 尝试创建一个虚拟的slide对象来进一步测试（不会真正读取文件）
    slide_obj = openslide.OpenSlide
    print("OpenSlide 基本功能正常。")
except Exception as e:
    print(f"OpenSlide 导入或初始化失败: {e}")
    sys.exit(1)

print("\n✅ 恭喜！PyTorch 与 OpenSlide 环境均已就绪。")
x = torch.rand(5, 3)
print(x)