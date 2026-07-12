# BookShelf CMS

A full‑featured book catalogue application built with Django, following the **"Django 5 by Example"** book (Chapters 1–4).  
It replaces the blog example with a dedicated **BookShelf CMS** – manage books, tag them, accept reader reviews, share via email, and benefit from powerful PostgreSQL full‑text search.  
With Chapter 4, the platform now includes a **complete user account system** with email verification, profile management, and media file uploads.

---

## Features (Chapters 1‑4)

### Chapter 1 – Core Application
- **Book model** with title, slug, synopsis, publish date, status (Draft/Published) and a many‑to‑one relationship to the cataloger (`added_by`).
- **Custom manager** (`PublishedManager`) to easily retrieve only published books.
- **Admin interface** with customised list display, filters, search, prepopulated slug, raw‑id fields and date hierarchy navigation.
- **Function‑based views** for listing published books and displaying book details.
- **Basic templates** (Bootstrap‑free) – later upgraded throughout the chapters.

### Chapter 2 – Enhancing the Blog
- **SEO‑friendly canonical URLs** using `get_absolute_url()`.
- **slug‑based detail URLs**: `/catalog/some-book-slug/`.
- **Pagination** with graceful handling of invalid page numbers.
- **Class‑based list view** (`BookListView`) as an alternative, with a reusable pagination template.
- **Email sharing** (`EmailBookForm`) – send a book recommendation to a friend. Email configuration via environment variables; fallback to console backend for development.
- **Review system** (`Review` model, `ReviewForm`) – readers can leave reviews for books, with admin moderation (`active` flag).

### Chapter 3 – Extending the Application
- **Tagging** with `django-taggit`: free‑form tags on books, tag‑filtered list pages (`/catalog/tag/sci-fi/`).
- **Similar books** based on shared tags, sorted by tag overlap and recency.
- **Custom template tags & filters**:
  - `total_books` – total count of published books.
  - `show_latest_books` – latest 3 (or custom number) books in the sidebar.
  - `get_most_reviewed_books` – most reviewed books.
  - `markdown` filter – renders Markdown content safely in templates.
- **Sitemap** (`/sitemap.xml`) with all published books.
- **RSS Feed** (`/catalog/feed/`) – the five most recently published books.
- **Full‑text search** powered by PostgreSQL:
  - Weighted ranking (title weight A, synopsis weight B).
  - Stemming and stop‑word removal.
  - Trigram similarity fallback for typo‑tolerant title search.
- **Database migration** from SQLite to PostgreSQL (Docker container setup + data dump/load).

### Chapter 4 – User Accounts & Profiles
- **User registration** with email verification:
  - Sign‑up form (username, email, password).
  - Email containing a **6‑digit OTP** and a one‑click **magic link**.
  - Account remains inactive until verified.
- **Email‑based login**: authenticate with email and password instead of username.
- **Logout** functionality.
- **Password change** and **password reset** (via email) using Django’s built‑in views.
- **User profile** with editable fields:
  - First name, last name, bio, phone number.
  - **Avatar** (profile picture) – file uploads stored in `media/avatars/`.
- **Media file handling**: configuration for user‑uploaded files.
- **Custom authentication backend** (`accounts.backends.EmailBackend`) that allows login with email.
- **Account signal**: a `user_verified` signal ensures a `Profile` object is created automatically when the email is verified.

---

## Prerequisites

- Python 3.12+
- PostgreSQL (recommended) or SQLite for local development
- (Optional) Docker – to run PostgreSQL if you don’t have a local instance

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/john-otienoh/BookCMS
   cd BookCMS
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```
   Django~=5.2
   python-decouple==3.8
   django-taggit==5.0.1
   markdown==3.6
   psycopg[binary]==3.1.18
   Pillow   # for image uploads (avatar)
   ```

