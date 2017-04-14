from processes import *

#----------MAIN ---------

event, ID_dict,ID_list, X_list, Y_list, Z_list, NRG_list = countElem2Dict("AuAu_cut.txt")
average = avPart(event,ID_dict)
#plotPart(average,event)
mass = get_Mass(ID_list,X_list, Y_list, Z_list, NRG_list,event)