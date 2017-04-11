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
        #print(AuAu_list_dict)
        print(str(event)+ " number of events occured")
        return event

#average particle per event
def avPart(event,part_dict):
#making event to float in order to get
#exact number
#declaring average dict where we store the particle ID and its average per event
    event = float(event)
    average_dict = {}
#looping in the elements of part_dict
    for i in part_dict:
#getting the average particle per event
        average_particle = part_dict.get(i)/event
        average_dict[i] = average_particle
    print("On average in %d"  %int(event) + " event(s) we have: ")
    print(average_dict)
    return average_dict