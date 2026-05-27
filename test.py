import os

root_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(root_dir, "output")
print(save_dir)

print(f"{'-'*50}")
print(f"开始识别图片...")
print(f"{'-'*50}")