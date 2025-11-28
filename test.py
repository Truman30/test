
import torch

log_path = "/data/outputs.txt"

with open(log_path, "w") as f:
    gpu_count = torch.cuda.device_count()
    f.write(f"GPU 数量: {gpu_count}\n")

    for i in range(gpu_count):
        f.write(f"GPU {i}: {torch.cuda.get_device_name(i)}\n")

print(f"GPU 信息已写入: {log_path}")

