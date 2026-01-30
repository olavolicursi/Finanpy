## Lista de Tarefas

### Sprint 1: Configuração Inicial e Autenticação

#### 1.1 Configuração do Projeto

- [X] **1.1.1** Configurar settings.py
  - [X] 1.1.1.1 Adicionar apps ao INSTALLED_APPS (users, accounts, categories, transactions)
  - [X] 1.1.1.2 Configurar AUTH_USER_MODEL = 'users.User'
  - [X] 1.1.1.3 Configurar LANGUAGE_CODE = 'pt-br'
  - [X] 1.1.1.4 Configurar TIME_ZONE = 'America/Sao_Paulo'
  - [X] 1.1.1.5 Configurar diretório TEMPLATES (templates/)
  - [X] 1.1.1.6 Configurar STATICFILES_DIRS e STATIC_ROOT
  - [X] 1.1.1.7 Configurar LOGIN_URL, LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL

- [X] **1.1.2** Configurar TailwindCSS
  - [X] 1.1.2.1 Criar package.json com dependências do Tailwind
  - [X] 1.1.2.2 Criar tailwind.config.js com configuração de paths
  - [X] 1.1.2.3 Criar arquivo CSS base com diretivas @tailwind
  - [X] 1.1.2.4 Configurar script de build do Tailwind
  - [X] 1.1.2.5 Gerar output.css inicial

- [X] **1.1.3** Criar estrutura de templates
  - [X] 1.1.3.1 Criar diretório templates/ na raiz
  - [X] 1.1.3.2 Criar diretório templates/components/
  - [X] 1.1.3.3 Criar diretório templates/public/
  - [X] 1.1.3.4 Criar diretório templates/dashboard/
  - [X] 1.1.3.5 Criar diretório static/css/
  - [X] 1.1.3.6 Criar diretório static/js/

#### 1.2 Model de Usuário Customizado

- [ ] **1.2.1** Implementar model User
  - [ ] 1.2.1.1 Criar classe User herdando de AbstractUser em users/models.py
  - [ ] 1.2.1.2 Definir username = None
  - [ ] 1.2.1.3 Definir email como campo único e obrigatório
  - [ ] 1.2.1.4 Definir USERNAME_FIELD = 'email'
  - [ ] 1.2.1.5 Definir REQUIRED_FIELDS = []
  - [ ] 1.2.1.6 Adicionar campos created_at e updated_at
  - [ ] 1.2.1.7 Criar UserManager customizado para criar usuários por email

- [ ] **1.2.2** Configurar admin do User
  - [ ] 1.2.2.1 Criar classe UserAdmin em users/admin.py
  - [ ] 1.2.2.2 Configurar list_display com campos relevantes
  - [ ] 1.2.2.3 Configurar search_fields para busca por email
  - [ ] 1.2.2.4 Registrar User no admin

- [ ] **1.2.3** Criar e aplicar migrações
  - [ ] 1.2.3.1 Executar makemigrations users
  - [ ] 1.2.3.2 Executar migrate
  - [ ] 1.2.3.3 Criar superusuário para testes

#### 1.3 Template Base e Componentes

- [ ] **1.3.1** Criar template base.html
  - [ ] 1.3.1.1 Definir estrutura HTML5 com doctype
  - [ ] 1.3.1.2 Configurar meta tags (viewport, charset)
  - [ ] 1.3.1.3 Incluir link para output.css do Tailwind
  - [ ] 1.3.1.4 Definir fundo escuro (bg-gray-950)
  - [ ] 1.3.1.5 Criar bloco {% block content %}
  - [ ] 1.3.1.6 Criar bloco {% block title %}
  - [ ] 1.3.1.7 Criar bloco {% block extra_css %}
  - [ ] 1.3.1.8 Criar bloco {% block extra_js %}

- [ ] **1.3.2** Criar template base_public.html
  - [ ] 1.3.2.1 Estender base.html
  - [ ] 1.3.2.2 Layout para páginas públicas (landing, login, registro)
  - [ ] 1.3.2.3 Navbar simples com logo e links

- [ ] **1.3.3** Criar template base_dashboard.html
  - [ ] 1.3.3.1 Estender base.html
  - [ ] 1.3.3.2 Incluir sidebar com navegação
  - [ ] 1.3.3.3 Área de conteúdo principal
  - [ ] 1.3.3.4 Bloco para mensagens de feedback

