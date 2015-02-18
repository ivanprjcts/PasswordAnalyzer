



def count_passwords_contains_char(char):
    f = open('db/passwords_db', 'r')
    #f = open('db/example_db', 'r')
    lines = f.readlines()
    f.close()

    counter = 0
    for line in lines:
        if char in line:
            counter += 1

    return counter

def char_frequency(char):
    f = open('db/passwords_db', 'r')
    #f = open('db/example_db', 'r')
    lines = f.readlines()
    f.close()

    counter = 0
    for line in lines:
        counter += line.count(char)

    return counter


if __name__ == '__main__':
    a_password_couter = count_passwords_contains_char('a')
    print("Number of passwords that contain a: " + str(a_password_couter))

    a_frequency = char_frequency('a')
    print("Frequency of a: " + str(a_frequency))
