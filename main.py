from processes import *

#----------MAIN ---------

event, ID_dict,ID_list, X_list, Y_list, Z_list, NRG_list = countElem2Dict("AuAu_1000_b_09_10.txt")
average = avPart(event,ID_dict)
mass = get_Mass(ID_list,average,X_list, Y_list, Z_list, NRG_list,event)
plotPart(ID_dict,average,event,10)
plotPart(ID_dict,mass,event,0)
