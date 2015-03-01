


lowercase_charset = "abcdefghijklmnopqrstuvwxyz"
uppercase_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_charset = "0123456789"
special_charset = "_+."



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


def generate_all_charset_count_passwords_statistic():
    charset = lowercase_charset + uppercase_charset + numbers_charset + special_charset
    for c in charset:
        n = count_passwords_contains_char(c)
        print("Number of passwords that contain " + c + ": " + str(n))

def generate_all_charset_frequency_statistic():
    charset = lowercase_charset + uppercase_charset + numbers_charset + special_charset
    for c in charset:
        n = char_frequency(c)
        print("Frequency of " + c + ": " + str(n))


if __name__ == '__main__':
    '''
    a_password_couter = count_passwords_contains_char('a')
    print("Number of passwords that contain a: " + str(a_password_couter))

    a_frequency = char_frequency('a')
    print("Frequency of a: " + str(a_frequency))
    '''
    generate_all_charset_count_passwords_statistic()
    generate_all_charset_frequency_statistic()
