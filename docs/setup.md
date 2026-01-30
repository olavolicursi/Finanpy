# Instalação e Configuração

Guia para configurar o ambiente de desenvolvimento do Finanpy.

## Pré-requisitos

- **Python** 3.12 ou superior
- **Git**

## Passo a Passo

1. **Clone o repositório**

    ```bash
    git clone https://github.com/olavolicursi/Finanpy.git
    cd Finanpy
    ```

2. **Crie e ative um ambiente virtual**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o Banco de Dados**

    Execute as migrações para criar as tabelas no banco de dados SQLite:

    ```bash
    python manage.py migrate
    ```

5. **Crie um Superusuário (Opcional)**

    Para acessar o painel administrativo do Django:

    ```bash
    python manage.py createsuperuser
    ```

6. **Execute o Servidor de Desenvolvimento**

    ```bash
    python manage.py runserver
    ```

    O projeto estará acessível em `http://127.0.0.1:8000/`.
