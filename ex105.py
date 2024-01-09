def notas(* a , sit=False):
    dic = dict()
    dic['total'] = len(a)
    dic['maior'] = max(a)
    dic['menor'] = min(a)
    soma = sum(a)
    dic['média'] = soma / len(a)
    if sit==True:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        if 5 <= dic['média'] < 7:
            dic['situação'] = 'REGULAR'
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
    return dic
    


print(notas(3 , 10 , 9))

