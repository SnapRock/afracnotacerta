import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit

class NcmApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Obter NCM V.1.0")
        self.resize(500, 400)

        # Widgets
        self.descricao_label = QLabel("Descrição do Produto:")
        self.descricao_edit = QLineEdit()
        self.obter_ncm_button = QPushButton("Obter NCM")
        self.resultados_text = QTextEdit()

        # Layouts
        descricao_layout = QHBoxLayout()
        descricao_layout.addWidget(self.descricao_label)
        descricao_layout.addWidget(self.descricao_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.obter_ncm_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(descricao_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.resultados_text)

        self.setLayout(main_layout)

        # Conexões de Sinais e Slots
        self.obter_ncm_button.clicked.connect(self.obter_ncm)

    def obter_ncm(self):
        descricao = self.descricao_edit.text()
        url = "https://afrac-ncm-demo.hf.space/api/predict"
        payload = json.dumps({
            "data": [descricao]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            data = response.json()
            result = data['data'][0]

            ncm_principal = result['label']
            confidences = result['confidences']

            self.resultados_text.clear()
            self.resultados_text.append("NCM Principal:")
            self.resultados_text.append(f"NCM: {ncm_principal}")

        
            self.resultados_text.append("Percentual de Confiança: {:.2f} %".format(float(confidences[0]['confidence']) * 100))
            #Descrição do NCM Principal.
            self.resultados_text.append(f"Descrição: {data['data'][1]}")


            self.resultados_text.append("\nOutros NCMs:")
            for ncm in confidences[1:]:
                self.resultados_text.append(f"NCM: {ncm['label']}")
                self.resultados_text.append(f"Percentual de Confiança: {float(ncm['confidence']) * 100:.2f} %")
                
        else:
            self.resultados_text.clear()
            self.resultados_text.append("Erro ao fazer a solicitação.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ncm_app = NcmApp()
    ncm_app.show()
    sys.exit(app.exec_())