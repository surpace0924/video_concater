import os
import re
import sys
import shutil

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    rename_files_and_folders(directory_path)


def rename_files_and_folders(directory):
    # ディレクトリ内のアイテム（ファイルおよびフォルダ）を取得
    for root, dirs, files in os.walk(directory, topdown=False):
        # ファイルのリネーム
        for filename in files:
            old_file_path = os.path.join(root, filename)
            new_filename = re.sub(r'\[.*?\]', '', filename).strip()
            new_file_path = os.path.join(root, new_filename)
            
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed file: {old_file_path} to {new_file_path}')

        # フォルダのリネーム
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            new_dirname = re.sub(r'\[.*?\]', '', dirname).strip()
            new_dir_path = os.path.join(root, new_dirname)
            
            if old_dir_path != new_dir_path:
                if os.path.exists(new_dir_path):
                    shutil.rmtree(new_dir_path)
                    print(f'Deleted existing directory: {new_dir_path}')
                
                os.rename(old_dir_path, new_dir_path)
                print(f'Renamed directory: {old_dir_path} to {new_dir_path}')


if __name__ == "__main__":
    main()