- [ ] **1.3.4** Criar componentes reutilizáveis
  - [ ] 1.3.4.1 Criar components/navbar.html
  - [ ] 1.3.4.2 Criar components/sidebar.html
  - [ ] 1.3.4.3 Criar components/card.html
  - [ ] 1.3.4.4 Criar components/form_field.html
  - [ ] 1.3.4.5 Criar components/button.html
  - [ ] 1.3.4.6 Criar components/alert.html

#### 1.4 Landing Page

- [ ] **1.4.1** Criar view da landing page
  - [ ] 1.4.1.1 Criar view landing_page em core/views.py ou criar app 'pages'
  - [ ] 1.4.1.2 Usar TemplateView ou função simples
  - [ ] 1.4.1.3 Redirecionar para dashboard se usuário autenticado

- [ ] **1.4.2** Criar template da landing page
  - [ ] 1.4.2.1 Criar templates/public/landing.html
  - [ ] 1.4.2.2 Seção hero com título e subtítulo
  - [ ] 1.4.2.3 Gradiente de fundo cyan/emerald
  - [ ] 1.4.2.4 Botões "Cadastre-se" e "Entrar"
  - [ ] 1.4.2.5 Seção de features/benefícios
  - [ ] 1.4.2.6 Design responsivo

- [ ] **1.4.3** Configurar URL da landing page
  - [ ] 1.4.3.1 Adicionar rota '' para landing page em core/urls.py

#### 1.5 Sistema de Autenticação

- [ ] **1.5.1** Criar formulários de autenticação
  - [ ] 1.5.1.1 Criar users/forms.py
  - [ ] 1.5.1.2 Criar UserRegistrationForm com campos: first_name, last_name, email, password1, password2
  - [ ] 1.5.1.3 Criar UserLoginForm (AuthenticationForm customizado para email)
  - [ ] 1.5.1.4 Estilizar campos com classes Tailwind

- [ ] **1.5.2** Criar views de autenticação
  - [ ] 1.5.2.1 Criar RegisterView (CreateView) em users/views.py
  - [ ] 1.5.2.2 Criar LoginView customizada para usar email
  - [ ] 1.5.2.3 Configurar LogoutView
  - [ ] 1.5.2.4 Configurar redirecionamentos após login/logout

- [ ] **1.5.3** Criar templates de autenticação
  - [ ] 1.5.3.1 Criar templates/users/register.html
  - [ ] 1.5.3.2 Criar templates/users/login.html
  - [ ] 1.5.3.3 Estilizar formulários com design system
  - [ ] 1.5.3.4 Adicionar validação visual de erros
  - [ ] 1.5.3.5 Adicionar links entre login e registro

- [ ] **1.5.4** Configurar URLs de autenticação
  - [ ] 1.5.4.1 Criar users/urls.py
  - [ ] 1.5.4.2 Adicionar rotas: register/, login/, logout/
  - [ ] 1.5.4.3 Incluir users.urls em core/urls.py

---

### Sprint 2: Dashboard e Estrutura Base dos Módulos

#### 2.1 Dashboard Básico

- [ ] **2.1.1** Criar view do dashboard
  - [ ] 2.1.1.1 Criar views.py na app core ou criar app 'dashboard'
  - [ ] 2.1.1.2 Criar DashboardView (TemplateView)
  - [ ] 2.1.1.3 Adicionar LoginRequiredMixin
  - [ ] 2.1.1.4 Preparar contexto inicial vazio (será populado depois)

- [ ] **2.1.2** Criar template do dashboard
  - [ ] 2.1.2.1 Criar templates/dashboard/index.html
  - [ ] 2.1.2.2 Estender base_dashboard.html
  - [ ] 2.1.2.3 Criar grid de cards para estatísticas
  - [ ] 2.1.2.4 Card de saldo total (placeholder)
  - [ ] 2.1.2.5 Card de receitas do mês (placeholder)
  - [ ] 2.1.2.6 Card de despesas do mês (placeholder)
  - [ ] 2.1.2.7 Área para últimas transações (placeholder)
  - [ ] 2.1.2.8 Área para saldos por conta (placeholder)

