Contents
1. Building a Blog Application
Installing Python
Creating a Python virtual environment
Installing Django
Installing Django with pip
Django overview
Main framework components
The Django architecture
New features in Django 5
Creating your first project
Applying initial database migrations
Running the development server
Project settings
Projects and applications
Creating an application
Creating the blog data models
Creating the Post model
Adding datetime fields
Defining a default sort order
Adding a database index
Activating the application
Adding a status field
Adding a many-to-one relationship
Creating and applying migrations
Creating an administration site for models
Creating a superuser
The Django administration site
Adding models to the administration site
Customizing how models are displayed
Adding facet counts to filters
Working with QuerySets and managers
Creating objects
Updating objects
Retrieving objects
Filtering objects
Using field lookups
Chaining filters
Excluding objects
Ordering objects
Limiting QuerySets
Counting objects
Checking if an object exists
Deleting objects
Complex lookups with Q objects
When QuerySets are evaluated
More on QuerySets
Creating model managers
Building list and detail views
Creating list and detail views
Using the get_object_or_404 shortcut
Adding URL patterns for your views
Creating templates for your views
Creating a base template
Creating the post list template
Accessing our application
Creating the post detail template
The request/response cycle
Management commands used in this chapter


2. Enhancing Your Blog and Adding Social Features

Using canonical URLs for models
Creating SEO-friendly URLs for posts
Modifying the URL patterns
Modifying the views
Modifying the canonical URL for posts
Adding pagination
Adding pagination to the post list view
Creating a pagination template
Handling pagination errors
Building class-based views
Why use class-based views
Using a class-based view to list posts
Recommending posts by email
Creating forms with Django
Handling forms in views
Sending emails with Django
Working with environment variables
Sending emails in views
Rendering forms in templates
Creating a comment system
Creating a model for comments
Adding comments to the administration site
Creating forms from models
Handling ModelForms in views
Creating templates for the comment form
Adding comments to the post detail view
Adding comments to the post detail template
Using simplified templates for form rendering


3. Extending Your Blog Application

Implementing tagging with django-taggit
Retrieving posts by similarity
Creating custom template tags and filters
Implementing custom template tags
Creating a simple template tag
Creating an inclusion template tag
Creating a template tag that returns a QuerySet
Implementing custom template filters
Creating a template filter to support Markdown syntax
Adding a sitemap to the site
Creating feeds for blog posts
Adding full-text search to the blog
Installing Docker
Installing PostgreSQL
Dumping the existing data
Switching the database in the project
Loading the data into the new database
Simple search lookups
Searching against multiple fields
Building a search view
Stemming and ranking results
Stemming and removing stop words in different languages
Weighting queries
Searching with trigram similarity


4. Building a Social Website

Creating a social website project
Starting the social website project
Using the Django authentication framework
Creating a login view
Using Django’s built-in authentication views
Login and logout views
Change password views
Reset password views
User registration and user profiles
User registration
Extending the user model
Installing Pillow and serving media files
Creating migrations for the profile model
Using a custom user model


5. Implementing Social Authentication

Technical requirements
Using the messages framework
Building a custom authentication backend
Preventing users from using an existing email address
Adding social authentication to your site
Running the development server through HTTPS
Authentication using Google
Creating a profile for users that register with social
authentication


6. Sharing Content on Your Website

Creating an image bookmarking website
Building the image model
Creating many-to-many relationships
Registering the image model in the administration site
Posting content from other websites
Cleaning form fields
Installing the Requests library
Overriding the save() method of a ModelForm
Building a bookmarklet with JavaScript
Creating a detail view for images
Creating image thumbnails using easy-thumbnails
Adding asynchronous actions with JavaScript
Loading JavaScript on the DOM
Cross-site request forgery for HTTP requests in JavaScript
Performing HTTP requests with JavaScript
Adding infinite scroll pagination to the image list


7. Tracking User Actions

