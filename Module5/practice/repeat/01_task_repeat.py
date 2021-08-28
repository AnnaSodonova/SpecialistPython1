# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random


def gen_list(size, of, to):
    list_of_values = range(of, to + 1)
    return random.sample(list_of_values, size)

