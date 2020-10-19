import pandas as pd 
from collections import Counter

f = 'excel.xlsx'
file = pd.read_excel(f)
df = pd.DataFrame(file)
df = df[:] # 범위 지정
print()

M_Under_10,M_Under_20, M_Under_30, M_Under_40 , M_other = [],[],[],[],[]
main_list = []
print('일반')
for i in range(1,7):

    lot =  df[i].tolist()
    main_list.extend(lot)
    
#print(main_list)
#print(len(main_list))

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


bonus_list = df["보너스"].tolist()                                  #모든 보너스
Under_10,Under_20, Under_30, Under_40 , other = [],[],[],[],[]

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

#print(len(Under_10),len(Under_20), len(Under_30), len(Under_40) , len(other))

zz = [Under_10,Under_20, Under_30, Under_40 , other]
print('\nBonus ')
for z in zz:
    print(Counter(z))
    #print('hi')
##########################################################




all_Under_10 = M_Under_10 + Under_10

all_Under_20 = M_Under_20 + Under_20

all_Under_30 = M_Under_30 + Under_30

all_Under_40 = M_Under_40 + Under_40

all_other = M_other + other


all = [ all_Under_10, all_Under_20, all_Under_30,all_Under_40 , all_other]
print('\n All ')
for z in all:
    print(Counter(z))
    #print('hi')

all_of_all = all_Under_10 + all_Under_20+ all_Under_30 + all_Under_40 + all_other
print('\n 총 횟수 ', Counter(all_of_all))
#######################################