Building a follow system
Creating many-to-many relationships with an intermediate model
Creating list and detail views for user profiles
Adding user follow/unfollow actions with JavaScript
Creating an activity stream application
Using the contenttypes framework
Adding generic relations to your models
Avoiding duplicate actions in the activity stream
Adding user actions to the activity stream
Displaying the activity stream
Optimizing QuerySets that involve related objects
Using select_related()
Using prefetch_related()
Creating templates for actions
Using signals for denormalizing counts
Working with signals
Application configuration classes
Using Django Debug Toolbar
Installing Django Debug Toolbar
Django Debug Toolbar panels
Django Debug Toolbar commands
Counting image views with Redis
Installing Redis
Using Redis with Python
Storing image views in Redis
Storing a ranking in Redis
Next steps with Redis


8. Building an Online Shop

Creating an online shop project
Creating product catalog models
Registering catalog models on the administration site
Building catalog views
Creating catalog templates
Building a shopping cart
Using Django sessions
Session settings
Session expiration
Storing shopping carts in sessions
Creating shopping cart views
Adding items to the cart
Building a template to display the cart
Adding products to the cart
Updating product quantities in the cart
Creating a context processor for the current cart
Context processors
Setting the cart in the request context
Registering customer orders
Creating order models
Including order models in the administration site
Creating customer orders
Creating asynchronous tasks
Working with asynchronous tasks
Workers, message queues, and message brokers
Using Django with Celery and RabbitMQ
Monitoring Celery with Flower


9. Managing Payments and Orders

Integrating a payment gateway
Creating a Stripe account
Installing the Stripe Python library
Adding Stripe to your project
Building the payment process
Integrating Stripe Checkout
Testing the checkout process
Using test credit cards
Checking the payment information in the Stripe
dashboard
Using webhooks to receive payment notifications
Creating a webhook endpoint
Testing webhook notifications
Referencing Stripe payments in orders
Going live
Exporting orders to CSV files
Adding custom actions to the administration site
Extending the administration site with custom views
Generating PDF invoices dynamically
Installing WeasyPrint
Creating a PDF template
Rendering PDF files
Sending PDF files by email


10. Extending Your Shop

Creating a coupon system
Building the coupon model
Applying a coupon to the shopping cart
Applying coupons to orders
Creating coupons for Stripe Checkout
Adding coupons to orders on the administration site and to
PDF invoices
Building a recommendation engine
Recommending products based on previous purchases


11. Adding Internationalization to Your Shop

Internationalization with Django
Internationalization and localization settings
Internationalization management commands
Installing the gettext toolkit
How to add translations to a Django project
How Django determines the current language
Preparing your project for internationalization
Translating Python code
Standard translations
Lazy translations
Translations including variables
Plural forms in translations
Translating your own code
Translating templates
The {% translate %} template tag
The {% blocktranslate %} template tag
Translating the shop templates
Using the Rosetta translation interface
Fuzzy translations
URL patterns for internationalization
Adding a language prefix to URL patterns
Translating URL patterns
Allowing users to switch language
Translating models with django-parler
Installing django-parler
Translating model fields
Integrating translations into the administration site
Creating migrations for model translations
Using translations in QuerySets
Adapting views for translations
Format localization
Using django-localflavor to validate form fields
Expanding your project using AI


12. Building an E-Learning Platform

Setting up the e-learning project
Serving media files
Building the course models
Registering the models in the administration site
Using fixtures to provide initial data for models
Creating models for polymorphic content
Using model inheritance
Abstract models
Multi-table model inheritance
Proxy models
Creating the Content models
Creating custom model fields
Adding ordering to Module and Content objects
Adding authentication views
Adding an authentication system
Creating the authentication templates



13. Creating a Content Management System

Creating a CMS
Creating class-based views
Using mixins for class-based views
Working with groups and permissions
Restricting access to class-based views
Managing course modules and their contents
Using formsets for course modules
Adding content to course modules
Managing modules and their contents
Reordering modules and their contents
Using mixins from django-braces


14. Rendering and Caching Content

