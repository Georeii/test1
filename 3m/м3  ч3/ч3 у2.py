s = """Было просто пасмурно, дуло с севера 
А к обеду насчитал сто градаций серово. 
Так всегда первого ноль девятого 
То ли весь мир сошол с ума, то ли я - того... 
На столе записка от неё смята 
Недопитый виски допиваю с матами. 
Посмотрю в окно, допишу главу 
Первое сентебря, дворник жжёт листву. 
Если знаешь как жить живи 
Ты хотела плыть как все - так плыви!
"""

s_list = s.split(' ')
list = []
for i in s_list:
    if len(i) >= 5:
        list.append(i)
print(list)


