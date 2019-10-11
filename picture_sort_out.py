import os.path
import shutil
import re

target_folder = input('please input your folder dir to be operated:')
dst = input('please input your new folder dir:')
exclude_file_suffix = input('please input your exclude file suffix:')
all_file_count = 0
move_done_file = 0
for parent, _, file_names in os.walk(target_folder):
    for filename in file_names:
        src = os.path.join(parent ,filename)
        if exclude_file_suffix == '':
            pass
        elif re.findall('(.*){}'.format(exclude_file_suffix), filename):
            continue
        else:
            pass
        try:
            shutil.move(src, dst)
            all_file_count = all_file_count + 1
            move_done_file = move_done_file + 1
        except shutil.Error as e:
            all_file_count = all_file_count + 1
            print("filename already exists, please rename this file.")
            print("Duplicate file full path:" + os.path.join(parent, filename))

print('all file count:' + str(all_file_count))
print('move success file count:' + str(move_done_file))