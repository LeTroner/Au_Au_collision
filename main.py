import string
import itertools
from data import *
AuAu_list_dict = {}
AuAu_list = []

with open("AuAu_cut.txt") as f:
    for lines in itertools.islice(f, 1, None):
        for line in f:
            cur_part = ''                                                       # resets current particle
            for i in range(20, 26):                                             # runs thru on indexes 20-26
                try:
                    cur_part += line[i]                                             # the line i-th char puts into cur_part
                    cur_part = cur_part.strip()                                     # removing whitespace
                except IndexError:
                    line = line
            AuAu_list.append(int(cur_part))                                          # adding every read cur_part to the list
# -----------------PROBLEM WHEN REACHING A STRING ------------------------------------
        for c in AuAu_list:                                                     # looping thru the particles in the same list
            #if c not in AuAu_dict:
            #    print("Current particle are not in the dictionary ")
            #else:
                if c not in AuAu_list_dict:                                     # checking if the dict has already the key or not
                    AuAu_list_dict[c] = 1
                else:
                    AuAu_list_dict[c] += 1
#            for p in AuAu_list:
#                AuAu_list_dict[p] = AuAu_dict[p]
    print(AuAu_list_dict)
# print(AuAu_list)
