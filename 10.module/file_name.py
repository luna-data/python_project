import os

def change_extension(directory, old_ext, new_ext):
    if not os.path.isdir(directory):
        print(f"'{directory}' 는 유효한 디렉토리가 아닙니다.")
        return
    for filename in os.listdir(directory):  
        if filename.endswith(old_ext):
            old_file_path=directory+"\\"+filename
            new_filename=filename.replace(old_ext, new_ext)
            new_file_path=directory+"\\"+new_filename
            os.rename(old_file_path, new_file_path)
            print(f"'{filename}' 파일의 '{new_filename}'(으)로 변경했습니다.")

target_directory="d:\\test"
old_extension='.c'
new_extension='.py'
change_extension(target_directory, old_extension, new_extension)    