- [ ] **2.1.3** Configurar URL do dashboard
  - [ ] 2.1.3.1 Adicionar rota 'dashboard/' em core/urls.py
  - [ ] 2.1.3.2 Configurar como LOGIN_REDIRECT_URL

#### 2.2 Model de Contas Bancárias

- [ ] **2.2.1** Implementar model Account
  - [ ] 2.2.1.1 Criar classe Account em accounts/models.py
  - [ ] 2.2.1.2 Definir ACCOUNT_TYPES choices
  - [ ] 2.2.1.3 Campo user (ForeignKey para User)
  - [ ] 2.2.1.4 Campo name (CharField, max_length=100)
  - [ ] 2.2.1.5 Campo account_type (CharField com choices)
  - [ ] 2.2.1.6 Campo balance (DecimalField, max_digits=12, decimal_places=2)
  - [ ] 2.2.1.7 Campo color (CharField, max_length=7, default='#06b6d4')
  - [ ] 2.2.1.8 Campo is_active (BooleanField, default=True)
  - [ ] 2.2.1.9 Campos created_at e updated_at
  - [ ] 2.2.1.10 Método **str** retornando nome da conta
  - [ ] 2.2.1.11 Meta class com ordering

- [ ] **2.2.2** Configurar admin de Account
  - [ ] 2.2.2.1 Criar AccountAdmin em accounts/admin.py
  - [ ] 2.2.2.2 Configurar list_display
  - [ ] 2.2.2.3 Configurar list_filter por tipo e usuário
  - [ ] 2.2.2.4 Registrar Account no admin

- [ ] **2.2.3** Criar e aplicar migrações
  - [ ] 2.2.3.1 Executar makemigrations accounts
  - [ ] 2.2.3.2 Executar migrate

#### 2.3 Model de Categorias

- [ ] **2.3.1** Implementar model Category
  - [ ] 2.3.1.1 Criar classe Category em categories/models.py
  - [ ] 2.3.1.2 Definir CATEGORY_TYPES choices (income, expense)
  - [ ] 2.3.1.3 Campo user (ForeignKey para User)
  - [ ] 2.3.1.4 Campo name (CharField, max_length=100)
  - [ ] 2.3.1.5 Campo category_type (CharField com choices)
  - [ ] 2.3.1.6 Campo icon (CharField, max_length=50, blank=True)
  - [ ] 2.3.1.7 Campo color (CharField, max_length=7, default='#06b6d4')
  - [ ] 2.3.1.8 Campos created_at e updated_at
  - [ ] 2.3.1.9 Método **str** retornando nome da categoria
  - [ ] 2.3.1.10 Meta class com ordering e verbose_name_plural

- [ ] **2.3.2** Configurar admin de Category
  - [ ] 2.3.2.1 Criar CategoryAdmin em categories/admin.py
  - [ ] 2.3.2.2 Configurar list_display
  - [ ] 2.3.2.3 Configurar list_filter por tipo
  - [ ] 2.3.2.4 Registrar Category no admin

- [ ] **2.3.3** Criar e aplicar migrações
  - [ ] 2.3.3.1 Executar makemigrations categories
  - [ ] 2.3.3.2 Executar migrate

#### 2.4 Model de Transações

- [ ] **2.4.1** Implementar model Transaction
  - [ ] 2.4.1.1 Criar classe Transaction em transactions/models.py
  - [ ] 2.4.1.2 Definir TRANSACTION_TYPES choices (income, expense)
  - [ ] 2.4.1.3 Campo user (ForeignKey para User)
  - [ ] 2.4.1.4 Campo account (ForeignKey para Account, on_delete=CASCADE)
  - [ ] 2.4.1.5 Campo category (ForeignKey para Category, on_delete=SET_NULL, null=True)
  - [ ] 2.4.1.6 Campo transaction_type (CharField com choices)
  - [ ] 2.4.1.7 Campo amount (DecimalField, max_digits=12, decimal_places=2)
  - [ ] 2.4.1.8 Campo date (DateField)
  - [ ] 2.4.1.9 Campo description (CharField, max_length=255, blank=True)
  - [ ] 2.4.1.10 Campos created_at e updated_at
  - [ ] 2.4.1.11 Método **str** retornando descrição ou tipo + valor
  - [ ] 2.4.1.12 Meta class com ordering por data decrescente