Displaying the catalog of courses
Adding student registration
Creating a student registration view
Enrolling in courses
Rendering course contents
Accessing course contents
Rendering different types of content
Using the cache framework
Available cache backends
Installing Memcached
Installing the Memcached Docker image
Installing the Memcached Python binding
Django cache settings
Adding Memcached to your project
Cache levels
Using the low-level cache API
Checking cache requests with Django Debug Toolbar
Low-level caching based on dynamic data
Caching template fragments
Caching views
Using the per-site cache
Using the Redis cache backend
Monitoring Redis with Django Redisboard


15. Building an API

Building a RESTful API
Installing Django REST framework
Defining serializers
Understanding parsers and renderers
Building list and detail views
Consuming the API
Extending serializers
Adding additional fields to serializers
Implementing serializer method fields
Adding pagination to views
Building the course serializer
Serializing relations
Creating nested serializers
Creating ViewSets and routers
Building custom API views
Handling authentication
Implementing basic authentication
Adding permissions to views
Adding additional actions to ViewSets
Creating custom permissions
Serializing course contents
Consuming the RESTful API


16. Building a Chat Server

Creating a chat application
Implementing the chat room view
Real-time Django with Channels
Asynchronous applications using ASGI
The request/response cycle using Channels
Installing Channels and Daphne
Writing a consumer
Routing
Implementing the WebSocket client
Enabling a channel layer
Channels and groups
Setting up a channel layer with Redis
Updating the consumer to broadcast messages
Adding context to the messages
Modifying the consumer to be fully asynchronous
Persisting messages into the database
Creating a model for chat messages
Adding the message model to the administration site
Storing messages in the database
Displaying the chat history
Integrating the chat application with existing views


17. Going Live
Creating a production environment
Managing settings for multiple environments
Local environment settings
Running the local environment
Production environment settings
Using Docker Compose
Installing Docker Compose via Docker Desktop
Creating a Dockerfile
Adding the Python requirements
Creating a Docker Compose file
Configuring the PostgreSQL service
Applying database migrations and creating a superuser
Configuring the Redis service
Serving Django through WSGI and NGINX
Using uWSGI
Configuring uWSGI
Using NGINX
Configuring NGINX
Using a hostname
Serving static and media assets
Collecting static files
Serving static files with NGINX
Securing your site with SSL/TLS
Checking your project for production
Configuring your Django project for SSL/TLS
Creating an SSL/TLS certificate
Configuring NGINX to use SSL/TLS
Redirecting HTTP traffic over to HTTPS
Configuring Daphne for Django Channels
Using secure connections for WebSockets
Including Daphne in the NGINX configuration
Creating a custom middleware
Creating subdomain middleware
Serving multiple subdomains with NGINX
Implementing custom management commands

Here’s a detailed mapping of each of the three proposed projects to the exact subtopics from *Django 5 by Example*. Every bullet in the book’s table of contents is accounted for, adapted to the specific domain of the platform.

---

## Project 1: All‑in‑One Community Platform for Creators
*(Patreon/Substack clone – articles, paid subscriptions, courses, chat)*

### 1. Building a Blog Application → Creator Article System
- **Installing Python, virtualenv, Django, pip** – Project bootstrap.
- **Creating a virtual environment, installing Django** – Standard.
- **Django overview, main framework components, architecture, new features in Django 5** – Applied throughout.
- **Creating your first project, applying initial database migrations, running the development server** – Initial setup.
- **Project settings, projects and applications** – Config and `blog` app.
- **Creating an application** – `articles` app.
- **Creating the blog data models (Post model, datetime fields, default sort order, database index)** – `Article` model with `title`, `body`, `publish`, `status`, `author`. Indexes on publish date and status.
- **Activating the application, adding a status field, adding a many-to-one relationship** – Status (draft/published/locked), relationship to creator (User).
- **Creating and applying migrations** – Migrations for all article-related models.
- **Creating an administration site for models, superuser, adding models to admin, customizing display, facet counts** – Admin for articles with filters by creator, status; facet counts on tags.
- **Working with QuerySets and managers (create, update, retrieve, filter, field lookups, chaining, exclude, order, limit, count, exists, delete, Q objects, evaluation, custom managers)** – `Article.published` manager, complex search with Q objects across title/body.
- **Building list and detail views, `get_object_or_404`** – Public feed (list) and full article (detail), locked content gated.
- **Adding URL patterns for views** – `/creators/<username>/articles/`, `/articles/<slug>/`.
- **Creating templates (base, post list, post detail)** – Base template with creator branding, article list, article detail.
- **The request/response cycle** – Standard.
- **Management commands used in this chapter** – Basic commands.

