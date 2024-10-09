Que bom que deu certo! Agora, para criar um README.md mais sofisticado e visualmente atraente, vamos incorporar alguns ícones e emojis para destacar as seções. Abaixo, segue uma versão mais estilizada do README.md:

---

# 🚀 Aplicativo de Consulta de NCM com IA da AFRAC

Este é um aplicativo desktop desenvolvido em **PyQt5** que permite ao usuário consultar o código **NCM** (Nomenclatura Comum do Mercosul) de produtos a partir de uma descrição. Utilizando a ferramenta de **Inteligência Artificial Nota Certa** da AFRAC, o aplicativo retorna o NCM mais relevante, acompanhado de percentuais de confiança.

## 🛠️ Funcionalidades

- 🔍 **Consulta de NCM**: Digite a descrição de um produto para obter seu código NCM utilizando IA.
- 📊 **Percentual de Confiança**: Exibe o código NCM com o nível de confiança da predição.
- 🖥️ **Interface Gráfica Intuitiva**: Desenvolvida em PyQt5, com uma experiência de usuário moderna e acessível.

## ℹ️ O que é NCM?

A **Nomenclatura Comum do Mercosul (NCM)** é um sistema utilizado pelos países do Mercosul para padronizar a classificação de mercadorias. O código NCM é composto por 8 dígitos que descrevem o produto, sendo obrigatório para diversas transações comerciais.

## ⚙️ Instalação

### Pré-requisitos

- 🐍 **Python 3.8+**
- 🌐 Conexão com a internet para acessar a API da Nota Certa.

### Passos de Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/snaprock/ncm-app.git
   cd ncm-app
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python ncm_app.py
   ```

## 🔧 Como Usar

1. ✏️ Digite a descrição do produto no campo correspondente.
2. 🖱️ Clique em **Obter NCM** para realizar a consulta.
3. 📋 O NCM principal e os NCMs alternativos, juntamente com os percentuais de confiança, serão exibidos.

### Exemplo

- **Entrada**: `Smartphone`
- **Saída**:
  ```
  NCM Principal:
  NCM: 85171200
  Percentual de Confiança: 98.54%

  Outros NCMs:
  NCM: 85176299
  Percentual de Confiança: 1.46%
  ```

## 🌐 API Utilizada

O aplicativo utiliza a API da **Nota Certa** da AFRAC para realizar a consulta de NCMs.

- **Endpoint**: `https://afrac-ncm-demo.hf.space/api/predict`
- **Método**: `POST`
- **Formato do Payload**:
  ```json
  {
      "data": ["descrição do produto"]
  }
  ```

- **Resposta**: A API retorna um NCM principal e outros possíveis NCMs com seus respectivos percentuais de confiança.

## 🗂️ Estrutura do Projeto

```bash
ncm-app/
│
├── ncm_app.py          # Script principal com a lógica do aplicativo
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## 🔮 Melhorias Futuras

- 🌐 **Melhorar o tratamento de erros** de conexão com a API.
- 🔗 **Adicionar funcionalidade** para copiar os resultados para a área de transferência.
- 💾 **Salvar histórico** de consultas realizadas.

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.