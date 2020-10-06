# -*- coding: utf-8 -*
import sys

with open('FONTE.mgol') as obj_arquivo:
    arquivo = obj_arquivo.read()
    print(arquivo)

"""#Definição do alfabeto
Onde iremos definir o alfabeto
"""


def busca(lista, chave, valor):
    for item in lista:
        if item[chave] == valor:
            return item
    return False


class AnaLex():
    def letra(caractere):
        return caractere in string.ascii_letters  # Todas as letras maiscúlas e miniscúlas

    def numero(caractere):
        return caractere in string.digits  # É equivalente a “0123456789”

    def exp(caractere):
        return caractere in 'eE'  # Função exponencial

    def caractereValido(caractere):
        return caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.<>=+-*/(),:;#$?_!%&|\\ "

    def ponto(caractere):
        return "." == caractere

    def aspas(caractere):
        return "\"" == caractere

    def underline(caractere):
        return "_" == caractere

    def abreChave(caractere):
        return "{" == caractere

    def fechaChave(caractere):
        return "}" == caractere

    def menor(caractere):
        return "<" == caractere

    def maior(caractere):
        return ">" == caractere

    def igual(caractere):
        return "=" == caractere

    def mais(caractere):
        return "+" == caractere

    def menos(caractere):
        return "-" == caractere

    def multiplicacao(caractere):
        return "*" == caractere

    def divisao(caractere):
        return "/" == caractere

    def abreParenteses(caractere):
        return "(" == caractere

    def fechaParenteses(caractere):
        return ")" == caractere

    def pontoVirgula(caractere):
        return ";" == caractere

    def eof(caractere):
        return "" == caractere

    def tab(caractere):
        return "\t" == caractere

    def salto(caractere):
        return "\n" == caractere

    def espaco(caractere):
        return " " == caractere

    """#Mapa de Caracteres
    ###Reconhecendo caracteres
    #### Dicionário que mapeia cada caractere lido.
    """

    mapaCaracteres = {

        0: letra,
        1: numero,
        2: exp,
        3: caractereValido,
        4: ponto,
        5: aspas,
        6: underline,
        7: abreChave,
        8: fechaChave,
        9: menor,
        10: maior,
        11: igual,
        12: mais,
        13: menos,
        14: multiplicacao,
        15: divisao,
        16: abreParenteses,
        17: fechaParenteses,
        18: pontoVirgula,
        19: eof,
        20: tab,
        21: salto,
        22: espaco

    }

    """#Tabela de transição"""

    tabelaDeTransicoes = (
        (8, 1, None, None, 6, None, 9, None, 12, 15, 16, 17, 17, 17, 17, 18, 19, 20, 11, 0, 0, 0),
        (None, 1, 4, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None),
        (None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None),
        (None, 3, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None),
        (None, 3, None, None, None, None, None, None, None, None, None, 5, None, None, None, None, None, None, None,
         None, None, None),
        (None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None),
        (6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (8, 8, None, None, None, 8, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None),
        (9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, None, 9, 9, 9),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, 13, 13, None, 14, None, None, None, None, None, None,
         None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None,
         None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None),
        (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None)
    )

    estadosFinais = [
        {'estado': 1, 'tipo': 'Num'},
        {'estado': 3, 'tipo': 'Num'},
        {'estado': 7, 'tipo': 'Literal'},
        {'estado': 8, 'tipo': 'id'},
        {'estado': 10, 'tipo': 'Comentário'},
        {'estado': 11, 'tipo': 'EOF'},
        {'estado': 12, 'tipo': 'OPR'},
        {'estado': 13, 'tipo': 'OPR'},
        {'estado': 14, 'tipo': 'OPR'},
        {'estado': 15, 'tipo': 'OPR'},
        {'estado': 16, 'tipo': 'RCB'},
        {'estado': 17, 'tipo': 'OPM'},
        {'estado': 18, 'tipo': 'AB_P'},
        {'estado': 19, 'tipo': 'FC_P'},
        {'estado': 20, 'tipo': 'PT_V'},

    ]

    estadosNaoFinais = [
        {'estado': 0, 'erro': 'Caractere inválido para formação da primeira palavra da linguagem MGOL'},
        {'estado': 2, 'erro': 'Número inválido - ponto não seguido por dígito'},
        {'estado': 4, 'erro': 'Número inválido - exponencial não seguido por sinal ou dígito'},
        {'estado': 5, 'erro': 'Número inválido - exponencial com sinal mas não seguido por dígito'},
        {'estado': 6, 'erro': 'Literal inválido - Sem fechamento com aspas'},
        {'estado': 9, 'erro': 'Comentário  inválido - sem fechamento com chaves'},
    ]


    def verificarEstadoFinal(estadosFinais, estado, estadoAutomato):
        verif = busca(estadosFinais, estado, estadoAutomato)
        if (verif):
            print("é um estado final")
        else:
            print("deu ruim")

    verificarEstadoFinal(estadosFinais, 'estado', 17)

    """#Função de busca geral
    ##Essa função foi feita pela necessidade, constante, de fazer busca.
    """

    resultado = busca(estadosFinais, 'estado', 11)
    print(resultado)

    """#Tabela de Símbolos"""

    tabelaDeSimbolos = [
        {'token': 'inicio', 'lexema': 'inicio', 'tipo': ''},
        {'token': 'varinicio', 'lexema': 'varinicio', 'tipo': ''},
        {'token': 'varfim', 'lexema': 'varfim', 'tipo': ''},
        {'token': 'escreva', 'lexema': 'escreva', 'tipo': ''},
        {'token': 'leia', 'lexema': 'leia', 'tipo': ''},
        {'token': 'se', 'lexema': 'se', 'tipo': ''},
        {'token': 'entao', 'lexema': 'entao', 'tipo': ''},
        {'token': 'senao', 'lexema': 'senao', 'tipo': ''},
        {'token': 'fimse', 'lexema': 'fimse', 'tipo': ''},
        {'token': 'fim', 'lexema': 'fim', 'tipo': ''},
        {'token': 'literal', 'lexema': 'literal', 'tipo': ''},
        {'token': 'inteiro', 'lexema': 'inteiro', 'tipo': ''},
        {'token': 'real', 'lexema': 'real', 'tipo': ''},
    ]
    palavrasReservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'senao', 'fimse', 'fim',
                          'literal', 'inteiro', 'real']

    def verificarTabelaDeSimbolos(self, token, lexema, tipo=""):

        if ({'token': token, 'lexema': lexema, 'tipo': tipo} not in self.tabelaDeSimbolos and token == 'id'):
            self.tabelaDeSimbolos.append({'token': token, 'lexema': lexema, 'tipo': tipo})
            # print("Não pertence a tabela de simbolos e é um id")
            ''' laço para mostrar a tabela de simbolo
            vamos utilizar para criar a funcao de printar a tabela de simbolos
            for obj in self.tabelaDeSimbolos:
                print(obj)'''
        else:
            print("Já pertence a uma tabela de simbolos")

    def org_estado_final(self, estado):
        final = busca(self.estadosFinais, 'estado', estado)
        if final:
            if self.palavra in self.palavrasReservadas:
                '''self.verificarTabelaDeSimbolos(self.palavra,self.palavra)'''
                print("Já pertence a uma tabela de simbolos")
            else:
                self.verificarTabelaDeSimbolos(final['tipo'], self.palavra)
            self.palavra = ''
            self.estado = 0

            return True
        return False


def main():
    analisadorLex = AnaLex()

    analisadorLex.verificarTabelaDeSimbolos('id', 'ana')


if __name__ == "__main__":
    main()
