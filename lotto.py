import numpy as np
import pandas as pd 

f = 'excel.xlsx'
file = pd.read_excel(f)
df = pd.DataFrame(file)
df = df.drop(0)


bonus_list = df["보너스"].tolist()                                  #모든 보너스
Under_10,Under_20, Under_30, Under_40 , other = [],[],[],[],[]
main_list = []
for i in bonus_list :
    if i < 10 : 
        Under_10.append(i)
    elif 10<= i < 20 :
        Under_20.append(i)
    elif 20 <= i < 30 :
        Under_30.append(i)
    elif 30 <= i < 40 :
        Under_40.append(i)
    else :
        other.append(i)

print(len(Under_10),len(Under_20), len(Under_30), len(Under_40) , len(other))

from collections import Counter
zz = [Under_10,Under_20, Under_30, Under_40 , other]
for z in zz:
    #print(Counter(z))
    print('hi')


#######################################
M_Under_10,M_Under_20, M_Under_30, M_Under_40 , M_other = [],[],[],[],[]

for i in range(1,7):

    lot =  df[i].tolist()
    main_list.extend(lot)
    
#print(main_list)
print(len(main_list))

for i in main_list :
    if i < 10 : 
        M_Under_10.append(i)
    elif 10<= i < 20 :
        M_Under_20.append(i)
    elif 20 <= i < 30 :
        M_Under_30.append(i)
    elif 30 <= i < 40 :
        M_Under_40.append(i)
    else :
        M_other.append(i)

zzz = [M_Under_10,M_Under_20, M_Under_30, M_Under_40 , M_other]
for lotto in zzz:
    print(Counter(lotto))
    #print('hi')
