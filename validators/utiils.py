

from functools import reduce

validation_one = [10, 9, 8, 7, 6, 5, 4, 3, 2]
validation_two = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def cpf_validator(cpf:str) -> bool:
    """ """
    cpf_split = cpf.split("-") # remove os 9 digitos do validador [999.999.999, 99]

    validators = [int(number) for number in cpf_split[1]] # pega os validadores do cpf(os fois ultimos numeros)
    cpf_clened = cpf_split[0].replace(".", "")

    numbers = [int(number) for number in cpf_clened]

    val_1 = validation(numbers, validation_one) # função feita pra reduzir um pouco a repetição de código
    val_2 = validation(numbers, validation_two)
    
    return (val_1 == validators[0] and val_2 == validators[1])


def validation(num_list: list, val_list: list) -> int:
    """ função:
    - soma os numeros de cpf com a lista de validação
    - reduz a lista para o somatorio dos numeros
    - divide por 11
    - divide por 11
    - se o resultado for maior que nove o digito é 0
    """
    result  = [num_list[i] * val_list[i] for i in range(0, 9)] # soma as duas listas
    result_sum = reduce(lambda a,b: a+b, result) # reduz a lista para o somatorio dos numeros

    rest = 11 - (result_sum % 11)
    if rest > 9:
        rest = 0
    return rest