- [ ] **2.4.2** Configurar admin de Transaction
  - [ ] 2.4.2.1 Criar TransactionAdmin em transactions/admin.py
  - [ ] 2.4.2.2 Configurar list_display
  - [ ] 2.4.2.3 Configurar list_filter por tipo, conta e categoria
  - [ ] 2.4.2.4 Configurar date_hierarchy
  - [ ] 2.4.2.5 Registrar Transaction no admin

- [ ] **2.4.3** Criar e aplicar migrações
  - [ ] 2.4.3.1 Executar makemigrations transactions
  - [ ] 2.4.3.2 Executar migrate

---

### Sprint 3: CRUD de Contas Bancárias

#### 3.1 Formulário de Contas

- [ ] **3.1.1** Criar formulário de Account
  - [ ] 3.1.1.1 Criar accounts/forms.py
  - [ ] 3.1.1.2 Criar AccountForm (ModelForm)
  - [ ] 3.1.1.3 Definir fields: name, account_type, balance, color
  - [ ] 3.1.1.4 Configurar widgets com classes Tailwind
  - [ ] 3.1.1.5 Definir labels em português
  - [ ] 3.1.1.6 Configurar help_texts se necessário

#### 3.2 Views de Contas

- [ ] **3.2.1** Criar view de listagem
  - [ ] 3.2.1.1 Criar AccountListView (ListView) em accounts/views.py
  - [ ] 3.2.1.2 Adicionar LoginRequiredMixin
  - [ ] 3.2.1.3 Filtrar queryset por request.user
  - [ ] 3.2.1.4 Ordenar por nome

- [ ] **3.2.2** Criar view de criação
  - [ ] 3.2.2.1 Criar AccountCreateView (CreateView)
  - [ ] 3.2.2.2 Adicionar LoginRequiredMixin
  - [ ] 3.2.2.3 Usar AccountForm
  - [ ] 3.2.2.4 Sobrescrever form_valid para associar user
  - [ ] 3.2.2.5 Configurar success_url para lista de contas
  - [ ] 3.2.2.6 Adicionar mensagem de sucesso

- [ ] **3.2.3** Criar view de edição
  - [ ] 3.2.3.1 Criar AccountUpdateView (UpdateView)
  - [ ] 3.2.3.2 Adicionar LoginRequiredMixin
  - [ ] 3.2.3.3 Filtrar queryset por request.user
  - [ ] 3.2.3.4 Usar AccountForm
  - [ ] 3.2.3.5 Configurar success_url
  - [ ] 3.2.3.6 Adicionar mensagem de sucesso

- [ ] **3.2.4** Criar view de exclusão
  - [ ] 3.2.4.1 Criar AccountDeleteView (DeleteView)
  - [ ] 3.2.4.2 Adicionar LoginRequiredMixin
  - [ ] 3.2.4.3 Filtrar queryset por request.user
  - [ ] 3.2.4.4 Configurar success_url
  - [ ] 3.2.4.5 Adicionar mensagem de sucesso

#### 3.3 Templates de Contas

- [ ] **3.3.1** Criar template de listagem
  - [ ] 3.3.1.1 Criar templates/accounts/account_list.html
  - [ ] 3.3.1.2 Estender base_dashboard.html
  - [ ] 3.3.1.3 Título da página "Contas"
  - [ ] 3.3.1.4 Botão "Nova Conta"
  - [ ] 3.3.1.5 Grid ou lista de cards de contas
  - [ ] 3.3.1.6 Exibir nome, tipo, saldo e cor de cada conta
  - [ ] 3.3.1.7 Botões de editar e excluir em cada card
  - [ ] 3.3.1.8 Mensagem quando não há contas
  - [ ] 3.3.1.9 Exibir mensagens de feedback

- [ ] **3.3.2** Criar template de criação/edição
  - [ ] 3.3.2.1 Criar templates/accounts/account_form.html
  - [ ] 3.3.2.2 Estender base_dashboard.html
  - [ ] 3.3.2.3 Título dinâmico (Nova/Editar Conta)
  - [ ] 3.3.2.4 Formulário estilizado com design system
  - [ ] 3.3.2.5 Botões Cancelar e Salvar
  - [ ] 3.3.2.6 Exibição de erros de validação

