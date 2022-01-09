# Desafio Frexco

## Descricao

**Desafio Tech (Automação)**

Construir pelo menos duas APIs utilizando Django:

- Cadastrar usuário, fornecendo o login, senha e data de nascimento
- Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
- Baixar todos os usuários cadastrados em XLSX.
- Nos enviar no formato .zip

## Requisitos

- Python 3
- Pip

## Instalacao

```
pip install -r requirements.txt
```

## Execucao

```
python manage.py makemigrations cadastro
python manage.py migrate cadastro
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
