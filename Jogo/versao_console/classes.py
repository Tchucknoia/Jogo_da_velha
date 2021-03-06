import platform


class Velha:
    def __init__(self):
        self._tabela = [_ for _ in range(9)]
        self._vez = True
        self._fim = False
        self._os = platform.system()

    def posicionar_letra(self):
        """
        Função que irá colocar o marcador onde o jogador quer que ele fique posicionado
        :param self: o objeto que corresponde a classe Velha
        :return: Sem retorno
        """
        num = -1
        while not (num in self._tabela):
            num = int(Velha.pegar_letra())
        pos = int(self._tabela.index(num))
        if self._os == 'Linux':
            if self._vez is True:
                self._tabela[pos] = '\033[31m' + 'X' + '\033[0;0m'
            else:
                self._tabela[pos] = '\033[34m' + 'O' + '\033[0;0m'
            self._vez = not self._vez
        elif self._os == 'Windows':
            self._fim = True
            pass

    def vitoria(self):
        self._fim = True
        self._vez = not self._vez
        pass

    def empate(self):
        self._fim = True
        self._vez = 2
        pass

    def identificar_fim(self):
        if self._tabela[0] == self._tabela[4] == self._tabela[8]:
            self.vitoria()
        elif self._tabela[2] == self._tabela[4] == self._tabela[6]:
            self.vitoria()
        elif all(type(x) != int for x in self._tabela):
            self.empate()
        for x in range(0, 9, 3):
            if self._tabela[x] == self._tabela[x + 1] == self._tabela[x + 2]:
                self.vitoria()
                break
        for x in range(3):
            if self._tabela[x] == self._tabela[x + 3] == self._tabela[x + 6]:
                self.vitoria()
                break

    def imprimir_r_b_linux(self, text1, text2):
        if self._vez:
            print('\033[31m' + text1 + '\033[0;0m')
        else:
            print('\033[34m' + text2 + '\033[0;0m')

    def imprimir_tabela(self):
        text = f'{self._tabela[0]}|{self._tabela[1]}|{self._tabela[2]}\n' \
               f'{self._tabela[3]}|{self._tabela[4]}|{self._tabela[5]}\n' \
               f'{self._tabela[6]}|{self._tabela[7]}|{self._tabela[8]}\n'
        print(text)
        if self._vez == 2:
            print("Empate")
            pass
        elif self._fim:
            self.imprimir_r_b_linux('Vermelho ganhou', 'Azul ganhou')
        else:
            self.imprimir_r_b_linux('Vez do vemelho', 'Vez do azul')


    def iniciar(self):
        """
        Função para inciar o jogo e identificar quando ele acaba
        :param self: o objeto que corresponde a classe Velha
        :return: Sem retorno
        """

        while not self._fim:
            self.imprimir_tabela()
            self.posicionar_letra()
            self.identificar_fim()
        self.imprimir_tabela()

    @staticmethod
    def pegar_letra():
        """
        Função para pegar a posição que o jogador quer que o seu marcador fique
        :param self: o objeto que corresponde a classe Velha
        :return: String com a posição desejada
        """

        return input("Digite o número que corresponde a posição desejada:")


if __name__ == '__main__':
    jogo = Velha()
    jogo.iniciar()