4. **Environment variables** – create a `.env` file in the project root (next to `manage.py`):
   ```
   # Database (leave empty to use SQLite, or set for PostgreSQL)
   DB_NAME=bookshelf
   DB_USER=bookshelf
   DB_PASSWORD=your_password
   DB_HOST=localhost

   # Email settings (required for verification emails & password reset)
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   DEFAULT_FROM_EMAIL=BookShelf CMS <your_email@gmail.com>
   ```

   For local development without SMTP, the project will automatically use the **console email backend** if the email variables are missing. However, to test the full verification flow, provide real SMTP credentials or use a service like Mailtrap.

5. **Database configuration**
   - By default, `settings.py` uses **PostgreSQL** and reads from the `.env` file.
   - If you want to use SQLite (for quick tests), comment out the PostgreSQL configuration and use:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
     ```
   - To run PostgreSQL using Docker (optional):
     ```bash
     docker run --name=bookshelf_db -e POSTGRES_DB=bookshelf \
       -e POSTGRES_USER=bookshelf -e POSTGRES_PASSWORD=your_password \
       -p 5432:5432 -d postgres:16.2
     ```

6. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **(Optional) Load sample data**
   If you have a fixture file `bookshelf_data.json`:
   ```bash
   python manage.py loaddata bookshelf_data.json
   ```

9. **Media files (avatars)**
   Ensure your `settings.py` contains the following media configuration (already set up in the project):
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```
   During development, add this to your project’s `urls.py`:
   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       # ... my URL patterns
   ]
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

---

## Running the Development Server

```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/catalog/** to browse published books.  
User account pages are under **http://127.0.0.1:8000/accounts/**.

---

## Admin Interface

Go to **http://127.0.0.1:8000/admin/** and log in with your superuser credentials.  
The admin offers:
- **Books** with facet counts, search, date hierarchy, and prepopulated slug.
- **Reviews** with moderation (active/inactive).
- **Tags** (via django‑taggit).
- **Sites** (required for sitemap generation – set domain to `localhost:8000`).
- **Email OTPs** – admin can inspect verification tokens (read‑only).
- **Profiles** – manage user bio, phone, avatar.

---

## URL Patterns Overview

| URL                                      | Purpose                                     |
|------------------------------------------|---------------------------------------------|
| `/catalog/`                              | Paginated list of published books           |
| `/catalog/tag/<slug:tag_slug>/`          | Books filtered by tag                       |
| `/catalog/<slug:book>/`                  | Book detail (SEO‑friendly)                  |
| `/catalog/<int:id>/share/`               | Share a book via email                      |
| `/catalog/<int:id>/review/`              | Submit a review (POST only)                 |
| `/catalog/search/`                       | Full‑text search                            |
| `/catalog/feed/`                         | RSS feed of latest books                    |
| `/sitemap.xml`                           | Sitemap index                               |
| `/admin/`                                | Django admin                                |
| **Accounts**                             |                                             |
| `/accounts/register/`                    | Create a new account                        |
| `/accounts/register/done/`               | After sign‑up – prompt to check email       |
| `/accounts/register/confirm/`            | Enter OTP to verify email                   |
| `/accounts/register/confirm/<uidb64>/<token>/` | Magic‑link verification               |
| `/accounts/register/resend/`             | Resend verification code                    |
| `/accounts/login/`                       | Email‑based login                           |
| `/accounts/logout/`                      | Sign out                                    |
| `/accounts/profile/`                     | View your profile                           |
| `/accounts/profile/edit/`                | Edit profile (name, bio, phone, avatar)     |
| `/accounts/password-change/`             | Change password (authenticated)             |
| `/accounts/password-reset/`              | Request password reset email                |
| `/accounts/password-reset/done/`         | After reset email sent                      |
| `/accounts/password-reset/<uidb64>/<token>/` | Set new password (from email)           |
| `/accounts/password-reset/complete/`     | Password reset successful                   |

---

## Project Structure

```
bookshelf/                    # Django project folder
├── docker-compose.yml
├── Dockerfile
├── do.sh
├── README.md
├── pyproject.toml
├── manage.py
├── requirements.txt
├── .env                      # environment variables (gitignored)
├── bookshelf/                # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── catalog/                  # main catalogue application
│   ├── models.py             # Book, Review
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   ├── feeds.py
│   ├── sitemaps.py
│   ├── templatetags/
│   ├── migrations/
│   └── templates/
├── accounts/                 
│   ├── models.py
│   ├── views.py             
│   ├── forms.py    
│   ├── backends.py
│   ├── signals.py
│   ├── admin.py
│   ├── urls.py
│   ├── apps.py              
│   ├── migrations/
│   └── templates/
│       ├── accounts/
│       │   ├── register.html
│       │   ├── register_done.html
│       │   ├── register_confirm.html
│       │   ├── login.html
│       │   ├── logout.html
│       │   ├── profile.html
│       │   ├── profile_edit.html
│       │   └── email/
│       │       └── verification_email.txt
│       └── registration/     # password‑reset templates
│           ├── password_change_form.html
│           ├── password_change_done.html
│           ├── password_reset_form.html
│           ├── password_reset_confirm.html
│           ├── password_reset_done.html
│           ├── password_reset_email.html
│           └── password_reset_complete.html
└── media/                    # uploaded files (e.g., avatars/)
    └── avatars/
