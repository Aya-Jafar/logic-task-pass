
# Q1/ Write a method that will remove any given character from a String?
def remove_char(char_to_remove, old_string):
    new_string = ''.join([
        i for i in old_string if i != char_to_remove.lower()
    ])
    return new_string
    # or ...
    # return old_string.replace(char.lower(), '')


print(remove_char('A', 'aya'))  # output => y


# Q2/ Write a program to find all prime numbers up to a given range
# of numbers?
def find_prime_numbers(start, end):

    prime_numbers = list()
    numbers = range(start, end+1)

    for num in numbers:
        flag =  True if num != 1 else False
        for j in range(2, num):
            if num % j == 0:  # not prime
                flag = False
                break
        if flag:
            prime_numbers.append(num)

    return prime_numbers


print(find_prime_numbers(1, 11))  # output => [2, 3, 5, 7, 11]


# Q3/write a function that count how many the given character repeated
# in a given string?
def count_repeated_chars(given_char, string):
    count = 0
    for i in string:
        if i == given_char.lower() : 
            count += 1
    return count
    # or...
    # return string.count(given_char)


print(count_repeated_chars('a', 'aya')) # output => 2
