import random
import string

def pergunta_tamanho():
    while True:    
        try:
            tamanho = int(input('quantos caracteres sua senha terá:'))
            if tamanho < 8:
                print("uma senha com menos de 8 caracteres não é tão segura, digite pelo menos 8")
                
            
            elif tamanho > 12:
                print('essa senha está grande demais')
                
            
            else:
                print('muito bem, vamos continuar.')
                return tamanho
        
        except ValueError:
            print('você não digitou um número, tente novamente')
tamanho = pergunta_tamanho()

def pergunta_sim_nao(pergunta, dica=None):
    while True:
        resposta = input(pergunta).lower().strip()
        if resposta in ('sim', 'ss', 's'):
            return True

        elif resposta in ('não', 'nao', 'nn', 'n'):
                   
            if dica:
                print(dica)
                return False
        else:
            print('você não digitou uma das opcões, digite apenas com sim ou não')
            continue
tem_letras = pergunta_sim_nao('Sua senha terá letras? responda apenas com sim ou não:', 'uma senha com letras é mais segura, mas vamos continuar.')
tem_numeros = pergunta_sim_nao('Sua senha terá números? novamente, apenas responda com sim ou não:', 'uma senha com números é mais segura, mas vamos continuar.')
tem_simbolos = pergunta_sim_nao('Sua senha terá símbolos, pela última vez, responda com sim ou não:', 'uma senha com símbolos é mais segura, mas vamos continuar')

def criar_senha(tamanho, letras, numeros, simbolos):
    caracteres = ""
    if letras:
        caracteres += string.ascii_letters

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        print('Escolha pelo menos um tipo de caractere')
        return None
    
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

senha = criar_senha(tamanho, tem_letras, tem_numeros, tem_simbolos)
if senha:
    print('Sua senha aleatória é:')
    print(senha)

if __name__ == '__main__':
    tamanho = pergunta_tamanho()

    tem_letras = pergunta_sim_nao('Sua senha terá letras? responda apenas com sim ou não:', 'uma senha com letras é mais segura, mas vamos continuar.')
    tem_numeros = pergunta_sim_nao('Sua senha terá números? novamente, apenas responda com sim ou não:', 'uma senha com números é mais segura, mas vamos continuar.')
    tem_simbolos = pergunta_sim_nao('Sua senha terá símbolos, pela última vez, responda com sim ou não:', 'uma senha com símbolos é mais segura, mas vamos continuar')

    senha = criar_senha(tamanho, tem_letras, tem_numeros, tem_simbolos)
    if senha:
        print('Sua senha aleatória é: ')
        print(senha)