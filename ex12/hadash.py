# # # def max_find(lst):
# #     lo = 0
# #     hi = len(lst)
# #     while lo < hi:
# #         mid = (lo + hi) // 2
# #         val = lst[mid]
# #         if val > lst[mid + 1]:
# #             hi = mid
# #         elif val < lst[mid + 1]:
# #             lo = mid + 1
# #     return lst[lo]
# #
# #
# # def bubble_sort(l):
# #     n = len(l)
# #     for i in range(n):
# #         for j in range(n - i - 1):
# #             if l[j] > l[j + 1]:
# #                 t = l[j + 1]
# #                 l[j + 1] = l[j]
# #                 l[j] = t
# #     return l
# #
# #
# # def merge_sort(l):
# #     if len(l) == 1:
# #         return l
# #     mid = len(l) // 2
# #     num1 = merge_sort(l[mid:])
# #     num2 = merge_sort(l[:mid])
# #     lst = ["" for i in range(10)]
# #     if num1[0] > num2[0]:
# #         lst[0] = num1[0]
# #         lst[1] = num2[0]
# #     else:
# #         lst[0] = num2[0]
# #         lst[1] = num1[0]
# #     return lst
#
#
# # # print(merge_sort([81, 82, 83, 84, 828, 14, 10, 3, 3]))
# # ls = [[1,2,3]]
# # ls2 = ls*3
# # print(ls)
# # print(ls2)
# # ls[0][2]=4
# # print(ls)
# # print(ls2)
# #
# #
# # class It:
# #     def __init__(self):
# #         self.n= 5
# #         self.i=0
# #
# #     def __iter__(self):
# #         yield 2
# #         yield 3
# #         yield 7
# #
# #
#
#
# # def __next__(self):
# #     self.i += 1
# #     if self.i <= self.n:
# #         return self.i
# #     raise StopIteration
#
#
# #
# # p1 = 1
# # p2 = 2
# # def p_change():
# #     while True:
# #         yield p1
# #         yield p2
# # p = p_change()
# # print(next(p))
# # print(next(p))
# # print(next(p))
# # print(next(p))
#
# # def tt(n):
# #     for i in range(n):
# #         yield i
# # t = tt(4)
# # print(next(t))
# # print(next(t))
# # print(next(t))
# # print(next(t))
# # print(next(t))
# #
# # print("popopop".count("pop"))
# #
# # g = lambda x: x+7
# # foo = lambda f: (lambda x: f(x+1)*2)
# # print( g(3), (foo(g))(3), (foo(foo(g)))(3))
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data, self.next = data, next
#
#
# lst = Node('a', Node('b', Node('c', Node('d', Node('e')))))
# lst1 = Node('1', Node('2', Node('3', Node('4', Node('5')))))
#
#
# def get_reverse(lst):
#     cur = lst
#     lst2 = []
#
#     while cur.next != None:
#         lst2.append(cur.data)
#         cur = cur.next
#     lst2.append(cur.data)
#
#     for i in lst2[::-1]:
#         yield i
#
#
# for i in get_reverse(lst):
#     print(i)
#
#
# def zipper(head1, head2):
#     len = 0
#     cur = head1
#     while cur.next != None:
#         cur = cur.next
#         len += 1
#     len += 1
#     flag = False
#     start1 = head1
#     start2 = head2
#     for i in range(2 * len):
#         temp1 = head1.next
#         temp2 = head2.next
#         if flag:
#             head1.next = head2
#             head2.next = head1
#
#         head1 = temp1.next
#         head2 = temp2.next
#     head1 = start1
#     head2 = start2
#
#
# # zipper(lst,lst1)
#
# def count_sums(a, s):
#     count = [0]
#     _helper(a[:], s, count, 0)
#     return count[0]
#
#
# def _helper(a, s, count, sum):
#     if sum > s:
#         return
#     if sum == s:
#         count[0] += 1
#         return
#     else:
#         for i in a:
#             sum += i
#             _helper(a, s, count, sum)
#             sum -= i
#
#
# def power_sets(lst):
#     out = [[]]
#     for item in lst:
#         out += [out_item + [item] for out_item in out]
#     return out
#
#
# p = power_sets([3, 5, 8, 9, 11, 12, 20])
# t = len(list(filter(lambda x: sum(x) == 20, p)))
# print(t)
#
#
# def subsets(lst):
#     if len(lst) == 0:
#         yield []
#     else:
#         for tail in subsets(lst[1:]):
#             yield tail
#             yield [lst[0]] + tail
#
#
# r = [1, 2, 3, 4]
# p = power_sets(r)
#
# print(p)
# s = subsets(r)
# s1 = []
# for i in s:
#     s1.append(i)
# print(s1)
# print("================================================\n")
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, items))
# print(squared)
# print("================================================\n")
# items = [1, 2, 3, 4, 5]
# items2 = [0, 1, 1, 1, 1]
#
# squared = list(map(lambda x: x ** 2, items + items2))
# print(squared)
#
# print("\n=========================================================\n")
#
# from functools import reduce
#
# product = reduce((lambda x, y: x + y == 7), [2, 2, 3])
# print(product)
#
# print("\n=========================================================\n")
# SPLIT = ","
#
#
# def split(s):
#     lst = []
#     word = ""
#     for i in range(len(s)):
#         if s[i] != SPLIT:
#             word += s[i]
#             if i == len(s) - 1 and word:
#                 lst.append(word)
#         else:
#             if word:
#                 lst.append(word)
#                 word = ""
#     return lst
#
#
# s = "12,3,234,34,34,3534,563,5654,7456,546,7658,57,"
#
# print(split(s))
#
#
# def p():
#     print("\n=========================================================\n")
#
#
# def f(a, b=[2]):
#     c = [x for x in b if x % a]
#     b.append(sum(c))
#     return b
#
#
# print(f(1, [2]))
# print(f(2, [3]))
# print(f(3))
# print(f(5))
#
# t = [('a', 2), ('a', 1)], [('a', 1), ('a', 1)], [('a', 2), ('a', 4)], [
#     ('a', 2), ('b', 7), ('a', 1)], [('a', 1), ('b', 7), ('a', 3)]
#
#
# def verify_sublist_order(iterable):
#     sublists = {}
#     for i in iterable:
#         for k, v in i:
#             if k in sublists and sublists[k] != v - 1:
#                 return False
#             sublists[k] = v
#     return True
#
#
# print(verify_sublist_order(t))
#
# p()
#
# h = iter([1, 2, 3])
# g = range(4)
# print("111")
#
#
# def set_power(s, n):
#     return helper(s, [], [], n, 0)
#
#
# def helper(Lst, sub_List, my_List, n, index):
#     if index == n:
#         my_List.append(list(sub_List))
#         sub_List.pop()
#         return my_List
#     for item in Lst:
#         sub_List.append(item)
#         helper(Lst, sub_List, my_List, n, index + 1)
#     if sub_List:
#         sub_List.pop()
#     return my_List
#
#
# def power_sets(s):
#     out = [[]]
#     for item in s:
#         out += [out_item + [item] for out_item in out]
#     return out
#
#
# # p()
# # s = [1]
# # print(set_power(s,0))
# # print(power_sets(s))
# # p()
# p()
#
#
# def cartesian(s):
#     res = []
#     _helper1(s, res, len(s), "", 0)
#     return res
#
#
# def _helper1(lst, res, max, pre, idx):
#     if len(pre) == max:
#         res.append(pre)
#     else:
#         for i in lst[idx]:
#             _helper1(lst, res, max, pre + i, idx + 1)
#
#
# p()
#
# a = 12
# b = 15
#
# assert b == a, "lalal"
# def max_find(lst):
# #     lo = 0
# #     hi = len(lst)
# #     while lo < hi:
# #         mid = (lo + hi) // 2
# #         val = lst[mid]
# #         if val > lst[mid + 1]:
# #             hi = mid
# #         elif val < lst[mid + 1]:
# #             lo = mid + 1
# #     return lst[lo]
# #
# #
# # def bubble_sort(l):
# #     n = len(l)
# #     for i in range(n):
# #         for j in range(n - i - 1):
# #             if l[j] > l[j + 1]:
# #                 t = l[j + 1]
# #                 l[j + 1] = l[j]
# #                 l[j] = t
# #     return l
# #
# #
# # def merge_sort(l):
# #     if len(l) == 1:
# #         return l
# #     mid = len(l) // 2
# #     num1 = merge_sort(l[mid:])
# #     num2 = merge_sort(l[:mid])
# #     lst = ["" for i in range(10)]
# #     if num1[0] > num2[0]:
# #         lst[0] = num1[0]
# #         lst[1] = num2[0]
# #     else:
# #         lst[0] = num2[0]
# #         lst[1] = num1[0]
# #     return lst
#
#
# # # print(merge_sort([81, 82, 83, 84, 828, 14, 10, 3, 3]))
# # ls = [[1,2,3]]
# # ls2 = ls*3
# # print(ls)
# # print(ls2)
# # ls[0][2]=4
# # print(ls)
# # print(ls2)
# #
# #
# # class It:
# #     def __init__(self):
# #         self.n= 5
# #         self.i=0
# #
# #     def __iter__(self):
# #         yield 2
# #         yield 3
# #         yield 7
# #
# #
#
#
# # def __next__(self):
# #     self.i += 1
# #     if self.i <= self.n:
# #         return self.i
# #     raise StopIteration
#
#
# #
# # p1 = 1
# # p2 = 2
# # def p_change():
# #     while True:
# #         yield p1
# #         yield p2
# # p = p_change()
# # print(next(p))
# # print(next(p))
# # print(next(p))
# # print(next(p))
#
# # def tt(n):
# #     for i in range(n):
# #         yield i
# # t = tt(4)
# # print(next(t))
# # print(next(t))
# # print(next(t))
# # print(next(t))
# # print(next(t))
# #
# # print("popopop".count("pop"))
# #
# # g = lambda x: x+7
# # foo = lambda f: (lambda x: f(x+1)*2)
# # print( g(3), (foo(g))(3), (foo(foo(g)))(3))
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data, self.next = data, next
#
#
# lst = Node('a', Node('b', Node('c', Node('d', Node('e')))))
# lst1 = Node('1', Node('2', Node('3', Node('4', Node('5')))))
#
#
# def get_reverse(lst):
#     cur = lst
#     lst2 = []
#
#     while cur.next != None:
#         lst2.append(cur.data)
#         cur = cur.next
#     lst2.append(cur.data)
#
#     for i in lst2[::-1]:
#         yield i
#
#
# for i in get_reverse(lst):
#     print(i)
#
#
# def zipper(head1, head2):
#     len = 0
#     cur = head1
#     while cur.next != None:
#         cur = cur.next
#         len += 1
#     len += 1
#     flag = False
#     start1 = head1
#     start2 = head2
#     for i in range(2 * len):
#         temp1 = head1.next
#         temp2 = head2.next
#         if flag:
#             head1.next = head2
#             head2.next = head1
#
#         head1 = temp1.next
#         head2 = temp2.next
#     head1 = start1
#     head2 = start2
#
#
# # zipper(lst,lst1)
#
# def count_sums(a, s):
#     count = [0]
#     _helper(a[:], s, count, 0)
#     return count[0]
#
#
# def _helper(a, s, count, sum):
#     if sum > s:
#         return
#     if sum == s:
#         count[0] += 1
#         return
#     else:
#         for i in a:
#             sum += i
#             _helper(a, s, count, sum)
#             sum -= i
#
#
# def power_sets(lst):
#     out = [[]]
#     for item in lst:
#         out += [out_item + [item] for out_item in out]
#     return out
#
#
# p = power_sets([3, 5, 8, 9, 11, 12, 20])
# t = len(list(filter(lambda x: sum(x) == 20, p)))
# print(t)
#
#
# def subsets(lst):
#     if len(lst) == 0:
#         yield []
#     else:
#         for tail in subsets(lst[1:]):
#             yield tail
#             yield [lst[0]] + tail
#
#
# r = [1, 2, 3, 4]
# p = power_sets(r)
#
# print(p)
# s = subsets(r)
# s1 = []
# for i in s:
#     s1.append(i)
# print(s1)
# print("================================================\n")
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, items))
# print(squared)
# print("================================================\n")
# items = [1, 2, 3, 4, 5]
# items2 = [0, 1, 1, 1, 1]
#
# squared = list(map(lambda x: x ** 2, items + items2))
# print(squared)
#
# print("\n=========================================================\n")
#
# from functools import reduce
#
# product = reduce((lambda x, y: x + y == 7), [2, 2, 3])
# print(product)
#
# print("\n=========================================================\n")
# SPLIT = ","
#
#
# def split(s):
#     lst = []
#     word = ""
#     for i in range(len(s)):
#         if s[i] != SPLIT:
#             word += s[i]
#             if i == len(s) - 1 and word:
#                 lst.append(word)
#         else:
#             if word:
#                 lst.append(word)
#                 word = ""
#     return lst
#
#
# s = "12,3,234,34,34,3534,563,5654,7456,546,7658,57,"
#
# print(split(s))
#
#
# def p():
#     print("\n=========================================================\n")
#
#
# def f(a, b=[2]):
#     c = [x for x in b if x % a]
#     b.append(sum(c))
#     return b
#
#
# print(f(1, [2]))
# print(f(2, [3]))
# print(f(3))
# print(f(5))
#
# t = [('a', 2), ('a', 1)], [('a', 1), ('a', 1)], [('a', 2), ('a', 4)], [
#     ('a', 2), ('b', 7), ('a', 1)], [('a', 1), ('b', 7), ('a', 3)]
#
#
# def verify_sublist_order(iterable):
#     sublists = {}
#     for i in iterable:
#         for k, v in i:
#             if k in sublists and sublists[k] != v - 1:
#                 return False
#             sublists[k] = v
#     return True
#
#
# print(verify_sublist_order(t))
#
# p()
#
# h = iter([1, 2, 3])
# g = range(4)
# print("111")
#
#
# def set_power(s, n):
#     return helper(s, [], [], n, 0)
#
#
# def helper(Lst, sub_List, my_List, n, index):
#     if index == n:
#         my_List.append(list(sub_List))
#         sub_List.pop()
#         return my_List
#     for item in Lst:
#         sub_List.append(item)
#         helper(Lst, sub_List, my_List, n, index + 1)
#     if sub_List:
#         sub_List.pop()
#     return my_List
#
#
# def power_sets(s):
#     out = [[]]
#     for item in s:
#         out += [out_item + [item] for out_item in out]
#     return out
#
#
# # p()
# # s = [1]
# # print(set_power(s,0))
# # print(power_sets(s))
# # p()
# p()
#
#
# def cartesian(s):
#     res = []
#     _helper1(s, res, len(s), "", 0)
#     return res
#
#
# def _helper1(lst, res, max, pre, idx):
#     if len(pre) == max:
#         res.append(pre)
#     else:
#         for i in lst[idx]:
#             _helper1(lst, res, max, pre + i, idx + 1)
#
#
# p()
#
# a = 12
# b = 15
#
# assert b == a, "lalal"

