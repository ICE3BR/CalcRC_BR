import requests
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Cria os widgets da interface
        self.label_produto = QLabel('Valor do produto (em real):')
        self.edit_produto = QLineEdit()
        self.label_frete = QLabel('Valor do frete (em real):')
        self.edit_frete = QLineEdit()
        self.button_calcular = QPushButton('Calcular')
        self.label_resultado = QLabel()

        # Conecta o botão "Calcular" ao método de cálculo
        self.button_calcular.clicked.connect(self.calcular)

        # Cria o layout da interface
        layout = QVBoxLayout()
        layout.addWidget(self.label_produto)
        layout.addWidget(self.edit_produto)
        layout.addWidget(self.label_frete)
        layout.addWidget(self.edit_frete)
        layout.addWidget(self.button_calcular)
        layout.addWidget(self.label_resultado)
        self.setLayout(layout)

    def calcular(self):
        # Lê os valores dos campos de entrada
        produto = float(self.edit_produto.text())
        frete = float(self.edit_frete.text())

        # Calcula os valores
        vp = produto + frete
        vpdolar = vp / dolar
        if vpdolar > 50:
            taxa1 = round((vp*0.6)+vp,2)
            taxa2 = taxa1*0.17
            resultado1 = taxa2+taxa1
        else:
            taxa2 = vp*0.17
            resultado1 = taxa2

        resultado = round(resultado1,2)
        resultadodolar = resultado / dolar
        valortotal = vp + resultado

        # Atualiza o texto do resultado na interface
        self.label_resultado.setText('Seu produto com o frete custa: R${:.2f} ou ${:.2f} Dolar\n'
                                      'Sua compra vai ser taxada em: R${:.2f}\n'
                                      'Convertendo a taxa para Dólar: ${:.2f}\n'
                                      'Então no total com a taxa sua compra vai sair: R${:.2f}\n'
                                      'Dolar hoje: ${:.2f}'.format(vp, vpdolar, resultado, resultadodolar, valortotal, dolar))

if __name__ == '__main__':
    # Faz a requisição HTTP para a API do Banco Central do Brasil
    response = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json')

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Extrai o valor do dólar da resposta
        dados = response.json()
        dolar = float(dados[0]['valor'])
    else:
        print('Falha ao obter o valor do dólar')

    # Cria a aplicação e a janela principal
    app = QApplication(sys.argv)
    window = MainWindow()

    # Exibe a janela principal e inicia a aplicação
    window.show()
    sys.exit(app.exec_())