### 2. Enhancing Your Blog and Adding Social Features → Community Engagement
- **Using canonical URLs for models** – `get_absolute_url()` on Article.
- **Creating SEO-friendly URLs for posts** – Slug field in URL.
- **Modifying URL patterns, views** – Updated to use canonical URLs.
- **Adding pagination** – Article list paginated; error handling.
- **Building class-based views** – `ArticleListView`, `ArticleDetailView`.
- **Recommending posts by email** – “Share article with subscriber” via email form; Django forms, send_mail, env vars.
- **Sending emails in views** – Invitation / share emails.
- **Rendering forms in templates** – Share modal.
- **Comment system** – `Comment` model linked to `Article`, ModelForm, admin, templates, simplified form rendering.

### 3. Extending Your Blog Application → Discoverability & Search
- **Implementing tagging with django-taggit** – Tag articles (e.g., “Python”, “Design”).
- **Retrieving posts by similarity** – Related articles based on shared tags.
- **Custom template tags and filters** – Inclusion tags for “related posts”, custom filter for Markdown rendering.
- **Creating a simple template tag, inclusion tag, QuerySet-returning tag** – For trending articles, subscription CTAs.
- **Implementing custom template filters (Markdown)** – Markdown-to-HTML filter.
- **Adding a sitemap to the site** – `ArticleSitemap` for SEO.
- **Creating feeds for blog posts** – RSS/Atom feeds per creator.
- **Installing Docker, PostgreSQL** – Local dev with Docker Compose.
- **Dumping existing data, switching database, loading data** – Migrate from SQLite to PostgreSQL.
- **Simple search lookups, searching against multiple fields** – SearchVector on title, body.
- **Building a search view** – Full-text search with ranking, trigram similarity for “did you mean”.
- **Stemming and ranking, weighting queries, trigram similarity** – Advanced PostgreSQL full-text search with language stemming.

### 4. Building a Social Website → User Profiles & Subscriptions
- **Starting the social website project** – Integrated in the platform.
- **Using the Django authentication framework** – All auth features.
- **Creating a login view, using built-in auth views (login/logout, change password, reset password)** – Standard.
- **User registration, extending the user model** – Custom `Profile` with bio, social links, avatar (Pillow).
- **Installing Pillow and serving media files** – Avatar handling.
- **Creating migrations for the profile model** – Profile migration.
- **Using a custom user model** – Email-based custom User model.

### 5. Implementing Social Authentication → Third‑Party Login
- **Using the messages framework** – Success/error messages.
- **Building a custom authentication backend** – Allow login via email or username.
- **Preventing users from using an existing email address** – Validation.
- **Adding social authentication to your site** – Google OAuth via `social-auth-app-django`.
- **Running the development server through HTTPS** – For OAuth callbacks.
- **Authentication using Google** – “Sign in with Google” button.
- **Creating a profile for users that register with social authentication** – Auto-create Profile on first social login.

### 6. Sharing Content on Your Website → Asset Sharing & Bookmarking
- **Creating an image bookmarking website** – Creators and subscribers can share images, links.
- **Building the image model** – `SavedItem` (image URL, description, uploaded file).
- **Creating many-to-many relationships** – Users can save items to collections.
- **Registering the image model in the administration site** – Admin for saved items.
- **Posting content from other websites** – Bookmarklet to capture a webpage; Requests to fetch metadata.
- **Cleaning form fields, overriding save() of ModelForm** – Clean URL, auto-populate title.
- **Building a bookmarklet with JavaScript** – Drag-and-drop bookmarklet.
- **Creating a detail view for images** – Saved item detail.
- **Creating image thumbnails using easy-thumbnails** – Thumbnails for images.
- **Adding asynchronous actions with JavaScript, loading JavaScript on the DOM, CSRF for JS, performing HTTP requests with JavaScript** – AJAX save/unsave, like.
- **Adding infinite scroll pagination to the image list** – Saved items gallery with infinite scroll.

