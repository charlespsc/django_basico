# 🐍 Django Básico — Fundamentos de Desenvolvimento Web

Projeto de estudo desenvolvido com **Django** para praticar os fundamentos de uma aplicação web em Python.

O projeto evolui de uma página simples de **"Olá, Mundo!"** para uma aplicação com uma área de **produtos**, incluindo modelagem de dados, migrations, templates, formulários, arquivos estáticos e integração com SQLite.

> Este repositório representa uma etapa prática de aprendizagem dos principais conceitos do framework Django.

---

## 🎯 Objetivo

O objetivo deste projeto é compreender a estrutura fundamental de uma aplicação Django e o fluxo:

```text
Requisição HTTP
      │
      ▼
    URLconf
      │
      ▼
    View
      │
      ├──────────────► Template
      │
      ▼
    Model
      │
      ▼
   SQLite
```

Durante o projeto são praticados conceitos como:

- criação de um projeto Django;
- criação de aplicações (`apps`);
- configuração do `settings.py`;
- roteamento com `urls.py`;
- criação de views;
- utilização de templates;
- arquivos estáticos;
- definição de models;
- migrations;
- operações de persistência;
- formulários HTML;
- proteção CSRF;
- painel administrativo do Django.

---

# 🧰 Tecnologias

| Tecnologia | Utilização |
|---|---|
| **Python** | Linguagem principal |
| **Django 5.2.5** | Framework web |
| **SQLite** | Banco de dados |
| **HTML5** | Estrutura das páginas |
| **CSS3** | Estilização |
| **Git** | Controle de versão |

A versão do Django está indicada no arquivo de configurações gerado pelo projeto:

```text
Django 5.2.5
```

---

# 🏗️ Estrutura do projeto

```text
django_basico/
│
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── produtos/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── ver_produto.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── setup/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── static/
│       └── produtos/
│           ├── css/
│           │   └── estilo.css
│           └── img/
│               └── produto_exemplo.jpeg
│
├── manage.py
├── .gitignore
└── README.md
```

---

# 🧩 Projeto x App no Django

Uma das ideias fundamentais praticadas neste projeto é a diferença entre **projeto** e **aplicação**.

### Projeto

O diretório:

```text
setup/
```

concentra as configurações principais:

- `settings.py`
- `urls.py`
- `asgi.py`
- `wsgi.py`

### Aplicações

O projeto possui duas apps:

```text
core/
produtos/
```

A app `core` apresenta a página inicial.

A app `produtos` concentra a funcionalidade relacionada aos produtos.

Essa separação permite organizar uma aplicação Django em módulos com responsabilidades específicas.

---

# 🏠 Aplicação `core`

A app `core` possui uma view inicial:

```python
def home(request):
    return HttpResponse(
        "<h1>Olá, Mundo! Esta é a página principal da app core.</h1>"
    )
```

A rota está configurada em:

```text
core/urls.py
```

```text
GET /
```

Ao acessar:

```text
http://127.0.0.1:8000/
```

a requisição é direcionada para a view `home`.

---

# 📦 Aplicação `produtos`

A app `produtos` representa a primeira funcionalidade baseada em banco de dados.

Ela possui:

- model `Produto`;
- views;
- URLs;
- template HTML;
- arquivos CSS;
- imagem estática;
- migration;
- registro no Django Admin.

---

# 🗃️ Model `Produto`

O modelo é definido em:

```text
produtos/models.py
```

Estrutura:

```text
Produto
├── id
├── nome
├── preco
├── descricao
└── estoque
```

Correspondência dos campos:

| Campo | Tipo | Configuração |
|---|---|---|
| `id` | BigAutoField | Chave primária automática |
| `nome` | CharField | máximo de 100 caracteres |
| `preco` | DecimalField | 10 dígitos / 2 casas |
| `descricao` | TextField | opcional |
| `estoque` | IntegerField | padrão `0` |

O model também define:

```python
ordering = ['nome']
```

Portanto, a ordenação padrão dos produtos é pelo nome.

---

# 🗄️ Banco de dados

O projeto utiliza o banco padrão:

```text
SQLite
```

Configuração atual:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

O arquivo `db.sqlite3` é criado na raiz do projeto após a execução das migrations.

---

# 🔄 Migrations

O projeto possui uma migration inicial:

```text
produtos/migrations/0001_initial.py
```

Ela cria a tabela correspondente ao model `Produto`.

Para aplicar as migrations:

```bash
python manage.py migrate
```

Para criar novas migrations depois de alterar um model:

```bash
python manage.py makemigrations
```

E depois:

```bash
python manage.py migrate
```

---

# 🌐 URLs

O projeto principal possui o seguinte roteamento:

```text
setup/urls.py
```

```text
/admin/
    └── Django Admin

/
    └── core.urls

/produtos/
    └── produtos.urls
```

A app `produtos` disponibiliza:

| Método | URL | Função |
|---|---|---|
| `GET` | `/produtos/ver_produto/` | Exibe a página de produto |
| `POST` | `/produtos/ver_produto/` | Cadastra um produto |
| `GET` | `/produtos/inserir_produto/` | Exibe página de inserção |

---

# 📝 Cadastro de produtos

A view `ver_produto` trabalha com dois métodos HTTP.

### GET

Quando recebe:

```http
GET /produtos/ver_produto/
```

a aplicação renderiza:

```text
ver_produto.html
```

e apresenta a interface do produto.

### POST

Quando o formulário é enviado:

```http
POST /produtos/ver_produto/
```

a view recupera:

```text
nome
preco
descricao
estoque
```

cria uma instância de:

```python
Produto(...)
```

e salva o registro:

```python
produto.save()
```

---

# 🔐 Proteção CSRF

O formulário utiliza o mecanismo de proteção CSRF do Django:

