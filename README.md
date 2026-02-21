# Finanpy

Sistema de Gestão de Finanças Pessoais desenvolvido em Python com Django. Permite controlar contas bancárias, categorizar transações (receitas e despesas) e visualizar um dashboard com resumo das finanças.

## Descrição do projeto

O **Finanpy** é uma aplicação web monolítica construída com Django e estilizada com TailwindCSS. Principais características:

- **Autenticação por e-mail**: login usando e-mail no lugar de nome de usuário
- **Gestão de contas bancárias**: cadastro e controle de múltiplas contas (corrente, poupança, investimento, etc.)
- **Categorização de transações**: organização de receitas e despesas por categorias
- **Dashboard financeiro**: saldo total, receitas e despesas do mês, últimas transações e saldos por conta
- **Interface moderna**: tema escuro, design responsivo e gradientes

A aplicação segue arquitetura Django full-stack com templates (DTL), SQLite em desenvolvimento e modelo de usuário customizado.

## Requisitos de sistema

- **Python**: 3.12 ou superior
- **Node.js**: necessário para build do TailwindCSS (gerar `static/css/output.css`)
- **Sistema operacional**: Windows, Linux ou macOS

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/<seu-usuario>/Finanpy.git
cd Finanpy
```

### 2. Criar ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

```bash
python manage.py migrate
```

### 5. (Opcional) Criar superusuário

```bash
python manage.py createsuperuser
```

Use o e-mail como identificador de login.

### 6. Build do TailwindCSS (CSS)

Na raiz do projeto:

```bash
npm install
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
```

Para desenvolvimento com watch:

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

## Execução

Com o ambiente virtual ativado e o banco migrado:

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

- Página inicial (landing) em `/`
- Dashboard (após login) em `/dashboard/`
- Admin em `/admin/` (use o superusuário criado)

## Estrutura do projeto

```
Finanpy/
├── core/                 # Configurações globais, URLs, views públicas e dashboard
├── users/                # Modelo de usuário customizado e autenticação (login/registro)
├── accounts/             # CRUD de contas bancárias
├── categories/           # CRUD de categorias (receitas/despesas)
├── transactions/         # CRUD de transações e lógica de saldo
├── profiles/             # Perfis de usuário (estrutura base)
├── templates/            # Templates Django (base, public, dashboard, components)
├── static/               # Arquivos estáticos (CSS, JS)
├── docs/                 # Documentação do projeto
├── manage.py
├── requirements.txt
├── tailwind.config.js
├── package.json
├── PRD.MD                # Product Requirements Document
└── TASKS.md              # Lista de tarefas por sprint
```

### Apps Django

| App          | Responsabilidade                                      |
|-------------|--------------------------------------------------------|
| `core`      | Settings, URLs raiz, landing page, view do dashboard   |
| `users`     | User customizado (email), registro, login, logout      |
| `accounts`  | Contas bancárias (model, CRUD, listagem)              |
| `categories`| Categorias de transação (receita/despesa)              |
| `transactions` | Transações e atualização de saldo das contas       |
| `profiles`  | Perfil de usuário (estrutura preparada)               |

## Deploy com Docker

Para rodar com Docker e Docker Compose (produção ou ambiente homólogo):

```bash
cp .env.example .env   # edite .env com SECRET_KEY e ALLOWED_HOSTS
docker compose up --build
```

Acesse **http://localhost:8000**. Detalhes (volumes, comandos, produção): **[docs/docker.md](docs/docker.md)**.

Para publicar no **PythonAnywhere** (hosting gratuito): **[docs/pythonanywhere.md](docs/pythonanywhere.md)**.

## Configuração (desenvolvimento vs produção)

As configurações estão separadas em `core/settings/`:

- **Desenvolvimento** (padrão): `core.settings` ou `core.settings.development` — `DEBUG=True`, `ALLOWED_HOSTS` local.
- **Produção**: defina `DJANGO_SETTINGS_MODULE=core.settings.production` e as variáveis de ambiente `SECRET_KEY`, `ALLOWED_HOSTS` e, se quiser, `DATABASE_PATH`. Veja `.env.example`.

## Testes

Executar toda a suíte de testes:

```bash
python manage.py test
```

## Documentação adicional

- **PRD.MD**: requisitos do produto e user stories
- **docs/**: arquitetura, banco de dados e design system
- **CLAUDE.md**: contexto para assistentes de código

## Licença

Projeto em desenvolvimento ativo. Consulte o repositório para informações de licença.
