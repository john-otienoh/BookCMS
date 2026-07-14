# Commands

Complete consolidated list of all commands mentioned throughout the entire BookShelf CMS implementation (Chapters 1‑5), including environment setup, package management, Django management, Docker, and OAuth configuration.

---

### Virtual Environment & Package Management

```bash
# Create virtual environment
python -m venv bookshelf_env

# Activate (Linux/macOS)
source bookshelf_env/bin/activate
# Activate (Windows)
.\bookshelf_env\Scripts\activate

# Install dependencies
python -m pip install Django~=5.2
python -m pip install python-decouple==3.8
python -m pip install django-taggit==5.0.1
python -m pip install markdown==3.6
python -m pip install psycopg==3.1.18
python -m pip install Pillow==11.0.0
python -m pip install social-auth-app-django==5.4.0
python -m pip install django-extensions==3.2.3
python -m pip install werkzeug==3.0.2
python -m pip install pyOpenSSL==24.1.0
```

---

### Django Project & App Management

```bash
# Create project
django-admin startproject bookshelf

# Create apps
python manage.py startapp catalog
python manage.py startapp accounts

# Database migrations
python manage.py makemigrations catalog
python manage.py makemigrations accounts
python manage.py makemigrations --name=trigram_ext --empty catalog   # for trigram extension
python manage.py migrate
python manage.py sqlmigrate catalog 0001   # inspect SQL

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run with HTTPS (for social auth testing)
python manage.py runserver_plus --cert-file cert.crt
```

---

### Shell / Interactive (ORM & Email Testing)

```bash
python manage.py shell
```

Inside the shell:

```python
from catalog.models import Book
from django.core.mail import send_mail

Book.published.all()
Book.published.count()
Book.objects.filter(title__search='dune')
send_mail('Test', 'Hello from BookShelf', None, ['you@gmail.com'], fail_silently=False)

# taggit
book = Book.objects.get(id=1)
book.tags.add('sci-fi', 'space-opera', 'classic')
book.tags.all()
book.tags.remove('classic')

# Trigram testing etc.
```

---

### Data Dump & Load (SQLite → PostgreSQL)

```bash
# Dump current data
python manage.py dumpdata --indent=2 --output=bookshelf_data.json

# Load into new database
python manage.py loaddata bookshelf_data.json
```

---

### Docker (PostgreSQL)

```bash
docker pull postgres:16.2
docker run --name=bookshelf_db -e POSTGRES_DB=bookshelf \
  -e POSTGRES_USER=bookshelf -e POSTGRES_PASSWORD=xxxxx \
  -p 5432:5432 -d postgres:16.2
```

---

### Environment File Example (`.env`)

```env
DB_NAME=bookshelf
DB_USER=bookshelf
DB_PASSWORD=xxxxx
DB_HOST=localhost
EMAIL_HOST_USER=you@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=BookShelf CMS <you@gmail.com>
GOOGLE_OAUTH2_KEY=your-google-client-id
GOOGLE_OAUTH2_SECRET=your-google-client-secret
```

---

### Google Cloud Console (OAuth2)

- Create project “BookShelf CMS”
- Enable Google+ API / People API
- OAuth consent screen: External, add test users
- Credentials → Create OAuth client ID (Web application)
- Authorized JavaScript origins: `http://localhost:8000`
- Authorized redirect URIs: `http://localhost:8000/accounts/social-auth/complete/google-oauth2/`

---

### Local Domain for HTTPS Testing (Optional)

Edit `/etc/hosts` (Linux/macOS) or `C:\Windows\System32\drivers\etc\hosts` (Windows):

```
127.0.0.1   bookshelfcms.test
```

Then access: `https://bookshelfcms.test:8000/`

---