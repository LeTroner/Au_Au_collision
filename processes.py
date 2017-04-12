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
            try:
                nextLine = next(f).split()
            except StopIteration:
                print(" The file contains no more lines ")

            split_line = line.split()
            #if the current line first word is BEGINNINOFEVENT
            #then add 1 to the event counter and check if we got the same
            #amount of particle as it was in the line
            if nextLine[0] == 'BEGINNINGOFEVENT':
                line_0 = int(split_line[0])
                if line_0/numberofParticle != 1:
                    print(" Error 1")
                continue
            if split_line[0] == 'BEGINNINGOFEVENT':
                #setting the current event's numbers
                numberofParticle = 0
                event += 1
                #splitting the very after of the beginningofevent line
                #the second item of the line is #of the particles
                numberofParticle = int(nextLine[1])
                nextLine = 0
                try:
                    split_line = f.next().split()
                except StopIteration:
                    pass
            #splitting the line because above we had already the line
            #we need
            particle = int(split_line[1])
            if particle not in AuAu_list_dict:
                AuAu_list_dict[particle] = 1
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