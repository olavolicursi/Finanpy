# Deploy do Finanpy no PythonAnywhere

Este guia descreve como publicar o Finanpy no [PythonAnywhere](https://www.pythonanywhere.com/) (conta gratuita ou paga).

## Pré-requisitos

- Conta no [PythonAnywhere](https://www.pythonanywhere.com/)
- Projeto no GitHub (ou outro) para clonar no servidor

---

## 1. Criar a Web app (Manual Configuration)

1. No **Dashboard**, abra a aba **Web**.
2. Clique em **Add a new web app**.
3. Escolha **Manual configuration** (não use a opção “Django”).
4. Selecione a versão do Python (ex.: **Python 3.10**).
5. Confirme. Anote o domínio (ex.: `seuusuario.pythonanywhere.com`).

---

## 2. Enviar o código

No **Bash** (aba Consoles → New console → Bash):

```bash
cd ~
git clone https://github.com/SEU_USUARIO/Finanpy.git
cd Finanpy
```

(Substitua `SEU_USUARIO` pelo seu usuário do GitHub. Se o repositório for privado, configure [SSH/Deploy token](https://help.pythonanywhere.com/pages/ExternalVCS).)

---

## 3. Virtualenv e dependências

No mesmo Bash (ou em um novo):

```bash
# Criar virtualenv (Python 3.10; ajuste se precisar)
mkvirtualenv --python=/usr/bin/python3.10 Finanpy

# Ativar (se não estiver ativo)
workon Finanpy

# Instalar dependências
cd ~/Finanpy
pip install -r requirements.txt
```

Se aparecer `mkvirtualenv: command not found`, use antes: [Installing VirtualenvWrapper](https://help.pythonanywhere.com/pages/InstallingVirtualenvWrapper).

---

## 4. Variáveis de ambiente (produção)

O Finanpy usa `core.settings.production`, que lê `SECRET_KEY` e `ALLOWED_HOSTS` do ambiente. No PythonAnywhere isso é feito no **arquivo WSGI** (passo 6). Anote:

- **SECRET_KEY**: uma chave secreta (ex.: `python -c "import secrets; print(secrets.token_urlsafe(50))"`).
- **ALLOWED_HOSTS**: seu domínio, ex.: `seuusuario.pythonanywhere.com`.

---

## 5. Migrações e arquivos estáticos

No Bash, com o virtualenv ativo e na pasta do projeto:

```bash
cd ~/Finanpy
workon Finanpy

# Usar settings de produção (obrigatório para collectstatic correto)
export DJANGO_SETTINGS_MODULE=core.settings.production
export SECRET_KEY="sua-chave-secreta-aqui"
export ALLOWED_HOSTS="seuusuario.pythonanywhere.com"

python manage.py migrate
python manage.py collectstatic --noinput
```

(Substitua `sua-chave-secreta-aqui` e `seuusuario.pythonanywhere.com`.)

---

## 6. Configurar o WSGI

1. Na aba **Web**, em **Code**, clique no link do arquivo **WSGI** (ex.: `/var/www/seuusuario_pythonanywhere_com_wsgi.py`).
2. Apague o conteúdo e deixe apenas algo como o bloco abaixo (ajustando caminhos e nome do virtualenv):

```python
# +++++++++++ Finanpy (Django) +++++++++++
import os
import sys

# Caminho da pasta do projeto (onde está manage.py)
path = '/home/SEU_USUARIO_PA/Finanpy'
if path not in sys.path:
    sys.path.insert(0, path)

# Variáveis de ambiente para production
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.production'
os.environ['SECRET_KEY'] = 'COLOQUE_SUA_SECRET_KEY_AQUI'
os.environ['ALLOWED_HOSTS'] = 'seuusuario.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Substitua:

- `SEU_USUARIO_PA` pelo seu **username do PythonAnywhere** (ex.: `olavo` → path = `/home/olavo/Finanpy`).
- `COLOQUE_SUA_SECRET_KEY_AQUI` pela mesma `SECRET_KEY` usada no passo 5.
- `seuusuario.pythonanywhere.com` pelo seu domínio real (o que aparece no topo da aba Web).

Salve o arquivo.

---

## 7. Virtualenv na Web app

Na aba **Web**, em **Virtualenv**, clique em **Enter path to a virtualenv** e informe:

- `Finanpy` (nome curto)  
  ou o caminho completo: `/home/SEU_USUARIO_PA/.virtualenvs/Finanpy`

Clique no ícone verde para carregar.

---

## 8. Mapeamento de arquivos estáticos

1. Na aba **Web**, role até **Static files**.
2. Em **URL** coloque: `/static/`
3. Em **Directory** coloque o caminho absoluto da pasta de estáticos coletados, por exemplo:
   - `/home/SEU_USUARIO_PA/Finanpy/staticfiles`
4. Salve (Add/Update) e, em seguida, clique em **Reload** (canto superior direito da aba Web).

---

## 9. (Opcional) Working directory e link do código

Em **Code**:

- **Source code**: `/home/SEU_USUARIO_PA/Finanpy`
- **Working directory**: `/home/SEU_USUARIO_PA/Finanpy`

Isso facilita achar o projeto e rodar comandos.

---

## 10. Recarregar e testar

1. Na aba **Web**, clique em **Reload** (verde).
2. Acesse `https://seuusuario.pythonanywhere.com/`.
3. Deve aparecer a landing do Finanpy com CSS. Faça registro/login e teste o dashboard.

Se der **500**, abra o **Error log** (link na mesma aba Web) e confira a mensagem.

---

## Criar superusuário (admin)

No Bash:

```bash
cd ~/Finanpy
workon Finanpy
export DJANGO_SETTINGS_MODULE=core.settings.production
export SECRET_KEY="sua-chave"
export ALLOWED_HOSTS="seuusuario.pythonanywhere.com"
python manage.py createsuperuser
```

Use o e-mail como usuário de login. Depois acesse `https://seuusuario.pythonanywhere.com/admin/`.

---

## Atualizar o site depois de mudanças no código

No Bash:

```bash
cd ~/Finanpy
git pull
workon Finanpy
export DJANGO_SETTINGS_MODULE=core.settings.production
export SECRET_KEY="sua-chave"
export ALLOWED_HOSTS="seuusuario.pythonanywhere.com"
python manage.py migrate
python manage.py collectstatic --noinput
```

Na aba **Web**, clique em **Reload**.

---

## Resumo de caminhos (ajuste com seu usuário PA)

| Item            | Exemplo (usuário `olavo`)              |
|-----------------|----------------------------------------|
| Projeto         | `/home/olavo/Finanpy`                  |
| STATIC_ROOT     | `/home/olavo/Finanpy/staticfiles`      |
| Virtualenv      | `Finanpy` ou `/home/olavo/.virtualenvs/Finanpy` |
| WSGI            | `/var/www/olavo_pythonanywhere_com_wsgi.py`     |
| Domínio         | `olavo.pythonanywhere.com`             |

Com isso, o projeto sobe no PythonAnywhere usando `core.settings.production`, variáveis de ambiente no WSGI, SQLite (arquivo no próprio servidor) e estáticos servidos pelo mapeamento `/static/` → `staticfiles/`.
