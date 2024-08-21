import random
import string

def gerar_senha (tamanho):
    caracteres= string.ascii_letters + string.ascii_digits + string.punctuation
    
    senha=''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

def main():
    tamanho=int(input('Digite o tamanho da senha desejada:'))
    
    senha=gerar_senha(tamanho)
    
    print(f'Senha gerada:{senha}.')
    
if __name__ == '__main__':
    main()