- [ ] **3.3.3** Criar template de confirmação de exclusão
  - [ ] 3.3.3.1 Criar templates/accounts/account_confirm_delete.html
  - [ ] 3.3.3.2 Estender base_dashboard.html
  - [ ] 3.3.3.3 Mensagem de confirmação
  - [ ] 3.3.3.4 Exibir nome da conta a ser excluída
  - [ ] 3.3.3.5 Botões Cancelar e Excluir

#### 3.4 URLs de Contas

- [ ] **3.4.1** Configurar URLs
  - [ ] 3.4.1.1 Criar accounts/urls.py
  - [ ] 3.4.1.2 Definir app_name = 'accounts'
  - [ ] 3.4.1.3 Rota '' para AccountListView (name='list')
  - [ ] 3.4.1.4 Rota 'create/' para AccountCreateView (name='create')
  - [ ] 3.4.1.5 Rota '<int:pk>/edit/' para AccountUpdateView (name='edit')
  - [ ] 3.4.1.6 Rota '<int:pk>/delete/' para AccountDeleteView (name='delete')
  - [ ] 3.4.1.7 Incluir accounts.urls em core/urls.py com prefix 'accounts/'

---

### Sprint 4: CRUD de Categorias

#### 4.1 Formulário de Categorias

- [ ] **4.1.1** Criar formulário de Category
  - [ ] 4.1.1.1 Criar categories/forms.py
  - [ ] 4.1.1.2 Criar CategoryForm (ModelForm)
  - [ ] 4.1.1.3 Definir fields: name, category_type, icon, color
  - [ ] 4.1.1.4 Configurar widgets com classes Tailwind
  - [ ] 4.1.1.5 Definir labels em português
  - [ ] 4.1.1.6 Configurar choices para category_type

#### 4.2 Views de Categorias

- [ ] **4.2.1** Criar view de listagem
  - [ ] 4.2.1.1 Criar CategoryListView (ListView) em categories/views.py
  - [ ] 4.2.1.2 Adicionar LoginRequiredMixin
  - [ ] 4.2.1.3 Filtrar queryset por request.user
  - [ ] 4.2.1.4 Ordenar por tipo e nome

- [ ] **4.2.2** Criar view de criação
  - [ ] 4.2.2.1 Criar CategoryCreateView (CreateView)
  - [ ] 4.2.2.2 Adicionar LoginRequiredMixin
  - [ ] 4.2.2.3 Usar CategoryForm
  - [ ] 4.2.2.4 Sobrescrever form_valid para associar user
  - [ ] 4.2.2.5 Configurar success_url
  - [ ] 4.2.2.6 Adicionar mensagem de sucesso

- [ ] **4.2.3** Criar view de edição
  - [ ] 4.2.3.1 Criar CategoryUpdateView (UpdateView)
  - [ ] 4.2.3.2 Adicionar LoginRequiredMixin
  - [ ] 4.2.3.3 Filtrar queryset por request.user
  - [ ] 4.2.3.4 Usar CategoryForm
  - [ ] 4.2.3.5 Configurar success_url
  - [ ] 4.2.3.6 Adicionar mensagem de sucesso

- [ ] **4.2.4** Criar view de exclusão
  - [ ] 4.2.4.1 Criar CategoryDeleteView (DeleteView)
  - [ ] 4.2.4.2 Adicionar LoginRequiredMixin
  - [ ] 4.2.4.3 Filtrar queryset por request.user
  - [ ] 4.2.4.4 Configurar success_url
  - [ ] 4.2.4.5 Adicionar mensagem de sucesso

#### 4.3 Templates de Categorias

- [ ] **4.3.1** Criar template de listagem
  - [ ] 4.3.1.1 Criar templates/categories/category_list.html
  - [ ] 4.3.1.2 Estender base_dashboard.html
  - [ ] 4.3.1.3 Título "Categorias"
  - [ ] 4.3.1.4 Botão "Nova Categoria"
  - [ ] 4.3.1.5 Separar categorias por tipo (Receitas/Despesas)
  - [ ] 4.3.1.6 Grid de cards de categorias
  - [ ] 4.3.1.7 Exibir nome, tipo, ícone e cor
  - [ ] 4.3.1.8 Botões de editar e excluir
  - [ ] 4.3.1.9 Mensagem quando não há categorias

