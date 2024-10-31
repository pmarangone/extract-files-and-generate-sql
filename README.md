# API
### Stack: Flask, SQLAlchemy, SQLite, Pandas, Gunicorn

Esta é uma aplicação API Flask que fornece endpoints para recuperar informações sobre diferentes tipos (tipos) de um arquivo CSV.

#### Como configurar o ambiente:
1. Clone o repositório: git clone  
2. Crie um ambiente virtual (opcional, mas recomendado): 
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```
3. Execute o comando `pip install -r requirements.txt`, na root do projeto, para instalar as dependências.

> O arquivo **scripts/filter_by_status_and_generate_sql_table.py** deve ser executado antes de utilizar a API, pois a API depende de arquivos gerados pelo script.


#### Como executar a aplicação:
Se for executar a aplicação em:
- modo de desenvolvimento, execute `flask --app app run`
- modo de produção, execute `gunicorn -w 4 -b 0.0.0.0:5000 app:app`

#### Endpoints disponíveis e exemplos de requisições:
Exemplo de Requisição: `curl -X GET http://localhost:5000/tipo/1`

Resposta
- Sucesso (200): Retorna o nome correspondente ao tipo_id.
- Não Encontrado (404): Retorna "ID não encontrado" se o ID não existir.



