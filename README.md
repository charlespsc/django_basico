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