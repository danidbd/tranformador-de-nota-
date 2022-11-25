#progama que tranfere nota numeria para a, b, c, d... 
# 90 para cima == A
# entre 80-89 == B
#entre 70-79 == C
# entre 60-69 == D
# menor de 60==F
nota=int(input("Entre com sua nota : "))
while nota>0:
    if nota >= 90:
        print(" parabens exelente nota : A")

    elif nota>=80 and nota<=89:
        print("parabens bela nota : B")

    elif nota>=70 and nota <=79:
        print("parabens nota ok : C")

    elif nota>=60 and nota<=69:
        print("parabens : D, tu pode ser mais que isso")

    else:
        print("momento não tão bom nota : F, na proxima sera melhor")
    nota2=int(input("Entre com sua nota :"))
    break
