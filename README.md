# Projeto Imobiliária Django

Este é um projeto de aplicação web para uma imobiliária, desenvolvido com o framework Django. Ele serve como um portfólio completo demonstrando habilidades em desenvolvimento back-end e front-end, desde a modelagem de dados até a criação de uma interface de usuário interativa e responsiva.

## Funcionalidades Implementadas

*   **Autenticação de Usuários:** Sistema completo com Cadastro, Login, Logout e Recuperação de Senha por e-mail (simulado no console).
*   **Tipos de Usuário:** Diferenciação entre **Clientes** e **Corretores** com permissões e visualizações específicas.
*   **Gerenciamento de Imóveis (CRUD):**
    *   Visualização pública de imóveis com filtros dinâmicos de busca por localização e tipo.
    *   Página de detalhes para cada imóvel com galeria de fotos interativa (Carousel Bootstrap).
    *   Área restrita para Corretores logados adicionarem e editarem seus próprios imóveis.
*   **Acompanhamento de Obras:** Página exclusiva para usuários logados visualizarem o status e histórico de andamento das obras.
*   **Painel de Administração:** Interface do Django Admin customizada para gerenciamento de todos os dados da aplicação.
*   **Design Responsivo:** Interface estilizada com **Bootstrap 5**, adaptável a desktops, tablets e celulares.

## Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto no seu computador.

### Pré-requisitos

*   Python 3.8+
*   Git

### Passos de Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/jhonnythomaz/projeto-imobiliaria-django.git
    cd projeto-imobiliaria-django
    ```

2.  **Crie e ative um ambiente virtual:**
    *No Windows:*
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todos os pacotes necessários.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    Este comando irá criar o arquivo de banco de dados `db.sqlite3` com todas as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário:**
    Você precisará de um usuário administrador para acessar o painel `/admin` e cadastrar os primeiros dados.
    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções para criar seu usuário.*

6.  **Rode o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Abra seu navegador e acesse `http://127.0.0.1:8000/`.

---
**Desenvolvido por:** Jhonny Thomaz