- [ ] **4.3.2** Criar template de criação/edição
  - [ ] 4.3.2.1 Criar templates/categories/category_form.html
  - [ ] 4.3.2.2 Estender base_dashboard.html
  - [ ] 4.3.2.3 Título dinâmico
  - [ ] 4.3.2.4 Formulário estilizado
  - [ ] 4.3.2.5 Botões Cancelar e Salvar

- [ ] **4.3.3** Criar template de confirmação de exclusão
  - [ ] 4.3.3.1 Criar templates/categories/category_confirm_delete.html
  - [ ] 4.3.3.2 Mensagem de confirmação
  - [ ] 4.3.3.3 Botões Cancelar e Excluir

#### 4.4 URLs de Categorias

- [ ] **4.4.1** Configurar URLs
  - [ ] 4.4.1.1 Criar categories/urls.py
  - [ ] 4.4.1.2 Definir app_name = 'categories'
  - [ ] 4.4.1.3 Rota '' para CategoryListView (name='list')
  - [ ] 4.4.1.4 Rota 'create/' para CategoryCreateView (name='create')
  - [ ] 4.4.1.5 Rota '<int:pk>/edit/' para CategoryUpdateView (name='edit')
  - [ ] 4.4.1.6 Rota '<int:pk>/delete/' para CategoryDeleteView (name='delete')
  - [ ] 4.4.1.7 Incluir categories.urls em core/urls.py

---

### Sprint 5: CRUD de Transações

#### 5.1 Formulário de Transações

- [ ] **5.1.1** Criar formulário de Transaction
  - [ ] 5.1.1.1 Criar transactions/forms.py
  - [ ] 5.1.1.2 Criar TransactionForm (ModelForm)
  - [ ] 5.1.1.3 Definir fields: transaction_type, account, category, amount, date, description
  - [ ] 5.1.1.4 Configurar widgets com classes Tailwind
  - [ ] 5.1.1.5 Widget de date com type="date"
  - [ ] 5.1.1.6 Definir labels em português
  - [ ] 5.1.1.7 Sobrescrever **init** para filtrar contas e categorias do usuário

#### 5.2 Views de Transações

- [ ] **5.2.1** Criar view de listagem
  - [ ] 5.2.1.1 Criar TransactionListView (ListView) em transactions/views.py
  - [ ] 5.2.1.2 Adicionar LoginRequiredMixin
  - [ ] 5.2.1.3 Filtrar queryset por request.user
  - [ ] 5.2.1.4 Ordenar por data decrescente
  - [ ] 5.2.1.5 Usar select_related para account e category
  - [ ] 5.2.1.6 Paginar resultados (opcional)

- [ ] **5.2.2** Criar view de criação
  - [ ] 5.2.2.1 Criar TransactionCreateView (CreateView)
  - [ ] 5.2.2.2 Adicionar LoginRequiredMixin
  - [ ] 5.2.2.3 Usar TransactionForm
  - [ ] 5.2.2.4 Sobrescrever get_form para passar user
  - [ ] 5.2.2.5 Sobrescrever form_valid para associar user
  - [ ] 5.2.2.6 Atualizar saldo da conta no form_valid
  - [ ] 5.2.2.7 Configurar success_url
  - [ ] 5.2.2.8 Adicionar mensagem de sucesso

- [ ] **5.2.3** Criar view de edição
  - [ ] 5.2.3.1 Criar TransactionUpdateView (UpdateView)
  - [ ] 5.2.3.2 Adicionar LoginRequiredMixin
  - [ ] 5.2.3.3 Filtrar queryset por request.user
  - [ ] 5.2.3.4 Sobrescrever get_form para passar user
  - [ ] 5.2.3.5 Recalcular saldo da conta no form_valid
  - [ ] 5.2.3.6 Configurar success_url
  - [ ] 5.2.3.7 Adicionar mensagem de sucesso

- [ ] **5.2.4** Criar view de exclusão
  - [ ] 5.2.4.1 Criar TransactionDeleteView (DeleteView)
  - [ ] 5.2.4.2 Adicionar LoginRequiredMixin
  - [ ] 5.2.4.3 Filtrar queryset por request.user
  - [ ] 5.2.4.4 Reverter saldo da conta no delete
  - [ ] 5.2.4.5 Configurar success_url
  - [ ] 5.2.4.6 Adicionar mensagem de sucesso

#### 5.3 Lógica de Atualização de Saldo

