from data import *
import string
import itertools

#defining a particle counter
def countPart(file):
    #declaring variables which will be used to store info
    particle_list = []
    particle = 0
    event = 0
    numberofParticle = 0
    with open(file) as f:
        #reading thru the lines and skipping the first 28 line
        for line in itertools.islice(f, 28, None):
            split_line = line.split()
            if split_line[0] == 'BEGINNINGOFEVENT':
                event += 1
                #splitting the very after of the beginningofevent line
                #the second item of the line is #of the particles
                numberofParticle = int(f.next().split()[1])
                # redeclaring because above we were using the next line to skip
                split_line = f.next().split()

            #if the current line's second item
            #is the same as the numberofParticle
            #then we reached the end of the current event
            try:
                split_line[1] == numberofParticle
                #if the statement is true, continue
            except IndexError:
                #else, there is an error with the amount of
                #particles said and been
                print(" Error 1")
            #the current particle ID is the second item
            #of the split_line
            particle = int(split_line[1])
            #if its not in the dict yet
            #set its value to 1
            if particle not in AuAu_list_dict:
                AuAu_list_dict[particle] = 1
            #else, increase its value by one
            else:
                AuAu_list_dict[particle] += 1
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