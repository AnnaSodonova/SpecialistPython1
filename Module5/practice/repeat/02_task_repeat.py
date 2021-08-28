# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    is_palindrome = True
    for i in range(len(number)):
        if number[i] != number[-1-i]:
            is_palindrome = False
    if is_palindrome:
        return 'The number is a palindrome'
    else:
        return 'The number is not a palindrome'
