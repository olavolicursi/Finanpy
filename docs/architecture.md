# Arquitetura Técnica

Entenda como o Finanpy está estruturado.

## Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| **Backend** | Python 3.12+ / Django 6.0+ |
| **Banco de Dados** | SQLite 3 |
| **Frontend** | Django Templates + TailwindCSS 3.x |
| **Autenticação** | Django Auth System (Login por Email) |

## Estrutura do Projeto

O projeto segue uma arquitetura modular monolítica, organizada em apps Django:

- **core/**: Configurações globais do projeto (`settings.py`, `urls.py`).
- **users/**: Gerenciamento de usuários e autenticação customizada.
- **profiles/**: Gerenciamento de perfis de usuário (Avatar, Bio).
- **accounts/**: Gestão de contas bancárias (Corrente, Poupança, etc).
- **categories/**: Categorização de transações (Receitas/Despesas).
- **transactions/**: Registro de movimentações financeiras.
- **templates/**: Arquivos HTML globais e específicos de cada módulo.
- **static/**: Arquivos CSS, JS e imagens.

## Design Patterns

- **MVT (Model-View-Template)**: Padrão nativo do Django.
- **Class Based Views (CBVs)**: Utilizadas preferencialmente para views.
- **DRY (Don't Repeat Yourself)**: Reutilização de componentes e templates (sidebar, navbar).
