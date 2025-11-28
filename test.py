import os
import subprocess

# 日志文件路径
log_path = "/data/gpu_log.txt"



# 运行 nvidia-smi，并捕获 stdout 和 stderr
try:
    result = subprocess.run(
        ["nvidia-smi"],
        capture_output=True,
        text=True
    )

    output = ""
    output += "=== STDOUT ===\n"
    output += result.stdout if result.stdout else "<empty>\n"
    output += "\n=== STDERR ===\n"
    output += result.stderr if result.stderr else "<empty>\n"

except Exception as e:
    output = f"Error executing nvidia-smi: {str(e)}"

# 写入文件
with open(log_path, "w") as f:
    f.write(output)

print(f"GPU 日志已写入: {log_path}")
