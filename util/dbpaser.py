

def delete_username(intput_file, output_file):
    f = open(intput_file, 'r')
    lines = f.readlines()
    f.close()

    f = open(output_file, 'w')
    for line in lines:
        split_line = line.split()
        if len(split_line) == 1:
            f.write(split_line[0] + '\n')
            print(split_line[0])
        else:
            f.write(split_line[1] + '\n')

    f.close()





if __name__ == '__main__':
    delete_username('10-million-combos.txt', 'passwords_db')