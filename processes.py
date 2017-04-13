import string
import itertools
import matplotlib.pyplot as plt
import operator
import numpy as np

#----DECLARING CONSTANTS AND EMPTY VARIABLES

AuAu_dict = {
    '211': 'pi+',
    '111': 'pi0',
    '321': 'K+',
    '311': 'K0',
    '2212': 'p',
    '2112': 'n'
}

AuAu_list_dict = {}
AuAu_list = []
#---------PROCESSES ---------
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
                numberofParticle = int(next(f).split()[1])
                # redeclaring because above we were using the next line to skip
                split_line = next(f).split()

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


#plotting the the probability of the top particles
def plotPart(part_dict,event):
    #declaring empyty lists
    id = []
    prob = []
        #sorting out the values to see which particle has the most probability
    #sorting a list, because of d.items(), and checkin each and every element
    sorted_dict = sorted(part_dict.items(), key = operator.itemgetter(1))
    #now that everything is sorted splitting up the ID and its probabilty
    for i in range(len(sorted_dict)):
        if sorted_dict[i][1] > 10:
            id.append(sorted_dict[i][0])
            prob.append(sorted_dict[i][1])
    # declaring a linspace of the length of the prob list
    len_prob = np.linspace(1,len(prob),num=len(prob))
    #plotting in bars
    plt.bar(len_prob,prob,color = 'green')
    #adding labels and title
    plt.xlabel('Number of particle in increasing order')
    plt.ylabel('The occurrence a of particle')
    plt.title('Occurrence of particles on average in %d' %event + " event(s)")
    #adding the ID of the current particle to each bar
    for a, b, c in zip(len_prob,prob, id):
        plt.text(a, b, str(c),fontsize = 5.5)
    plt.show()
    # showing the already plotted function
