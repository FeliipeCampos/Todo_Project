# API de Lista de Tarefas

Esta é uma API de Lista de Tarefas construída com Django e Django REST framework. Ela permite que os usuários criem, atualizem, deletem e visualizem tarefas.

# Funcionalidades:

	-Criar uma nova tarefa;
				
	-Atualizar uma tarefa existente;
				
	-Deletar uma tarefa;
				
	-Marcar uma tarefa como completa;
				
	-Listar todas as tarefas;
	 

# Requisitos:

	-Python 3.6+
	
	-Django 3.0+
	
	-Django REST framework


# Instalação:

  Clonar o repositório: 

    git clone https://github.com/](https://github.com/FeliipeCampos/Todo_Project

    cd todo_project

  Criar e ativar um ambiente virtual:

    python -m venv venv

    source venv/bin/activate  

No Windows use: 

	venv\Scripts\activate


Instalar dependências:

	pip install -r requirements.txt

Aquivo .env:

No diretório "todo_project" que fica dentro do diretório principal, Crie um arquivo chamado ".env", que você pode usar para alterar as variáveis de ambiente, nele cole os seguintes dados:
	
	DEBUG=True
	SECRET_KEY=!-d23yku04yn$q2krxjne4%r61fdt09f@*95q%mas4mv1^(z@!
	DATABASE_URL=sqlite:///db.sqlite3
 



Aplicar migrações:

	python manage.py migrate


Criar um superusuário:

	python manage.py createsuperuser

  (Siga as instruções que vão aparecer no terminal para criar seu usuário admin.)

Rodar o servidor de desenvolvimento:

	python manage.py runserver

A API estará disponível em: http://127.0.0.1:8000, mas você só poderá utilizar usando os endpoints abaixo.

# EndPoints da API:

Listar todas as tasks:

GET: 

	http://127.0.0.1:8000/tasks/ 

Inserir Tasks:

POST: 

	http://127.0.0.1:8000/tasks/ 

Body: Raw:
		      
	{
		"title": "Título da Task",
		"description": "Aqui fica a descrição da task"
	}

Atualiza os dados da task, lembre-se de substituir "ID" pelo ID da task:

Put: 

	http://127.0.0.1:8000/tasks/ID/ 

  Body: Raw:

    {
      "title": "Altere o título aqui",
      "description": "Altere a descrição aqui",
      "completed": false
    }

Deleta um registro de task, lembre-se de substituir o "ID" pelo ID da task:

DELETE: 
	
	http://127.0.0.1:8000/tasks/ID/delete/ 
	 
Atualiza a task para concluida, lembre-se de substituir o "ID" pelo ID da task:

PATCH: 

	http://127.0.0.1:8000/tasks/ID/complete/ 
 
# Métricas:

Para acessar as métricas, use o navegador ou um GET para: 
 
	http://127.0.0.1:8000/metrics.

# Testes:

Para rodar um teste execute o comando:

	python manage.py test
