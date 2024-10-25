def calcular_imc():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    imc = peso / (altura ** 2)
    return imc

resultado_imc = calcular_imc()
print(f"O seu IMC é: {resultado_imc}")

# def verificar_par_impar_usuario():
#     numero = int(input("Digite um número inteiro: "))
#     if numero % 2 == 0:
#          return f"O número {numero} é: Par"
#     else:
#          return f"O número {numero} é: Ímpar"

# resultado = verificar_par_impar_usuario()
# print(resultado)

# Ctrl + ; = # em toda a linha
# = "anotação"