- [ ] **5.3.1** Implementar lógica de saldo
  - [ ] 5.3.1.1 Criar método ou signal para atualizar saldo ao criar transação
  - [ ] 5.3.1.2 Receita: saldo += amount
  - [ ] 5.3.1.3 Despesa: saldo -= amount
  - [ ] 5.3.1.4 Ao editar: reverter valor antigo, aplicar novo
  - [ ] 5.3.1.5 Ao excluir: reverter valor da transação

#### 5.4 Templates de Transações

- [ ] **5.4.1** Criar template de listagem
  - [ ] 5.4.1.1 Criar templates/transactions/transaction_list.html
  - [ ] 5.4.1.2 Estender base_dashboard.html
  - [ ] 5.4.1.3 Título "Transações"
  - [ ] 5.4.1.4 Botão "Nova Transação"
  - [ ] 5.4.1.5 Tabela de transações
  - [ ] 5.4.1.6 Colunas: Data, Descrição, Categoria, Conta, Valor, Ações
  - [ ] 5.4.1.7 Valor verde para receita, vermelho para despesa
  - [ ] 5.4.1.8 Botões de editar e excluir
  - [ ] 5.4.1.9 Mensagem quando não há transações

- [ ] **5.4.2** Criar template de criação/edição
  - [ ] 5.4.2.1 Criar templates/transactions/transaction_form.html
  - [ ] 5.4.2.2 Estender base_dashboard.html
  - [ ] 5.4.2.3 Título dinâmico
  - [ ] 5.4.2.4 Formulário estilizado
  - [ ] 5.4.2.5 Botões Cancelar e Salvar

- [ ] **5.4.3** Criar template de confirmação de exclusão
  - [ ] 5.4.3.1 Criar templates/transactions/transaction_confirm_delete.html
  - [ ] 5.4.3.2 Mensagem de confirmação com detalhes da transação
  - [ ] 5.4.3.3 Botões Cancelar e Excluir

#### 5.5 URLs de Transações

- [ ] **5.5.1** Configurar URLs
  - [ ] 5.5.1.1 Criar transactions/urls.py
  - [ ] 5.5.1.2 Definir app_name = 'transactions'
  - [ ] 5.5.1.3 Rota '' para TransactionListView (name='list')
  - [ ] 5.5.1.4 Rota 'create/' para TransactionCreateView (name='create')
  - [ ] 5.5.1.5 Rota '<int:pk>/edit/' para TransactionUpdateView (name='edit')
  - [ ] 5.5.1.6 Rota '<int:pk>/delete/' para TransactionDeleteView (name='delete')
  - [ ] 5.5.1.7 Incluir transactions.urls em core/urls.py

---

### Sprint 6: Dashboard Completo e Refinamentos

#### 6.1 Dashboard com Dados Reais

- [ ] **6.1.1** Atualizar view do dashboard
  - [ ] 6.1.1.1 Calcular saldo total (soma de todas as contas do usuário)
  - [ ] 6.1.1.2 Calcular receitas do mês atual
  - [ ] 6.1.1.3 Calcular despesas do mês atual
  - [ ] 6.1.1.4 Calcular balanço do mês (receitas - despesas)
  - [ ] 6.1.1.5 Buscar últimas 5 transações
  - [ ] 6.1.1.6 Listar contas com saldos
  - [ ] 6.1.1.7 Passar dados para o contexto

- [ ] **6.1.2** Atualizar template do dashboard
  - [ ] 6.1.2.1 Exibir saldo total no card principal
  - [ ] 6.1.2.2 Exibir receitas do mês com valor em verde
  - [ ] 6.1.2.3 Exibir despesas do mês com valor em vermelho
  - [ ] 6.1.2.4 Exibir balanço com cor condicional
  - [ ] 6.1.2.5 Lista de últimas transações
  - [ ] 6.1.2.6 Cards de contas com saldos
  - [ ] 6.1.2.7 Links para ver mais transações/contas

#### 6.2 Mensagens de Feedback

- [ ] **6.2.1** Configurar sistema de mensagens
  - [ ] 6.2.1.1 Verificar MessageMiddleware no settings
  - [ ] 6.2.1.2 Adicionar messages framework context processor
  - [ ] 6.2.1.3 Criar componente de alert para mensagens
  - [ ] 6.2.1.4 Estilizar mensagens (success, error, warning, info)
  - [ ] 6.2.1.5 Adicionar mensagens em todas as views de CRUD

