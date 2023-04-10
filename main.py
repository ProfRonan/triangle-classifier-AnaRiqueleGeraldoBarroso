a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        print("Equilátero")
    elif a!=b!=c!=a:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é um triângulo")
