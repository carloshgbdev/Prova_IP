# Autor: Carlos Henrique Gonçalves Batista

# Bibliotecas necessárias
import numpy as np
from typing import List

# Essa função calcula a estimativa da distância entre o sonar e o objeto
def calculate__estimate_distance(time: float, speeds: List[float]):
    # Atribui a uma variável o tempo que o som viajou até o objeto
    time = time / 2

    # Realiza o cálculo
    estimate_distance = np.average(speeds) * time

    # Arredonda o resultado para duas casas decimais e retorna
    return np.round(estimate_distance, 2)

def main():
    # Define as constantes do problema
    min_speed = 1450 # m/s
    max_speed = 1570 # m/s
    
    # Pede ao usuário o tempo de retorno do sinal
    time = float(input("Digite o tempo do retorno do sinal em segundos: "))

    # Chama a função que calcula a estimativa da distância entre o sonar e o objeto
    estimate_distance = calculate__estimate_distance(time, [min_speed, max_speed])

    # Imprime a estimativa da distância entre o sonar e o objeto
    print(f"\nA estimativa da distância entre o sonar e o objeto é de {estimate_distance} metros.")

if __name__ == '__main__':
    main()