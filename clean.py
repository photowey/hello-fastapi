import os
import shutil
from pathlib import Path


def main():
    """
    删除构建过程中生成的临时文件和目录。
    """

    # 定义要删除的目录列表
    directories_to_clean = ["build", "dist"]

    # 移除指定的目录
    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"Removing {directory}")
            shutil.rmtree(directory)

    # 移除 .egg-info 文件夹
    for item in Path('.').glob('*/*.egg-info'):
        if item.is_dir():
            print(f"Removing {item}")
            shutil.rmtree(item)

    # 移除 .spec 文件
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    # 移除 .log 文件
    for file in os.listdir('.'):
        if file.endswith('.log'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    print("Clean operation completed.")


if __name__ == "__main__":
    main()
