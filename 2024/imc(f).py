def calcular_imc():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    imc = peso / (altura ** 2)
    return imc

resultado_imc = calcular_imc()
print(f"O seu IMC é: {resultado_imc}")