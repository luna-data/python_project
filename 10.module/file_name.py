import os

def change_extension(directory, old_ext, new_ext):
    if not os.path.isdir(directory):
        print(f"'{directory}' 는 유효한 디렉토리가 아닙니다.")