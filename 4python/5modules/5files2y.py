import os
import zipfile

my_dir='sesac'

#디렉토리 안에 파일만 읽어오기
for filename in os.listdir(my_dir):
    file_path=os.path.join(my_dir,filename)
    if(os.path.isfile(file_path)):
        zip_filename = f'{file_path}.zip'

        with zipfile.ZipFile(zip_filename,'w') as zipf:
            zipf.write(file_path, arcname=filename)
            print(f'{filename}을 {zip_filename}으로 압축')

        os.remove(file_path)
        print('원본 삭제')