import random
import sys

# Initialize Pygame

# 生成10个随机数（范围1-100）
numbers = [random.randint(1, 100) for _ in range(10)]

# 打印原始数列
print("原始数列:", numbers)

# 对数列进行排序
sorted_numbers = sorted(numbers)

# 打印排序后的数列
print("排序后:", sorted_numbers)


