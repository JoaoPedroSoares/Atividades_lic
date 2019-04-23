a1 = float(input('Nota A1'))
a2 = float (input('Nota A2'))
p1 = float(input('Nota P1'))
p2 = float(input('Nota P2'))
                 

def media_final (a1,p1,a2,p2):
    MF = (2*a1 + 4*p1 + 3*a2 + 3*p2) / 12
    if a1 >= 0 < 10 and a2 >= 0 < 10 and p1 >= 0 < 10 and p2 >= 0 < 10:
        print('A1:',a1,'P1:', p1)
        print('A2:',a2, 'P2:',p2)
        print('MF:', MF)


media_final (a1,p1,a2,p2)
