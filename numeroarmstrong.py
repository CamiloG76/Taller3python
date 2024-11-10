def numArmstrong(n):
    acum = 0
    for i in range(len(n)):
        acum = acum + (int(n[i]) ** len(n))
        print(acum)
    if acum==int(n):
        return True
    else: 
        return False
print(numArmstrong('22'))


   
