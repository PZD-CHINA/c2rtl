import os
import shutil

# 定义源文件夹和目标文件夹
source_dir = './'
destination_dir = './rtl'

# 确保目标文件夹存在
os.makedirs(destination_dir, exist_ok=True)

# 遍历所有的项目文件夹
for project_folder in os.listdir(source_dir):
    project_path = os.path.join(source_dir, project_folder)
    # 检查是否是文件夹
    if os.path.isdir(project_path):
        source_file = os.path.join(project_path, 'solution1', 'syn', 'verilog', 'atax.v')
        # 检查源文件是否存在
        if os.path.exists(source_file):
            destination_file = os.path.join(destination_dir, f'{project_folder}_atax.v')
            # 复制文件并重命名
            shutil.copyfile(source_file, destination_file)
            print(f'Copied {source_file} to {destination_file}')
        else:
            print(f'File not found: {source_file}')

print("All files have been processed.")
