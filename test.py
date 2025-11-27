import numpy as np

# 创建一个 NumPy 数组
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# 基本运算
sum_result = a + b
mul_result = a * 2
dot_result = np.dot(a, b)

# 打印结果到屏幕
print("数组 a:", a)
print("数组 b:", b)
print("a + b:", sum_result)
print("a * 2:", mul_result)
print("a 和 b 的点积:", dot_result)

# 将输出写入文件
with open("./data/output.txt", "w", encoding="utf-8") as f:
    f.write("数组 a: " + str(a) + "\n")
    f.write("数组 b: " + str(b) + "\n")
    f.write("a + b: " + str(sum_result) + "\n")
    f.write("a * 2: " + str(mul_result) + "\n")
    f.write("a 和 b 的点积: " + str(dot_result) + "\n")

print("\n结果已写入 output.txt 文件！")
