



def export_csv_two_equal_column(output, first_name, first_list, second_name, second_list):
    f = open(output, 'w+')
    f.write('sep=;\n')
    f.write(first_name + ';' + second_name + '\n')
    for (elem1, elem2) in zip(first_list, second_list):
        f.write(str(elem1) + ';' + str(elem2) + '\n')

    f.close()
