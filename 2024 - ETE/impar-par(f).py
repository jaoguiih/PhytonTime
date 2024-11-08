def verificar_par_impar_usuario():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
         return f"O número {numero} é: Par"
    else:
         return f"O número {numero} é: Ímpar"

resultado = verificar_par_impar_usuario()
print(resultado)