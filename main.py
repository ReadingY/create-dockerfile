import os


def main(root_path, layer_size):
    """
    Return a list of directory group
    :param root_path: The path of data
    :param layer_size: The docker layer size limit
    :return:
    """
    ans = []
    same_copy = []  # To store the directory in one copy command

    sum_size = 0  # To calculate and indicate if this directory put in same copy command
    top_level_directories = next(os.walk(root_path))[1]  # Top level directories
    for d in top_level_directories:
        path = f'{root_path}/{d}'  # Top level directory. I.e. data/dir1, data/dir2
        size = 0  # The size of current top level directory

        for root, dirs, files in os.walk(path):
            for f in files:
                fp = os.path.join(root, f)
                size += os.path.getsize(fp)

        sum_size += size
        if sum_size <= layer_size:
            # If the sum size less than 5 Mib, then the directory should go to same COPY command
            same_copy.append(path)
        else:  # Else create a new list for next COPY command
            ans.append(same_copy)
            same_copy = [path]
            sum_size = size

    ans.append(same_copy)

    # The ans is like:
    # [['data/dir-a01eabb9-4fd4-41e1-b213-b5221ecbfe06', 'data/dir-39d1efac-55f4-4654-bf2d-7d07910abdff'],
    # ['data/dir-c9cff361-692d-4270-ae8e-d8a283494420'], ...]
    return ans


def create_dockerfile(file_name, arr):
    """
    Write arr to Docker file
    :param file_name:
    :param arr:
    :return:
    """
    with open(file_name, 'w') as f:
        f.write('FROM ubuntu\n')
        for i in arr:
            command = 'COPY '
            for j in i:
                command += j + ' '
            command += '/data'
            f.write(command + '\n')


if __name__ == '__main__':
    data_path = 'data'
    docker_layer_size = 5 * 1024 * 1024  # 5 Mib
    directories_group = main(data_path, docker_layer_size)

    dockerfile_name = 'Dockerfile'
    create_dockerfile(dockerfile_name, directories_group)
