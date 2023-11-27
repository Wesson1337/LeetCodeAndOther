# from typing import Callable, Generator
#
#
# def bubble_sort(nums: list[int]) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(len(nums) - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
#
# print(list1 == list2)
#
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# print(tuple1 is tuple2)
# print(id(tuple1), id(tuple2))
#
#
# def some_func(some_arg: list = []):
#     print(id(some_arg))
#     some_arg.append(1)
#     return some_arg
#
#
# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())
#
#
# # background_tasks = list()
# #
# #
# # async def callee():
# #     print(background_tasks)
# #     return "Hello"
# #
# #
# # async def caller():
# #     for i in range(10):
# #         task = asyncio.create_task(callee())
# #         background_tasks.append(task)
# #         task.add_done_callback(background_tasks.clear)
# #     await asyncio.gather(*background_tasks)
# #     print(background_tasks)
# #
# #
# # asyncio.run(caller())
#
#
# from copy import deepcopy
#
# some_list = [1, [2], 3]
#
# some_list2 = some_list.copy()
# some_list3 = deepcopy(some_list)
# some_list[1][0] = 1
#
# print(some_list2)
# print(some_list3)
#
#
# def outer(num: int) -> Callable:
#     def wrapper(func: Callable) -> Callable:
#         def inner(*args, **kwargs):
#             args = list(args)
#             args[0] = -args[0] * num
#             return func(*args, **kwargs)
#         return inner
#     return wrapper
#
#
#
# @outer(5)
# def foo(length: int = 10) -> list:
#     is_less_than_zero = length < 0
#     return [-i if is_less_than_zero else i for i in range(1, abs(length) + 1) if i % 2 == 0]
#
#
# print(foo(10))
#
from abc import ABC, abstractmethod


def some_gen(nums: list):
    for i in nums:
        a = yield
        print(a)


lst = [1, 2, 3]
gen = some_gen(lst)
gen.send(None)
gen.send(2)
gen.send(3)

lst = [1, [2], 3]


def test():
    lst.append(1)


test()
print(lst)

print(list.__mro__)


class Abstract(ABC):
    @abstractmethod
    def abstr(self):
        raise NotImplemented


class Child(Abstract):
    def abstr(self):
        print("Implemented")


print(Child().abstr())

lst1 = [4, 1, 5, 4, 10, 4]
print(lst1.index(4, 3))
print(lst1.index(4, 4))
print(lst1.index(1))
print(lst1.index(4))

# import sys
# n = sys.stdin.readline().strip()
#
# prev_number = int(sys.stdin.readline().strip())
#
# for i in range(1, int(n)):
#     next_number = int(sys.stdin.readline().strip())
#     if prev_number != next_number or i == int(n) - 1:
#         print(prev_number)
#     prev_number = next_number
