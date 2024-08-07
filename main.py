from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()



comodo=Comodo(
    input("Qual  a largura do cômodo? "),
    input("Qual  a profundidade do cômodo? "))
    


print('a area das paredes é: ', 
      calc.calcular_area_paredes(
        comodo)
        )

print('a area do teto é: ',
      calc.calcular_area_teto(comodo)
        )

print('a litragem necessária é: ',
    calc.calcular_litragem_necessaria()
        )



