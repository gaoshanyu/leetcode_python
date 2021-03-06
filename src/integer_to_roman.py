# coding: utf-8
#                                                    ##       ##
#                                                  #####   #  ####
#                                               ######### ## #######
#                                              ###  ############ ##
#                               ####          #     ####### #########
#  ###########               #########       #      ###########  ##
# #############             ###    ####        ##  #### ########                                     ##
# ##   ##    ##            ##        ###     #########  #########        ###         ##       #     ###      ##      #
#      ##   ##                    ## ###    ########   ##########       #### ##     ###     ####   ###    #####    ####
#     ## ####                     ##  ##   #########   ##########      ########    #####   ####    ####   #####   #####
#    ######          ####        ##   ##  ### ## ###  ############    ## ### ##   ## ##   ###      ###    #####  ### ##
#    ####           #####        ##  ###  ###  ###### ############       ##  ##  #####    ### ##  ###     ###    #####
#   ## ##         ### ###       ###  ###   ######### ##############     ### ##   ####     ## ###  #####  ####    ####
#   ## ###        ##  ##        ##  ###     #####    ##############    #######    #####   #####   #####  ###     ######
#  ##   ###  ##  #######        ######              ###############    ####         ##     ##       #              ###
#  ##   ######   #######       #####               #################   ###
# ##      ###     ##  ##       ###                  #################  ##
# ##                           ##                 ###################  ##
# ##                          ###                  ######################
#                             ##                    #               ## #
#                             ##
# author: RaPoSpectre
# time: 2016-11-07

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                      ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                      ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                      ["", "M", "MM", "MMM"]]
        roman = ''
        roman += roman_list[3][num / 1000 % 10]
        roman += roman_list[2][num / 100 % 10]
        roman += roman_list[1][num / 10 % 10]
        roman += roman_list[0][num % 10]
        return roman


# print Solution().intToRoman(1000)