import random

def lancar_dado():
    return random.randint(1, 6)

def simulador_lancamento():
    print("Simulador de Lançamento de Dados")
    print("===============================")
    try:
        vezes = int(input("Quantas vezes você deseja lançar o dado? "))

        if vezes <= 0:
            print("O número de lançamentos deve ser maior que zero.")
            return

        resultados = []
        for _ in range(vezes):
            resultado = lancar_dado()
            resultados.append(resultado)

        print("\nResultados dos lançamentos:")
        for indice, valor in enumerate(resultados, start=1):
            print(f"Lançamento {indice}: {valor}")

        print("\nResumo dos resultados:")
        for numero in range(1, 7):
            quantidade = resultados.count(numero)
            if quantidade > 0:
                print(f"Face {numero} apareceu {quantidade} vezes.")

    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    simulador_lancamento()
