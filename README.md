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


### 4. Rodando o Projeto

Após a instalação, inclua um comando para que a pessoa possa ver o projeto funcionando:


#### ▶️ Rodando o Servidor de Desenvolvimento

Com o ambiente virtual ativo, execute o seguinte comando para iniciar o servidor:

```bash
python manage.py runserver
```

Agora, abra seu navegador e acesse `http://127.0.0.1:8000/`.
