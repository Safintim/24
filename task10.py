from os import listdir
from os.path import isfile, exists


def create_file_with_names_files_from_directory(directory):
    name_output_file = 'monitor_dir.txt'
    files_output_file = get_data_from_file(name_output_file)
    with open(name_output_file, 'w') as f:

        files_directory = [file for file in listdir(directory) if isfile(file)]
        if files_output_file is not None:
            added_files = difference_list(files_directory, files_output_file)
            deleted_files = difference_list(files_output_file, files_directory)

            if added_files:
                print('Добавленные файлы: ', added_files)
            if deleted_files:
                print('Удаленные файлы: ', deleted_files)

        f.write(str(files_directory))


def get_data_from_file(file):
    if exists(file):
        with open(file, 'r') as f:
            t = f.read()
            if t:
                return eval(t)


def difference_list(first, second):
    second = set(second)
    return [item for item in first if item not in second]


monitor_directory = input()
create_file_with_names_files_from_directory(monitor_directory)
