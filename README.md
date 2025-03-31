# Healthcare Operators API

API desenvolvida com FastAPI com rota para busca de operadoras de plano de saúde. A base de dados utilizada é publica e forncecida pela Agência Nacional de Saúde Suplementar (https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

## Funcionalidades

- Importação de dados de operadoras de saúde a partir de um arquivo CSV.
- Exposição de endpoints para consulta de dados.
- Filtros para refinação da busca

---

## Requisitos

- Python 3.8 ou superior.
- Dependências listadas no arquivo `requirements.txt`.

---

## Execução da API

1. **Crie o ambiente a ative o ambiente virtual python**

   - python3 -m venv venv
   - source venv/bin/activate # Linux/Mac
   - venv\Scripts\activate # Windows

2. **Instale as dependências**

   - pip install -r requirements.txt

3. **Executar servidor com uvicorn**

   - uvicorn src.main:app --reload

---

## Rotas

1. /api/buscar-operadores
   - Aceita parâmetros: busca(string com o termo a ser pesquisado), cnpj, razao_social e numero_ans(booleanos, opções de filtro)

---

## Coleção postman

- O projeto conta com uma coleção do postman contendo 3 requisições de busca utilizando cada filtro. 

---

## Estrutura do projeto

1. src/

   - main.py: Ponto de entrada da aplicação.
   - routes.py: Definição das rotas da API.
   - services.py: Lógica de negócios e manipulação de dados.
   - models.py: Definição dos modelos de dados.
   - db.py: Configuração e conexão com o arquivo csv.
   - config.py: Configurações gerais do projeto.

2. data/
   - Relatorio_cadop.csv: Arquivo CSV com os dados das operadoras de saúde.

3. postman/

   - Coleção postman com requisições de busca utilizando as 3 opções de filtro.
