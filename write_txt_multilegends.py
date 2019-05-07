#!/usr/bin/python3
"""
Functions related to create a new txt file to write the data into 

"""
def create_file(file_name):
    """
    create a new file
    :param file_name: the name of the file
    :type: string
    :return:
    """

    f = open(file_name, 'a+')
    return f

def write_header(f, legend):
    """
    write data of one legend into txt file
    :param f: file
    :type f: file
    :param legend: one legend
    :type legend: one legend
    :return: f
    """

    f.write(legend + '\t')

    return f


def write_matrix(x, matrix, f):
    """
    write a matrix into the file, one row is one legend
    :param x: the array of variable x
    :type x: numpy array
    :param matrix: 2D data array, one dimension is variable x, the other is category(legend)
    :type matrix: 2D numpy array
    :param f: file
    :type f: file name
    :return: txt format file
    """

    num_legend = matrix.shape[0]
    num_variable_x = matrix.shape[1]
    for i in range(num_variable_x):
        f.write(str(x[i]) + '\t')
        for j in range(num_legend):
            f.write(str(matrix[i][j]) + '\t')
        f.write('\n')
    return f

def close_file(f):
    """
    close the txt format file
    :param f: file to close
    :return:
    """

    f.close()

