import os
import re

def replace_in_api(directory, old_str, new_str):
    for root, dirs, api in os.walk(directory):
        for filename in api:
            filepath = os.path.join(root, filename)
            try:
                # 读取文件内容
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 替换字符串
                new_content = content.replace(old_str, new_str)
                
                # 如果内容有变化，则写入文件
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"已替换: {filepath}")
            except (UnicodeDecodeError, PermissionError) as e:
                # 跳过二进制文件或无权限文件
                print(f"跳过文件: {filepath} ({str(e)})")

if __name__ == "__main__":
    current_dir = os.getcwd()  # 当前目录

    old_input = 'itingshu.vercel.app'
    new_input = 'itingshu.vercel.app'

    print(f"正在替换:\n{old_input}\n→\n{new_input}")
    replace_in_api(current_dir, old_input, new_input)
    print("替换完成！")
