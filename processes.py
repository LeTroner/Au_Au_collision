from data import *
import string
import itertools

#defining a particle counter
def countPart(file):
    particle_list = []
    particle = 0
    event = 1
    with open(file) as f:
        lines = f.readlines()[28:]
        #reading thru the lines
        for line in range(len(lines)):
            try:
                #on every line the particle id is on the same
                #spot, with this method, we only get the ID
                particle = int(lines[line].split()[1])
                particle_list.append(particle)
                #if the current particle is not in the
                #AuAu_list_dict yet, assign 1 to its
                #value
            except IndexError:
                line += 2
                event += 1
            if particle not in AuAu_list_dict:
                AuAu_list_dict[particle] = 1
            AuAu_list_dict[particle] += 1
        print(AuAu_list_dict)
        print(event)
        print(" number of events occured")


'''        
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