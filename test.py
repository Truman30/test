import os

# 输出路径
output_path = "/data/output.txt"

# 执行 nvidia-smi
stream = os.popen("nvidia-smi")
gpu_info = stream.read()



# 写入文件
with open(output_path, "w") as f:
    f.write(gpu_info)

print(f"GPU 信息已写入 {output_path}")