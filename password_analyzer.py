import re

from util.csvconverter import export_csv_two_equal_column


lowercase_charset = "abcdefghijklmnopqrstuvwxyz"
uppercase_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_charset = "0123456789"
special_charset = "_+.-@[]!?()%&*,"

all_charset = lowercase_charset + uppercase_charset + numbers_charset + special_charset



# groups
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"


# patterns
one_consecutive_vowels = '.*[' + vowels + ']{1,}.*'
two_consecutive_vowels = '.*[' + vowels + ']{2,}.*'
three_consecutive_vowels = '.*[' + vowels + ']{3,}.*'
four_consecutive_vowels = '.*[' + vowels + ']{4,}.*'
five_consecutive_vowels = '.*[' + vowels + ']{5,}.*'

one_consecutive_consonants = '.*[' + consonants + ']{1,}.*'
two_consecutive_consonants = '.*[' + consonants + ']{2,}.*'
three_consecutive_consonants = '.*[' + consonants + ']{3,}.*'
four_consecutive_consonants = '.*[' + consonants + ']{4,}.*'
five_consecutive_consonants = '.*[' + consonants + ']{5,}.*'

one_consecutive_equal_loweruppercase = '.*([a-zA-Z]).*'
two_consecutive_equal_loweruppercase = '.*([a-zA-Z])\\1.*'
three_consecutive_equal_loweruppercase = '.*([a-zA-Z])\\1\\1.*'
four_consecutive_equal_loweruppercase = '.*([a-zA-Z])\\1\\1\\1.*'

one_consecutive_numbers = '.*([0-9]).*'
two_consecutive_numbers = '.*([0-9])\\1.*'
three_consecutive_numbers = '.*([0-9])\\1\\1.*'
four_consecutive_numbers = '.*([0-9])\\1\\1\\1.*'



def database_length():
    f = open('db/passwords_db', 'r')
    #f = open('db/example_db', 'r')
    lines = f.readlines()
    f.close()

    counter = 0
    for line in lines:
        counter += 1

    return counter

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
    counts = []
    counts.append(database_length())
    for c in charset:
        n = count_passwords_contains_char(c)
        counts.append(n)
        print("Number of passwords that contain " + c + ": " + str(n))

    list1 = ["Total"]
    list1.extend(list(charset))

    export_csv_two_equal_column("charset_count_passwords.csv", "Letter", list1, "Passwords Count", counts)


def generate_all_charset_frequency_statistic():
    charset = lowercase_charset + uppercase_charset + numbers_charset + special_charset
    counts = []
    for c in charset:
        n = char_frequency(c)
        counts.append(n)
        print("Frequency of " + c + ": " + str(n))

    export_csv_two_equal_column("frequency_letter.csv", "Letter", charset, "Frequency", counts)


def count_pattern(pattern):
    f = open('db/passwords_db', 'r')
    #f = open('db/example_db', 'r')
    lines = f.readlines()
    f.close()

    counter = 0
    for line in lines:
        if re.match(pattern, line) is not None:
            counter += 1

    return counter

def generate_patterns_statistic():
    charset = lowercase_charset + uppercase_charset + numbers_charset + special_charset
    counts = []
    for c in charset:
        n = char_frequency(c)
        counts.append(n)
        print("Frequency of " + c + ": " + str(n))

    export_csv_two_equal_column("frequency_letter.csv", "Letter", charset, "Frequency", counts)


if __name__ == '__main__':
    '''
    a_password_couter = count_passwords_contains_char('a')
    print("Number of passwords that contain a: " + str(a_password_couter))

    a_frequency = char_frequency('a')
    print("Frequency of a: " + str(a_frequency))

    generate_all_charset_count_passwords_statistic()
    generate_all_charset_frequency_statistic()
    '''
    res = count_pattern(four_consecutive_numbers)
    print(res)