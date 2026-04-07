import torch
print(f"PyTorch版本: {torch.__version__}")
print(f"GPU是否可用: {torch.cuda.is_available()}")  # 显示True表示GPU版安装成功
import openslide