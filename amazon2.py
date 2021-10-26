#!/bin/python
import math
import os
import random
import re
import sys
#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#

# def foo(codeList, shoppingCart):
    
#     if codeList.count is 0:
#         return 1
    
#     for cList in codeList:
#         start = -1
#         gap = 0
#         # print "C : ",cList
#         # print "C split : ", cList[0].split()
#         for index, sCart in enumerate(shoppingCart):
#             print "s  ",sCart
#             if sCart in cList[0].split() or sCart.lower() is 'anything':
#                 start = index
#                 print "start before : ", start

#             if start > 0:
#                 print "start after ", start, " : ", index
#                 if start != index:
#                     return 0
#     return 1

# def foo(codeList, shoppingCart):

#     if codeList.count is 0:
#         return 1
    
#     for cList in codeList:

#         cListSplit = cList[0].split()
#         start = -1
#         index = 0

#         while index < len(cListSplit):

#             if shoppingCart[0] in cListSplit or shoppingCart[0] is 'anything':
#                 start = index

#             shoppingCart.pop(0)

#             print start, " : ", index

#             if start > 0:
#                 if start != index:
#                     return 0

#             index += 1

#     return 1

def freshPromotion(promotions, orders):
    p_idx = o_idx = 0
        # 1st loop until both index reach their size
    while p_idx < len(promotions) and o_idx < len(orders):
        # put the each promotion combination into a list
        promo_combination = promotions[p_idx]
        # initialize the above combination index
        promo_idx = 0
        # loop through the promo_combination and orders to see if
        # it satisfies
        while promo_idx < len(promo_combination) and o_idx < len(orders):
            # now compare each combination with the order and also wild card anything
            if promo_combination[promo_idx] == orders[o_idx] or promo_combination[promo_idx] == "anything":
                # increment the promo_idx
                promo_idx += 1
            else:
                # if not start the comparision from beginning
                promo_idx = 0
            # move to next order
            o_idx += 1
        if promo_idx != len(promo_combination):
            return False
        # move to next promotion combinations
        p_idx += 1
    # if the promotion index is less than total promotions
    # return False
    if p_idx < len(promotions):
        return False
    return True
                    

# codeList = [['apple apple'], ['banana anything banana']]
# shoppingCart = ['apple','apple','orange','orange','orange']


# print (freshPromotion(codeList, shoppingCart))


if __name__ == '__main__':
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['anything','anything','anything','anything','orange', 'apple', 'apple','anything','anything','anything', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'apple', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['banana', 'orange', 'banana', 'apple', 'apple']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['anything', 'anything','anything', 'banana', 'anything', 'banana']],
                          ['apple', 'apple', 'apple', 'banana']) \
           == False