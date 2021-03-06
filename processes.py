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
AuAu_list = []
#---------PROCESSES ---------
#defining an element counter, and the column number

def countElem2Dict(file):
    #declaring variables which will be used to store info
    holding_dict_id = {}
    holding_list_x = []
    holding_list_y = []
    holding_list_z = []
    holding_list_nrg = []
    holding_list_id = []
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
            #the current column's item is what we are looking for
            particle = int(split_line[1])
            mom_x = float(split_line[4])
            mom_y = float(split_line[5])
            mom_z = float(split_line[6])
            energy = float(split_line[7])
            #if its not in the dict yet
            #set its value to 1
            if particle not in holding_dict_id:
                holding_dict_id[particle] = 1
            #else, increase its value by one
            else:
                holding_dict_id[particle] += 1
            #appending each element to each list
            holding_list_id.append(particle)
            holding_list_x.append(mom_x)
            holding_list_y.append(mom_y)
            holding_list_z.append(mom_z)
            holding_list_nrg.append(energy)
    #returning the event number, particle id, energy,px,py and pz
    return event,holding_dict_id,holding_list_id,holding_list_x,holding_list_y,holding_list_z,holding_list_nrg



#average item per event
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
def plotPart(id_dict,part_dict,event,floor):
    #declaring empyty lists
    part_key = []
    part_val = []
    #the floor is where we are looking
    #for example, a mass value is unlikely to be above
    #1, if more methods are added, this can be splitted too
    if floor > 8:
        # sorting out the values to see which particle has the most probability
        # sorting a list, because of d.items(), and checkin each and every element
        sorted_dict = sorted(part_dict.items(), key=operator.itemgetter(1))
        # now that everything is sorted splitting up the ID and its probabilty
        for i in range(len(sorted_dict)):
            if sorted_dict[i][1] > floor:
                part_key.append(sorted_dict[i][0])
                part_val.append(sorted_dict[i][1])
        # declaring a linspace of the length of the prob list
        len_prob = np.linspace(1, len(part_val), num=len(part_val))
        # plotting in bars
        plt.bar(len_prob, part_val, color='green')
        # adding labels and title
        plt.xlabel('Number of particle in increasing order')
        plt.ylabel('The occurrence of particle')
        plt.title('Occurrence of particles on average in %d' %event + " event(s)")
        for a, b, c in zip(len_prob, part_val, part_key):
            plt.text(a, b, str(c), fontsize=10)
        plt.show()
        # showing the already plotted function
    else:
        # sorting out the values to see which particle has the most probability
        # sorting a list, because of d.items(), and checkin each and every element
        sorted_dict = sorted(part_dict.items(), key=operator.itemgetter(1))
        # now that everything is sorted splitting up the ID and its probabilty
        for i in range(len(sorted_dict)):
            if sorted_dict[i][0] > floor:
                part_key.append(sorted_dict[i][0])
                part_val.append(sorted_dict[i][1])
        plt.plot(part_key,part_val,'g*',markersize=12)
        plt.ylabel('The average occurence of a particle')
        plt.xlabel('The average mass of a particle')
        plt.title('The average mass of particles in %d' %event + " event(s)")
        #adding the ID of the current particle to each bar
        '''for a, b, c in zip(part_key,part_val, id_dict.keys()):
            plt.text(a, b, str(c),fontsize = 10)
        '''
        plt.yscale('log')
        plt.show()
        # showing the already plotted function

#getting the mass of a particle
def get_Mass(id,id_dict,px,py,pz,energy,event):
    #holding list for mass this will be returned
    massList = []
    temp_dict = {}
    id_mass_dict = {}
    #looping thru the length of a list
    #it doesnt matter which one because
    #they containing the same amount of elements
    for i in range(len(px)):
        #getting mass of a particle is
        #(m=sqrt(E^2-px^2-py^2-pz^2))
        try:
            #sometimes here a problem occurs that
            #we get negative square root but when recalculated
            #even though it is not true
            mass = (energy[i]**2-px[i]**2-py[i]**2-pz[i]**2)**0.5
            massList.append(mass)
            nrg = energy[i]
            x = px[i]
            y = py[i]
            z = pz[i]
        except ValueError:
            #checking if the problem above occured is true or not
            if mass == (nrg**2-x**2-y**2-z**2)**0.5:
                temp_dict[id[i]] = mass
            else:
                print('Error 2')
        #after we add every mass to each particle
        if id[i] not in temp_dict:
            temp_dict[id[i]] = mass
        else:
            temp_dict[id[i]] += mass
    #when every mass is added, we divide the the amount of mass by the
    #above calculated occurrence
    for n in temp_dict:
        average_mass = temp_dict.get(n) / id_dict.get(n)
        temp_dict[n] = average_mass
    #using the above declared average calculator
    temp_dict = avPart(event,temp_dict)
    #adding a new dict, key will be its occurence and value will be its average mass per event
    for i in temp_dict:
        if i not in id_mass_dict:
            #getting the occurence of the current particle
            #it will be key, and the value will be the average mass
            id_mass_dict[temp_dict.get(i)] = id_dict.get(i)
        else:
            print(' Error 3')
    return id_mass_dict