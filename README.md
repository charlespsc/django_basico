# Projeto Django Básico

Este é um projeto de estudo para aprender os fundamentos do Django.

**Pré-requisitos:** 

    ✅ Pré-requisitos

    Antes de começar, garanta que você tenha instalado:
    * [Python 3.8+](https://www.python.org/downloads/)
    * [Git](https://git-scm.com/)
    
## 🚀 Começando

Antes de rodar o projeto ou instalar qualquer dependência, o passo mais importante é criar um ambiente virtual (`venv`). Isso garante que as bibliotecas do projeto fiquem isoladas do seu sistema operacional.


### 1. Crie o Ambiente Virtual

Com o projeto aberto no VS Code, abra o terminal integrado e execute o seguinte comando:

```bash
python -m venv venv
```

### 2. Ativando o Ambiente Virtual

Agora que o ambiente foi criado, precisamos "ativá-lo". A ativação faz com que o seu terminal passe a usar o Python e o `pip` de dentro da pasta `venv`.

#### * No Windows (PowerShell/CMD):

```PowerShell
.\venv\Scripts\activate
```

#### * No macOS ou Linux:

```bash
source venv/bin/activate
```

Dica: Após ativar, você verá (venv) no início da linha do seu terminal, indicando que o ambiente está ativo!

### 3. Instalando as Dependências

Com o ambiente ativo, podemos finalmente instalar o Django e outras bibliotecas necessárias. Para isso, use o gerenciador de pacotes `pip`:

```bash
pip install -r requirements.txt
```

Obs.: Se o projeto ainda não tiver um arquivo requirements.txt, você pode começar instalando o Django manualmente:
```bash
pip install django
```

Pronto! Seu ambiente de desenvolvimento está configurado e pronto para começar.

---

## 🚀 Criando seu Primeiro Projeto Django

Com o ambiente virtual (`venv`) criado e ativado, estamos prontos para usar o Django e construir a base do nosso projeto.

Lembre-se: você sabe que o ambiente está ativo quando o nome dele, como (`venv`), aparece no início da linha do seu terminal.

### 1. Criando o Projeto Principal

Agora vamos usar o comando principal do Django para criar toda a estrutura de arquivos e pastas do nosso projeto.

```bash
# Sintaxe: django-admin startproject <nome_do_projeto> .
django-admin startproject setup .
```

Obs.: `setup` é o nome que escolhemos para o nosso diretório de configurações principal. Você poderia usar `core`, `config` ou o nome do seu site.

### 2. Aplicando as Migrações Iniciais

O Django já vem com recursos prontos, como sistema de autenticação, sessões, painel de admin, etc. Esses recursos precisam de tabelas no banco de dados. O comando `migrate` cria essas tabelas para nós. Por padrão, o Django usará um banco de dados simples chamado `db.sqlite3`, que será criado automaticamente.

```bash
python manage.py migrate
```

### 3. Rodando o Servidor de Desenvolvimento ▶️ 

Com o ambiente virtual ativo e o projeto `setup` iniciado, execute o seguinte comando para iniciar o servidor:

```bash
python manage.py runserver
```

Agora, abra seu navegador e acesse `http://127.0.0.1:8000/`.

Você deverá ver a página de boas-vindas do Django, com um foguete! 🚀


### 4.(Opcional) Criando um Superusuário

Para acessar o painel administrativo do Django, você precisa de um usuário. Vamos criar um:

```bash
python manage.py createsuperuser
```
---

## 🏗️ Criando sua Primeira Aplicação (App)

No Django, um "projeto" é o contêiner principal para as configurações e aplicações. Uma "aplicação" (ou app) é um módulo que faz algo específico, como um blog, uma enquete, ou um sistema de autenticação. Um projeto pode ser composto por várias aplicações, tornando-o modular e organizado.

Vamos criar nossa primeira aplicação, que chamaremos de `core`.

### 1. Usando o Comando startapp
Certifique-se de que seu ambiente virtual esteja ativo e que você esteja na pasta raiz do projeto (a mesma onde está o arquivo manage.py). Agora, execute o seguinte comando:

```bash
# Sintaxe: python manage.py startapp <nome_da_app>
python manage.py startapp core
```
O Django criará automaticamente uma nova pasta chamada `core` com uma estrutura de arquivos padrão para uma aplicação:

```
Django_basico/
├── venv/
├── core/             <-- Sua nova aplicação!
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py      <-- Para registrar seus modelos no painel Admin
│   ├── apps.py       <-- Configurações da sua aplicação
│   ├── models.py     <-- Onde você define a estrutura do banco de dados
│   ├── tests.py      <-- Para escrever testes para sua aplicação
│   └── views.py      <-- Onde fica a lógica das suas páginas
├── setup/
└── manage.py
```

### 2. Registrando a Nova Aplicação

Agora que a aplicação foi criada, precisamos "avisar" ao projeto principal do Django que ela existe e deve ser utilizada.

Abra o arquivo de configurações principal do seu projeto: `setup/settings.py`.

Procure pela lista chamada `INSTALLED_APPS` e adicione o nome da sua nova aplicação no final.

```
# setup/settings.py

# ... (outras configurações)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Minhas Apps
    'core',  # Adicione o nome da sua app aqui
]

# ... (outras configurações)
```
Por que isso é importante? Registrar a app em INSTALLED_APPS permite que o Django encontre os modelos, URLs, templates e outros componentes da sua aplicação. Sem isso, a aplicação simplesmente não será reconhecida pelo projeto.


### 3. Criando a Primeira View e URL

Agora, vamos fazer algo simples: criar uma página de "Olá, Mundo!" para testar se nossa `app` está funcionando.

#### Passo 1: Crie a View

A view é uma função Python que recebe uma requisição web e retorna uma resposta. Abra o arquivo `core/views.py` e adicione o seguinte código:

```python
# core/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é a página principal da app core.</h1>")
```

#### Passo 2: Configure as URLs da App

Precisamos de um "endereço" (URL) para acessar essa `view`. Crie um novo arquivo chamado `urls.py` dentro da pasta `core`:

```python
# core/urls.py

from django.urls import path
from . import views  # Importa as views da nossa app 'core'

urlpatterns = [
    path('', views.home, name='home'),  # A URL raiz ('') chama a view 'home'
]
```

#### Passo 3: Conecte as URLs da App ao Projeto Principal

Por fim, precisamos dizer ao nosso projeto principal para incluir as URLs da nossa `app`. Abra o arquivo de URLs do projeto: `setup/urls.py` e modifique-o:

```python
# setup/urls.py

from django.contrib import admin
from django.urls import path, include  # Não se esqueça de importar o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui todas as URLs da app 'core'
]
```
O comando `include` funciona como um ponteiro. Ele diz: "Sempre que alguém acessar a URL raiz (`''`) do site, vá procurar por mais instruções no arquivo `core.urls`".


### 4. Testando a Nova Página

Com tudo configurado, inicie o servidor novamente:

```bash
python manage.py runserver
```

Agora, ao acessar http://127.0.0.1:8000/, você não verá mais a página do foguete, mas sim a mensagem que definimos na nossa view: "Olá, Mundo!".

Sucesso! Você criou e integrou sua primeira aplicação ao projeto. Este é o fluxo de trabalho padrão no Django: criar `apps` para cada funcionalidade, definir suas `views` e `URLs`, e conectá-las ao projeto principal.