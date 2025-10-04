import os

def validate_dir_path(working_directory, directory="."):
    target = os.path.join(working_directory, directory)

    dir_stack = []
    for cd in target.split("/"):
        if cd == "..":
            try:
                dir_stack.pop()
            except IndexError:
                raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted directory')

        elif cd == "." or cd == "":
            continue

        elif "." in cd:
            raise Exception(f'Error: "{directory}" is not a directory')

        else:
            dir_stack.append(cd)


    if working_directory not in dir_stack:
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted directory')

    return target

def get_files_info(working_directory, directory="."):
    dir_path = None
    try:
        dir_path = validate_dir_path(working_directory, directory)

    except Exception as e:
        return e

    files = os.scandir(dir_path)
    contents = ""

    for file in files:
        contents = f"{contents}- {file.name}: file_size={file.stat().st_size}, is_dir={file.is_dir()}\n"

    return contents