```

---

## Custom Template Tags & Filters

Load them with `{% load catalog_tags %}` in any template.

- **`{% total_books %}`** – shows the total number of published books.
- **`{% show_latest_books 3 %}`** – renders a list of the 3 latest published books.
- **`{% get_most_reviewed_books as most_reviewed %}`** – retrieves the most reviewed books.
- **`{{ content|markdown }}`** – converts Markdown text to safe HTML.

---

## Search Functionality

The search page (`/catalog/search/?query=...`) uses PostgreSQL full‑text search with:
- **Weighted ranking** – title matches (weight A) are more important than synopsis matches (weight B).
- **Rank threshold** – only results with `rank >= 0.3` are shown.
- **Trigram similarity fallback** – if no full‑text results are found, the search will try to match misspelled titles using `TrigramSimilarity`.  
  (Requires the `pg_trgm` extension – automatically installed via migration `0005_trigram_ext`).

---

## Email Verification Flow

1. User fills out the registration form (`/accounts/register/`).
2. An email is sent with a 6‑digit code and a unique magic link.
3. The user must either:
   - Enter the code on the verification page (`/accounts/register/confirm/`), or
   - Click the magic link, which automatically verifies the account.
4. Once verified, the account is activated, a `Profile` is created, and the user is logged in automatically.
5. The code and link expire after 15 minutes. Users can request a new code if needed.

---

## Data Migration (SQLite → PostgreSQL)

If you started with SQLite and later switched to PostgreSQL, follow these steps:

1. Dump the SQLite data:
   ```bash
   python manage.py dumpdata --indent=2 --output=bookshelf_data.json
   ```
2. Switch the database settings in `settings.py` and `.env`.
3. Apply migrations on the new PostgreSQL database.
4. Load the data:
   ```bash
   python manage.py loaddata bookshelf_data.json
   ```

---

## Technologies Used

- **Backend**: Django 5.2, Python 3.12+
- **Database**: PostgreSQL 16 (with `psycopg` 3 driver) or SQLite
- **Templating**: Django templates + Tailwind CSS (premium UI kit)
- **Tagging**: django‑taggit
- **Markdown**: Python‑Markdown library
- **Email**: SMTP or console backend (via python‑decouple)
- **Search**: PostgreSQL full‑text search + trigram similarity
- **User authentication**: Custom email‑based backend, OTP & magic‑link verification
- **Image handling**: Pillow for avatar uploads
- **Additional**: Docker (optional), python‑decouple for configuration

---

## License

This project is for educational purposes based on the book **"Django 5 by Example"**.  
Feel free to use, modify, and extend it.

---

## Acknowledgements

- Book: **Django 5 by Example** by Antonio Melé (Packt Publishing)
- The Django community and all open‑source libraries used.

---

**Happy cataloguing! 📚**
```
