import streamlit as st
import pandas as pd
name_1 = st.text_input("Name 1:- ")
date_1 = st.text_input("Date of birth 1:- ")
name_2 = st.text_input("Name 2:- ")
date_2 = st.text_input("Date of birth 2:- ")
compat_dict = {"A" : {1 : [4, 5, 7], 2 : [4, 6, 22], 3 : [3, 6, 8, 9], 4 : [1, 2, 7, 8], 5 : [1], 6 : [2, 3, 6, 9], 7 : [1, 4, 22], 8 : [4, 22], 9 : [3, 6, 9], 11 : [22], 22 : [2, 7, 8, 11]},
              "B" : {1 : [1, 8], 2 : [2, 3, 7, 9, 11], 3 : [2, 22], 4 : [4, 6, 22], 5 : [5, 9, 11], 6 : [4, 11], 7 : [2, 7, 11], 8 : [1, 11], 9 : [2, 5, 7, 11, 22], 11 : [2, 5, 6, 7, 8, 9, 11], 22 : [3, 4, 9, 22]},
              "C" : {1 : [2, 6, 22], 2 : [1, 5], 3 : [4, 5, 7, 11], 4 : [3, 11], 5 : [2, 3, 4, 6, 7, 22], 6 : [1, 5, 7, 8], 7 : [3, 5, 6, 9], 8 : [3, 6, 8, 9], 9 : [4, 8], 11 : [3, 4], 22 : [1, 5]},
              "D" : {1 : [3, 9, 11], 2 : [8], 3 : [1], 4 : [5, 9], 5 : [8], 6 : [22], 7 : [8], 8 : [2, 5, 7], 9 : [1], 11 : [1], 22 : [6]}}
def compatability(x, y):
    if y in compat_dict["A"][x]:
        return "A"
    elif y in compat_dict["B"][x]:
        return "B"
    elif y in compat_dict["C"][x]:
        return "C"
    elif y in compat_dict["D"][x]:
        return "D"
def life_pn_func(date_1):
    date_1 = "-".join((date_1.split("/"))[::-1])
    life_pn = sum([int(j) for j in (date_1.split(' '))[0].split('-')])
    while life_pn >= 10:
        life_pn = sum([int(k) for k in str(life_pn)])
    date = date_1.split(' ')[0].split('-')
    if life_pn == 2 or life_pn == 4:
        date = sum([int(i) for i in date])
        date = sum([int(i) for i in str(date)])
        if date in [2, 4, 11, 22]:
            life_pn = date
    return life_pn
def lo_shu(date):
    date = ''.join(date.split("/"))
    date = [int(i) for i in date]
    list_1 = []
    for i in range(1, 10):
        count = 0
        for j in date:
            if j == i:
                count += 1
        list_1.append(count)
    output = [str(i) * list_1[i - 1] for i in range(1, 10)]
    return output
x = life_pn_func(date_1)
y = life_pn_func(date_2)
compat = compatability(x, y)
st.title(f"COMPATABILITY : {compat}")
st.title(f"LO SHU grid for {name_1}")
a = lo_shu(date_1)
df_1 = pd.DataFrame({" " : ["Mental Level", "Emotional Level", "Practical Level"], "Thought Level" : [a[2], a[1], a[0]], "Will Power and Determination Level" : [a[5], a[4], a[3]], "Action Level" : [a[8], a[7], a[6]]})
st.table(df_1)
st.title(f"LO SHU grid for {name_2}")
a = lo_shu(date_2)
df_2 = pd.DataFrame({" " : ["Mental Level", "Emotional Level", "Practical Level"], "Thought Level" : [a[2], a[1], a[0]], "Will Power and Determination Level" : [a[5], a[4], a[3]], "Action Level" : [a[8], a[7], a[6]]})
st.table(df_2)
