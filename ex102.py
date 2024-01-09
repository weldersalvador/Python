def fatorial(a , show=False):
    f = 1
    for count in range(a , 0 , -1):
        f *= count
        if show==True:
            print(count , end=' ')
            if count > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    return(f)
    

print(fatorial(5 , show=True))