### 7. Tracking User Actions → Activity Feed & Analytics
- **Building a follow system** – Follow creators (intermediate model).
- **Creating many-to-many relationships with an intermediate model** – Follow model with timestamps.
- **Creating list and detail views for user profiles** – Public creator profile.
- **Adding user follow/unfollow actions with JavaScript** – AJAX toggle.
- **Creating an activity stream application** – `Action` model using contenttypes framework.
- **Using the contenttypes framework** – GenericForeignKey to Article, Comment, SavedItem.
- **Adding generic relations to your models** – Activity stream feeds.
- **Avoiding duplicate actions in the activity stream** – Merge/update logic.
- **Adding user actions to the activity stream** – On post, comment, follow, save.
- **Displaying the activity stream** – Dashboard “What’s new” feed.
- **Optimizing QuerySets with select_related() and prefetch_related()** – For activity feed.
- **Creating templates for actions** – Action rendering template.
- **Using signals for denormalizing counts** – Article likes count, creator follower count.
- **Working with signals, application configuration classes** – Ready() in apps.py.
- **Using Django Debug Toolbar** – Development profiling.
- **Installing Redis, using Redis with Python, storing image views in Redis, storing a ranking in Redis** – Trending articles, popular saved items, view counts.

### 8. Building an Online Shop → Digital Products & Subscription Tiers
- **Creating an online shop project** – Shop module.
- **Creating product catalog models** – `Tier` (subscription plan) and `DigitalProduct` (e-book, template).
- **Registering catalog models on the administration site** – Admin management.
- **Building catalog views, templates** – Subscription plans page, product listing.
- **Building a shopping cart** – Using Django sessions.
- **Session settings, expiration** – Configure session duration.
- **Storing shopping carts in sessions** – Cart data in session.
- **Creating shopping cart views (add, update, remove)** – Add to cart, update quantity.
- **Adding items to the cart, updating quantities** – Views.
- **Building a template to display the cart** – Cart summary page.
- **Creating a context processor for the current cart** – Cart available in all templates.
- **Registering customer orders** – `Order` model.
- **Including order models in the administration site** – Order management.
- **Creating customer orders** – Checkout process.
- **Creating asynchronous tasks** – Celery and RabbitMQ setup.
- **Working with asynchronous tasks, workers, message queues, brokers** – Send welcome email, process files.
- **Using Django with Celery and RabbitMQ** – Configured in project.
- **Monitoring Celery with Flower** – Task monitoring.

### 9. Managing Payments and Orders → Stripe Subscriptions & Billing
- **Integrating a payment gateway, creating a Stripe account, installing Stripe Python library, adding Stripe to your project** – Stripe integration.
- **Building the payment process** – Subscription checkout via Stripe Checkout.
- **Testing the checkout process, using test credit cards, checking payment information in Stripe dashboard** – Testing.
- **Using webhooks to receive payment notifications** – Stripe webhooks for subscription creation, renewal, cancellation.
- **Creating a webhook endpoint, testing webhook notifications** – Endpoint view.
- **Referencing Stripe payments in orders** – Store Stripe subscription ID, payment intent.
- **Going live** – Production keys.
- **Exporting orders to CSV files** – Admin action for billing export.
- **Adding custom actions to the administration site** – Refund, cancel subscription.
- **Extending the administration site with custom views** – Revenue dashboard.
- **Generating PDF invoices dynamically** – WeasyPrint invoice generation.
- **Rendering PDF files** – PDF view.
- **Sending PDF files by email** – Email invoice on successful payment.

