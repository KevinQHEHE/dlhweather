import os
import json

import re

def rename_user_in_file(file_path, old_usernames, new_username):
    """Đọc file, thay thế các chuỗi cần thay bằng chuỗi mới."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        new_content = content
        for old in old_usernames:
            pattern = re.compile(rf'\b\w*{re.escape(old)}\w*\b')
            new_content = pattern.sub(new_username, new_content)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated username in: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def CanReadAndWriteAllFiles(root_folder, requiredFiles):
    """Kiểm tra quyền đọc/ghi tất cả các file cần thiết."""
    for path in requiredFiles:
        file_path = os.path.join(root_folder, path)
        if not os.path.exists(file_path):
            print(f"Error: File does not exist {file_path}")
            return False
        if not os.access(file_path, os.R_OK):
            print(f"Error: Couldn't read file {file_path}")
            return False
        if not os.access(file_path, os.W_OK):
            print(f"Error: Couldn't write to file {file_path}")
            return False
    return True

def rename_user_in_all_files(root_folder, old_usernames, new_username, requiredFiles):
    """Thay thế chuỗi trong tất cả các file chỉ định."""
    for path in requiredFiles:
        file_path = os.path.join(root_folder, path)
        rename_user_in_file(file_path, old_usernames, new_username)

def main():
    """Main function to get user input and start the renaming process."""
    try:
        # load json file
        with open('rename-config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return

    requiredFiles = data.get('requiredFiles', [])
    
    if not requiredFiles:
        print("Error: No required files specified in rename-config.json")
        return

    # get the root folder
    root_folder = os.getcwd() 
    
    # get the old username
    # Cho phép nhập nhiều chuỗi cần thay, cách nhau bởi dấu phẩy
    old_usernames = input("Nhập các chuỗi cần thay (cách nhau bởi dấu phẩy): ").strip().split(",")
    old_usernames = [s.strip() for s in old_usernames if s.strip()]
    if not old_usernames:
        print("Error: Không có chuỗi cần thay.")
        return
    new_username = input("Nhập chuỗi mới: ").strip()
    if not new_username:
        print("Error: Chuỗi mới không được để trống.")
        return
    canAccess = CanReadAndWriteAllFiles(root_folder, requiredFiles)
    print(canAccess)
    if not canAccess:
        print("Error: Couldn't access required files.")
        return
    rename_user_in_all_files(root_folder, old_usernames, new_username, requiredFiles)
    print("Done!")

if __name__ == "__main__":
    main()
