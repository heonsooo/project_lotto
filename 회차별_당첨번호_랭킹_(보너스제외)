import pandas as pd 
from collections import Counter

f = 'excel.xlsx'
file = pd.read_excel(f)
df = pd.DataFrame(file)
#df = df[:] # 범위 지정
def lotto(df):
    main_Under_10, main_Under_20, main_Under_30, main_Under_40 , main_other = [],[],[],[],[]
    main_list = []
    print(df)

    for i in range(1,7):
        lot =  df[i].tolist()
        main_list.extend(lot)

    for i in main_list :
        if i < 10 : 
            main_Under_10.append(i)
        elif 10<= i < 20 :
            main_Under_20.append(i)
        elif 20 <= i < 30 :
            main_Under_30.append(i)
        elif 30 <= i < 40 :
            main_Under_40.append(i)
        else :
            main_other.append(i)

    Normal_list = [main_Under_10, main_Under_20, main_Under_30, main_Under_40 , main_other]
    Normal_list_print = []
    for j in Normal_list:
        Normal_list_print.append(j)
 
    number_of_lotto = main_Under_10+ main_Under_20+ main_Under_30+ main_Under_40 + main_other
    print('\n 총 횟수 ', Counter(number_of_lotto))
    return print('끝')

a = int(input('회차(시작) :') )
b = int(input('회차(끝)   :'))

aa = len(df) - a 
bb = len(df) - b
df = df[aa : bb]
lotto(df)