### 10. Extending Your Shop → Coupons & Recommendations
- **Creating a coupon system** – `Coupon` model for discount on subscriptions.
- **Building the coupon model, applying a coupon to the shopping cart, applying coupons to orders** – Coupon validation at checkout.
- **Creating coupons for Stripe Checkout** – Stripe promotion codes.
- **Adding coupons to orders on the administration site and to PDF invoices** – Display coupon.
- **Building a recommendation engine** – “Creators you might like” based on subscription history; “Other subscribers also bought” for digital products.

### 11. Adding Internationalization to Your Shop → Multi‑Language Platform
- **Internationalization with Django (settings, management commands, gettext toolkit, adding translations to a Django project, how Django determines current language)** – Full i18n setup.
- **Preparing project for internationalization** – Mark strings.
- **Translating Python code (standard, lazy, variables, plural forms)** – `ugettext_lazy` in models/views.
- **Translating templates (% translate, % blocktranslate)** – Template translation tags.
- **Translating the shop templates** – All user-facing templates translated.
- **Using the Rosetta translation interface** – Web-based translation.
- **Fuzzy translations** – Rosetta fuzzy matching.
- **URL patterns for internationalization (language prefix, translating URL patterns)** – `/en/articles/`, `/es/articles/` with `i18n_patterns`.
- **Allowing users to switch language** – Language switcher.
- **Translating models with django-parler** – Translated Article body, product descriptions.
- **Integrating translations into the administration site** – Admin for translated fields.
- **Creating migrations for model translations, using translations in QuerySets, adapting views** – django-parler integration.
- **Format localization, using django-localflavor to validate form fields** – Date/number formatting, local address fields.
- **Expanding your project using AI** – Optional AI-assisted translation/content generation.

### 12. Building an E‑Learning Platform → Creator Courses
- **Setting up the e‑learning project, serving media files** – Courses app.
- **Building the course models** – `Course`, `Module` models.
- **Registering the models in the administration site** – Course admin.
- **Using fixtures to provide initial data for models** – Sample course data.
- **Creating models for polymorphic content (model inheritance: abstract, multi-table, proxy)** – `Content` base, `Text`, `Video`, `File`, `Image` inherited models.
- **Creating the Content models** – As above.
- **Creating custom model fields** – `OrderField` for ordering content.
- **Adding ordering to Module and Content objects** – Ordering implementation.
- **Adding authentication views** – Restrict course access to paid subscribers.

### 13. Creating a Content Management System → Course Authoring
- **Creating a CMS, class-based views, using mixins for class-based views** – Course management views.
- **Working with groups and permissions** – Instructor group with permissions.
- **Restricting access to class-based views** – `LoginRequiredMixin`, `UserPassesTestMixin`.
- **Managing course modules and their contents** – Views for adding/editing modules.
- **Using formsets for course modules** – Django formsets to manage modules inline.
- **Adding content to course modules** – Content creation views.
- **Managing modules and their contents** – Full CRUD.
- **Reordering modules and their contents** – Drag-and-drop or up/down ordering.
- **Using mixins from django-braces** – `OrderableListMixin`, etc.

### 14. Rendering and Caching Content → Performance
- **Displaying the catalog of courses** – Public course listing.
- **Adding student registration** – Enrolment after subscription.
- **Creating a student registration view, enrolling in courses** – Enrolment logic.
- **Rendering course contents** – Student course view.
- **Accessing course contents, rendering different types of content** – Template rendering based on content type.
- **Using the cache framework** – Cache backends setup.
- **Installing Memcached, Docker image, Python binding, cache settings, adding Memcached** – Memcached for caching.
- **Cache levels, low-level cache API** – Cache expensive queries.
- **Checking cache requests with Django Debug Toolbar** – Dev profiling.
- **Low-level caching based on dynamic data** – Cache course page per user tier.
- **Caching template fragments** – “Popular courses” sidebar.
- **Caching views, per-site cache** – Cached course catalog.
- **Using the Redis cache backend** – Redis for caching.
- **Monitoring Redis with Django Redisboard** – Redis monitoring.

