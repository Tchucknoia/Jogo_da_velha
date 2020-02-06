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
            pass

    def identificar_fim(self):
        if self._tabela[0] == self._tabela[4] == self._tabela[8]:
            self._fim = True

    def imprimir_tabela(self):
        text = f'{self._tabela[0]}|{self._tabela[1]}|{self._tabela[2]}\n' \
               f'{self._tabela[3]}|{self._tabela[4]}|{self._tabela[5]}\n' \
               f'{self._tabela[6]}|{self._tabela[7]}|{self._tabela[8]}\n'
        print(text)
        pass

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