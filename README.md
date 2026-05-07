
# Fast Car API 🚗

Uma API simples de gerenciamento de carros construída com **FastAPI** e **SQLAlchemy**.

---

## 📋 Descrição do Projeto

A **Fast Car API** permite realizar operações CRUD (Create, Read, Update, Delete) sobre um cadastro de carros.

Tecnologias usadas:

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Alembic
- Ruff (linter/formatter)
- MkDocs (documentação)

---

## 📦 Estrutura do Projeto

```
docs/
├── index.md
fast_car_api/
├── app.py
├── database.py
├── models.py
├── routers.py
├── schemas.py
migrations/
.gitignore
alembic.ini
mkdocs.yml
pyproject.toml
README.md
requirements.txt
```

---

## ▶️ Como rodar o projeto

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

---

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 3. Rodar as migrações do banco de dados (Alembic)

```bash
alembic upgrade head
alembic revision --autogenerate -m "initial"
```

---

### 4. Rodar o servidor FastAPI

```bash
task run
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🧹 Linters e Formatadores (Ruff)

### Verificar problemas de lint:

```bash
task lint
```

### Corrigir problemas automaticamente:

```bash
task lint_fix
```

### Formatar o código:

```bash
task format
```

---

## 📚 Documentação MkDocs

Para rodar a documentação local:

```bash
task docs
```

Acesse:

```
http://127.0.0.1:8001
```

---

## 🛠️ Endpoints disponíveis

| Método   | Rota                     | Descrição              |
|--------- |------------------------- |---------------------- |
| POST     | `/api/v1/cars/`          | Criar um carro        |
| GET      | `/api/v1/cars/`          | Listar todos os carros|
| GET      | `/api/v1/cars/{car_id}`  | Buscar carro por ID   |
| PUT      | `/api/v1/cars/{car_id}`  | Atualizar (replace)   |
| PATCH    | `/api/v1/cars/{car_id}`  | Atualizar (parcial)   |
| DELETE   | `/api/v1/cars/{car_id}`  | Deletar um carro      |

---

## 👤 Autor

**Manoel Cândido**

[manoelcandidodev@gmail.com](mailto:manoelcandidodev@gmail.com)