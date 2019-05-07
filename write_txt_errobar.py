#!/usr/bin/python3
"""
Functions related to create a new txt file to write the data into 

"""
def create_file(file_name):
    """
    create a new file
    :param file_name: the name of the file
    :type file_name: string
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


def write_row(row, f):
    """
    write row of one legend, both average value and error bar
    :param row: data array in one directory, including average value and error bar
    :type row: numpy array
    :param f: file
    :type f: file name
    :return: txt format file
    """

    for value, error_bar in zip(row[0], row[1]):
        f.write('\t' + str(value) + '\t' + str(error_bar))
    f.write('\n')
    return f

def close_file(f):
    """
    close the txt format file
    :param f: file to close
    :return:
    """

    f.close()

