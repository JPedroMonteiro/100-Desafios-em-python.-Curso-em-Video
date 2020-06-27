reta1 = float(input('comprimento 1: '))
reta2 = float(input('comprimento 2: '))
reta3 = float(input('comprimento 3: '))
if (reta1 < reta2 + reta3) and reta1 > abs(reta2 - reta3):
    if(reta2 < reta1 + reta3) and reta2 > abs(reta1 - reta3):
        if(reta3 < reta1 + reta2) and reta3 > abs(reta1 - reta2):
            print('Pode formar um triangulo')
            print('Esse é um triângulo: ')
            if reta1 == reta2 == reta3:
                print('Equilatero')
            elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
                print('Isósceles')
            else:
                print('Escaleno')