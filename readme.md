### README.md

# Aplicativo de Consulta de NCM com IA da AFRAC

Este é um aplicativo desktop desenvolvido em PyQt5 que permite aos usuários inserir a descrição de um produto e obter o código **NCM** (Nomenclatura Comum do Mercosul) correspondente. O aplicativo faz uso da ferramenta de **Inteligência Artificial Nota Certa** da AFRAC para realizar a consulta e retornar o código NCM mais adequado, juntamente com os níveis de confiança.

## Funcionalidades

- **Entrada de Descrição do Produto**: Permite ao usuário inserir uma descrição do produto para consulta.
- **Consulta de NCM via IA**: O aplicativo se conecta à API da Nota Certa para obter o NCM principal e outros possíveis NCMs relacionados.
- **Exibição do Percentual de Confiança**: Exibe o NCM principal, o percentual de confiança e outros possíveis NCMs.
- **Interface Intuitiva**: Interface gráfica amigável e moderna desenvolvida com PyQt5.

## O que é o NCM?

A **Nomenclatura Comum do Mercosul (NCM)** é um sistema de classificação utilizado para padronizar a identificação de mercadorias nos países do Mercosul. Cada código NCM é composto por 8 dígitos que descrevem a natureza e as características de cada produto.

## Instalação

### Pré-requisitos

- **Python 3.8** ou superior.
- Conexão com a internet para acessar a API da Nota Certa.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/snaprock/ncm-app.git
   cd ncm-app
   ```

2. Instale as dependências necessárias com o `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python ncm_app.py
   ```

## Como Funciona

1. O usuário insere uma descrição do produto no campo apropriado.
2. O aplicativo envia essa descrição para a **API da Nota Certa**, que utiliza IA para prever o NCM mais relevante.
3. A API retorna uma lista de códigos NCM, sendo o principal exibido com seu percentual de confiança.
4. Se disponíveis, outros possíveis NCMs e seus respectivos percentuais de confiança também são mostrados.

## API Utilizada

O aplicativo utiliza o serviço de IA da AFRAC, **Nota Certa**, para realizar a consulta:
- **Endpoint**: `https://afrac-ncm-demo.hf.space/api/predict`
- **Método**: `POST`
- **Payload**: Um objeto JSON com a descrição do produto.
- **Resposta**: Uma lista de previsões de NCM com seus níveis de confiança.

## Exemplo

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

## Estrutura do Projeto

- `ncm_app.py`: Script principal que contém a lógica da aplicação e a interface gráfica.
  
## Melhorias Futuras

- Melhorias no tratamento de erros de conexão com a API.
- Função para copiar os resultados diretamente para a área de transferência.

## Licença

Este projeto está licenciado sob a **Licença MIT**.