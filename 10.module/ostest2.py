import os
def list_files_in_directory(directory):
    if not os.path.isdir(directory):
        print(f"'{directory}'은 유효한 디렉토리가 아닙니다.")
        return
    print(f"디렉토리 '{directory}' 안의 파일 : ")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            print(filename)

target_directory = 'c:\\python\\'

list_files_in_directory(target_directory)