### 15. Building an API → Public API & Mobile Backend
- **Building a RESTful API, installing DRF, defining serializers, parsers/renderers** – DRF setup.
- **Building list and detail views** – Article list/detail API.
- **Consuming the API** – Test with curl/httpie.
- **Extending serializers, adding additional fields, implementing serializer method fields** – Article serializer with computed fields.
- **Adding pagination to views** – DRF pagination.
- **Building the course serializer, serializing relations, nested serializers** – Course with modules.
- **Creating ViewSets and routers** – Course, Article ViewSets.
- **Building custom API views** – Custom endpoint for trending.
- **Handling authentication, implementing basic authentication, adding permissions, additional actions, custom permissions** – JWT authentication, permissions per tier.
- **Serializing course contents** – Polymorphic content serialization.
- **Consuming the RESTful API** – For mobile app.

### 16. Building a Chat Server → Subscriber‑Only Live Chat
- **Creating a chat application** – `chat` app.
- **Implementing the chat room view** – Template view.
- **Real-time Django with Channels, asynchronous applications using ASGI, request/response cycle using Channels** – ASGI config.
- **Installing Channels and Daphne** – Install.
- **Writing a consumer, routing** – ChatConsumer for room messages.
- **Implementing the WebSocket client** – JS client.
- **Enabling a channel layer, channels and groups** – Group per creator’s chat room.
- **Setting up a channel layer with Redis** – Redis as channel backend.
- **Updating the consumer to broadcast messages** – Broadcasting to room group.
- **Adding context to the messages** – Sender username, avatar.
- **Modifying the consumer to be fully asynchronous** – Async consumer.
- **Persisting messages into the database** – ChatMessage model.
- **Adding the message model to the administration site** – Admin view.
- **Storing messages in the database** – Save on receive.
- **Displaying the chat history** – Load last 50 messages.
- **Integrating the chat application with existing views** – Embed chat on course page.

### 17. Going Live → Production Deployment
- **Creating a production environment, managing settings for multiple environments** – `settings/local.py`, `production.py`.
- **Local environment settings, running the local environment** – Docker Compose for dev.
- **Production environment settings, using Docker Compose** – Production stack.
- **Installing Docker Compose via Docker Desktop** – Setup.
- **Creating a Dockerfile, adding Python requirements** – Custom image.
- **Creating a Docker Compose file** – Services: web, db, redis, celery, nginx.
- **Configuring the PostgreSQL service** – Postgres container.
- **Applying database migrations and creating a superuser** – Startup commands.
- **Configuring the Redis service** – Redis container.
- **Serving Django through WSGI and NGINX** – Gunicorn or uWSGI + Nginx.
- **Using uWSGI, configuring uWSGI, using NGINX, configuring NGINX** – Nginx reverse proxy.
- **Using a hostname** – Domain setup.
- **Serving static and media assets, collecting static files, serving with NGINX** – Static/media handling.
- **Securing your site with SSL/TLS** – Let’s Encrypt.
- **Checking your project for production** – `manage.py check --deploy`.
- **Configuring your Django project for SSL/TLS, creating an SSL/TLS certificate, configuring NGINX to use SSL/TLS, redirecting HTTP to HTTPS** – Full HTTPS.
- **Configuring Daphne for Django Channels, using secure connections for WebSockets** – Daphne alongside WSGI, WSS.
- **Including Daphne in the NGINX configuration** – Nginx proxies WebSockets.
- **Creating a custom middleware** – Subdomain middleware to route `<creator>.platform.com` to their page.
- **Creating subdomain middleware** – Middleware to detect subdomain and set current creator.
- **Serving multiple subdomains with NGINX** – Wildcard SSL, Nginx config.
- **Implementing custom management commands** – `create_initial_tiers`, `populate_sample_data`.

The project maps directly and completely to every single subtopic in the *Django 5 by Example* table of contents, each offering a unique, production‑ready portfolio piece.