```django
{% csrf_token %}
```

Esse recurso é importante para proteger requisições de alteração enviadas através de formulários.

---

# 🎨 Templates e arquivos estáticos

O projeto utiliza um template:

```text
produtos/templates/ver_produto.html
```

O template utiliza:

```django
{% load static %}
```

para carregar os arquivos estáticos.

CSS:

```text
templates/static/produtos/css/estilo.css
```

Imagem:

```text
templates/static/produtos/img/produto_exemplo.jpeg
```

A configuração de arquivos estáticos está no:

```text
setup/settings.py
```

---

# 🛠️ Django Admin

O model `Produto` está registrado no painel administrativo:

```python
admin.site.register(Produto)
```

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Depois de iniciar o servidor:

```bash
python manage.py runserver
```

acesse:

```text
http://127.0.0.1:8000/admin/
```

---

# ▶️ Executando o projeto

## 1. Pré-requisitos

É necessário possuir:

- Python 3.8 ou superior;
- Git.

A versão do Python utilizada pelo projeto deve ser compatível com o Django instalado.

---

## 2. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/django_basico.git
```

Entrar na pasta:

```bash
cd django_basico
```

---

## 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### Windows

PowerShell:

```powershell
.\venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal normalmente exibirá:

```text
(venv)
```

---

# 📦 Instalação do Django

O repositório atual **não possui um `requirements.txt`**.

Por isso, em um ambiente novo, instale o Django:

```bash
pip install django
```

Para conferir:

```bash
python -m django --version
```

O projeto foi desenvolvido com:

```text
Django 5.2.5
```

---

# 🗄️ Aplicar as migrations

Com o ambiente virtual ativo:

```bash
python manage.py migrate
```

Isso cria as tabelas necessárias no SQLite, incluindo a estrutura do model `Produto`.

---

# ▶️ Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

# 🔗 Principais páginas

### Página inicial

```text
http://127.0.0.1:8000/
```

### Visualização / cadastro de produto

```text
http://127.0.0.1:8000/produtos/ver_produto/
```

### Inserção de produto

```text
http://127.0.0.1:8000/produtos/inserir_produto/
```

### Django Admin

```text
http://127.0.0.1:8000/admin/
```

---

# 🧪 Testes

As apps possuem arquivos preparados para testes:

```text
core/tests.py
produtos/tests.py
```

No estado atual do projeto, esses arquivos ainda contêm apenas a estrutura inicial criada pelo Django.

Para executar a suíte de testes:

```bash
python manage.py test
```

A próxima evolução natural seria criar testes para:

- acesso às URLs;
- resposta das views;
- criação de produtos;
- validação dos campos;
- persistência no banco;
- acesso ao Django Admin.

---

# 🔄 Fluxo da aplicação

Um exemplo do cadastro de produto:

```text
Usuário
   │
   │ POST
   ▼
URL /produtos/ver_produto/
   │
   ▼
View ver_produto()
   │
   ▼
Produto(...)
   │
   ▼
produto.save()
   │
   ▼
SQLite
   │
   ▼
HttpResponse
```

Esse fluxo demonstra uma das ideias fundamentais do Django:

```text
URL → View → Model → Banco
       │
       ▼
    Template
```

---

# 📚 Conceitos praticados

Este projeto permite praticar:

- Python;
- Django;
- arquitetura MVT;
- projetos e apps;
- URLs;
- views;
- models;
- migrations;
- ORM;
- SQLite;
- templates;
- arquivos estáticos;
- formulários HTML;
- CSRF;
- Django Admin;
- ambientes virtuais;
- testes automatizados.

---

# 🎓 Contexto de aprendizagem

Este projeto representa uma etapa introdutória de desenvolvimento web com Django.

A evolução pode ser entendida em etapas:

```text
Django
  │
  ├── Projeto
  │
  ├── App
  │
  ├── URL
  │
  ├── View
  │
  ├── Template
  │
  ├── Model
  │
  ├── Migration
  │
  └── Banco de Dados
```

A partir dessa base, o projeto pode evoluir para uma aplicação mais completa utilizando autenticação, formulários Django, CRUD completo, APIs REST, testes e banco de dados externo.

---

# 🚧 Próximas melhorias

Algumas evoluções naturais para este projeto:

- [ ] criar `requirements.txt`;
- [ ] mover a `SECRET_KEY` para variável de ambiente;
- [ ] desativar `DEBUG` em ambiente de produção;
- [ ] configurar `ALLOWED_HOSTS`;
- [ ] criar CRUD completo de produtos;
- [ ] utilizar Django Forms;
- [ ] utilizar mensagens do Django;
- [ ] criar páginas de listagem e edição;
- [ ] adicionar validações de formulário;
- [ ] criar testes automatizados;
- [ ] adicionar autenticação;
- [ ] melhorar o Django Admin;
- [ ] utilizar PostgreSQL;
- [ ] criar API REST com Django REST Framework;
- [ ] containerizar a aplicação com Docker;
- [ ] configurar CI com GitHub Actions.

---

# ⚠️ Observações importantes

Este é um **projeto de estudo** e utiliza configurações apropriadas para desenvolvimento local.

O arquivo `setup/settings.py` contém atualmente:

```python
DEBUG = True
```

e uma `SECRET_KEY` diretamente no código.

Essas configurações não devem ser utilizadas dessa forma em produção.

O projeto também não possui atualmente um `requirements.txt`, portanto a instalação das dependências precisa ser feita manualmente ou esse arquivo deve ser criado como uma melhoria futura.

---

## 👨‍💻 Autor

**Charles Pereira**

Tecnologia • Desenvolvimento • Python • Django • Banco de Dados • Infraestrutura • Educação Tecnológica

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório.
