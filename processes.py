from data import *
import string
import itertools

def countPart(file):
    with open(file) as f:
        lines = f.readlines()
        print(type(lines))
'''        for lines in itertools.islice(f, 1, None):
            for line in f:
                    # resets current particle
                    cur_part = ''
                    # runs thru on indexes 20-26 because there are
                    #the particle ID
                    for i in range(20, 26):
                        try:
                            # the line i-th char puts into cur_part
                            cur_part += line[i]
                            # removing whitespace
                            cur_part = cur_part.strip()
                        except (IndexError):
                            pass
                    # adding every read cur_part to the list
                    AuAu_list.append(int(cur_part))
                # looping thru the particles in the same list
            for c in AuAu_list:
                #if c not in AuAu_dict:
                #    print("Current particle are not in the dictionary ")
                #else:
                    # checking if the dict has already the key or not
                    if c not in AuAu_list_dict:
                        AuAu_list_dict[c] = 1
                    else:
                        AuAu_list_dict[c] += 1
    #            for p in AuAu_list:
    #                AuAu_list_dict[p] = AuAu_dict[p]
        print(AuAu_list_dict)
    # print(AuAu_list)'''