#### 6.3 Navegação e Links

- [ ] **6.3.1** Atualizar sidebar
  - [ ] 6.3.1.1 Adicionar link para Dashboard
  - [ ] 6.3.1.2 Adicionar link para Contas
  - [ ] 6.3.1.3 Adicionar link para Categorias
  - [ ] 6.3.1.4 Adicionar link para Transações
  - [ ] 6.3.1.5 Destacar item ativo da navegação
  - [ ] 6.3.1.6 Adicionar botão de logout

- [ ] **6.3.2** Atualizar navbar (mobile)
  - [ ] 6.3.2.1 Menu hamburger para mobile
  - [ ] 6.3.2.2 Links de navegação no menu mobile
  - [ ] 6.3.2.3 Botão de logout no mobile

#### 6.4 Refinamentos de UI

- [ ] **6.4.1** Melhorias visuais
  - [ ] 6.4.1.1 Adicionar ícones nos botões
  - [ ] 6.4.1.2 Adicionar ícones na sidebar
  - [ ] 6.4.1.3 Melhorar espaçamentos
  - [ ] 6.4.1.4 Adicionar transições e animações sutis
  - [ ] 6.4.1.5 Verificar responsividade em todas as páginas

- [ ] **6.4.2** Validações e UX
  - [ ] 6.4.2.1 Validar formulários no frontend (HTML5)
  - [ ] 6.4.2.2 Melhorar mensagens de erro
  - [ ] 6.4.2.3 Adicionar loading states (opcional)
  - [ ] 6.4.2.4 Confirmar exclusões com modal ou página

---

### Sprint 7: Testes e Documentação (Final)

#### 7.1 Testes Unitários

- [ ] **7.1.1** Testes de Models
  - [ ] 7.1.1.1 Testes para User model
  - [ ] 7.1.1.2 Testes para Account model
  - [ ] 7.1.1.3 Testes para Category model
  - [ ] 7.1.1.4 Testes para Transaction model

- [ ] **7.1.2** Testes de Views
  - [ ] 7.1.2.1 Testes de autenticação
  - [ ] 7.1.2.2 Testes de CRUD de contas
  - [ ] 7.1.2.3 Testes de CRUD de categorias
  - [ ] 7.1.2.4 Testes de CRUD de transações
  - [ ] 7.1.2.5 Testes de permissões (usuário só vê seus dados)

- [ ] **7.1.3** Testes de Formulários
  - [ ] 7.1.3.1 Testes de validação de UserRegistrationForm
  - [ ] 7.1.3.2 Testes de AccountForm
  - [ ] 7.1.3.3 Testes de CategoryForm
  - [ ] 7.1.3.4 Testes de TransactionForm

#### 7.2 Documentação

- [ ] **7.2.1** README.md
  - [ ] 7.2.1.1 Descrição do projeto
  - [ ] 7.2.1.2 Requisitos de sistema
  - [ ] 7.2.1.3 Instruções de instalação
  - [ ] 7.2.1.4 Instruções de execução
  - [ ] 7.2.1.5 Estrutura do projeto
  - [ ] 7.2.1.6 Screenshots (opcional)

- [ ] **7.2.2** Comentários no código
  - [ ] 7.2.2.1 Documentar models com docstrings
  - [ ] 7.2.2.2 Documentar views complexas
  - [ ] 7.2.2.3 Documentar funções utilitárias

#### 7.3 Preparação para Deploy (Opcional)

- [ ] **7.3.1** Configurações de produção
  - [ ] 7.3.1.1 Separar settings de dev e prod
  - [ ] 7.3.1.2 Configurar variáveis de ambiente
  - [ ] 7.3.1.3 Configurar ALLOWED_HOSTS
  - [ ] 7.3.1.4 Desabilitar DEBUG em produção
  - [ ] 7.3.1.5 Configurar coleta de arquivos estáticos

- [ ] **7.3.2** Docker (Sprint Final)
  - [ ] 7.3.2.1 Criar Dockerfile
  - [ ] 7.3.2.2 Criar docker-compose.yml
  - [ ] 7.3.2.3 Configurar volumes para dados persistentes
  - [ ] 7.3.2.4 Documentar uso do Docker

---
