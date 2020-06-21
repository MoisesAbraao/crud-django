# CRUD Django

Projetinho simples de CRUD usando o Flask.

## Como rodar o Projeto

1. Clone este repositório no terminal
```bash
git clone https://github.com/MoisesAbraao/crud-django.git
```

2. Caso tenha o pipenv, vá para a pasta raiz do projeto start o ambiente virtual e instale as dependências
```bash
pipenv shell
pipenv install
```

3. Ainda no terminal, execute o seguinte comando para criar o banco
```bash
python manage.py migrate
```

4. Ainda no terminal, execute o seguinte comando para criar o usuário adminstrador
```bash
python manage.py createsuperuser
```
5. Execute o seguinte comando para iniciar o servidor
```bash
python manage.py runserver
```

6. Abra o navegador e acesse o sistema 
```bash
localhost:8000
```