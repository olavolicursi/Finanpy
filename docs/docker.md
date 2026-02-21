# Uso do Docker (Finanpy)

Este documento descreve como executar o Finanpy com **Docker** e **Docker Compose** para deploy ou ambiente homólogo à produção.

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2+)

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (copie de `.env.example`):

```bash
cp .env.example .env
```

Edite `.env` e defina pelo menos:

- **SECRET_KEY**: chave secreta do Django (produção). Exemplo: `python -c "import secrets; print(secrets.token_urlsafe(50))"`
- **ALLOWED_HOSTS**: hosts permitidos, separados por vírgula (ex: `localhost,127.0.0.1,.seudominio.com`)
- **DEBUG**: `false` em produção

## Build e execução

### Subir com Docker Compose

Na raiz do projeto:

```bash
docker compose up --build
```

A aplicação estará disponível em **http://localhost:8000**.

### Parar

```bash
docker compose down
```

Para remover também os volumes (apaga banco e estáticos):

```bash
docker compose down -v
```

## Volumes (dados persistentes)

O `docker-compose.yml` define dois volumes nomeados:

| Volume      | Montagem        | Uso                          |
|------------|------------------|------------------------------|
| `db_data`  | `/app/db_data`   | Banco SQLite (`db.sqlite3`)  |
| `static_data` | `/app/staticfiles` | Arquivos estáticos coletados |

Assim, ao reiniciar com `docker compose up`, os dados do banco e os estáticos são mantidos.

## Comandos úteis

- **Criar superusuário** (com o container em execução):

  ```bash
  docker compose exec web python manage.py createsuperuser
  ```

- **Rodar migrações manualmente**:

  ```bash
  docker compose exec web python manage.py migrate
  ```

- **Coletar arquivos estáticos**:

  ```bash
  docker compose exec web python manage.py collectstatic --noinput
  ```

- **Abrir shell no container**:

  ```bash
  docker compose exec web sh
  ```

## Imagem standalone (sem Compose)

Para build e execução apenas com Docker:

```bash
docker build -t finanpy .
docker run -p 8000:8000 \
  -e SECRET_KEY="sua-chave-secreta" \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  -e DEBUG=false \
  -v finanpy_db:/app/db_data \
  -e DATABASE_PATH=/app/db_data/db.sqlite3 \
  finanpy
```

O banco será persistido no volume nomeado `finanpy_db`.

## Produção

Em produção real, recomenda-se:

- Usar **PostgreSQL** (ou outro banco) em vez de SQLite (configurar em `core.settings.production` com `DATABASE_URL` ou equivalente).
- Colocar um **proxy reverso** (Nginx, Caddy) na frente do Gunicorn para servir estáticos e SSL.
- Nunca usar `DEBUG=true` e garantir `SECRET_KEY` e `ALLOWED_HOSTS` corretos.
