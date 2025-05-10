# Shadium API

Shadium API is a Django-based backend project that replicates the core functionalities of a social blogging platform like Medium. It supports multilingual content, user interactions (comments, claps, ratings, bookmarks), and advanced search capabilities using Elasticsearch. The system handles logic such as pricing, calculations, and content management based on the selected language.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Installation Instructions](#installation-instructions)
4. [Running the Project](#running-the-project)
5. [Languages & Translation Support](#languages--translation-support)
6. [Admin Panel Functionality](#admin-panel-functionality)
7. [Environment Variables](#environment-variables)
8. [Dependencies](#dependencies)
9. [Database](#database)
10. [Extra Notes](#extra-notes)

## Project Overview

Shadium API provides the following features:
- **Multilingual Support**: Content and logic adapt to the selected language.
- **User Interactions**: Users can clap, comment, rate, and bookmark posts.
- **Advanced Search**: Elasticsearch integration for efficient content discovery.
- **Admin Management**: Admins can manage users, posts, and system settings via a robust admin panel.

## Project Structure

### Apps and Core Components

- **`apps.account`**: Handles user authentication, profiles, and user management.
  - Models: `User`, `Profile`
  - Views: `RegisterUserView`, `LogoutView`, `ProfileViewSet`, `UserExploreViewSet`
  - Serializers: `UserSerializer`, `ProfileSerializer`
  - Admin: `UserAdmin`, `ProfileAdmin`

- **`apps.blog`**: Manages blog posts, comments, claps, ratings, and bookmarks.
  - Models: `Post`, `Comment`, `Clap`, `Rating`, `BookMark`
  - Views: `PostViewSet`, `CommentViewSet`, `ClapViewSet`, `RatingExploreViewSet`, `PostElasticSearchViewSet`
  - Serializers: `PostSerializer`, `CommentSerializer`, `ClapSerializer`, `RatingSerializer`
  - Admin: `PostAdmin`, `CommentAdmin`, `ClapAdmin`, `RatingAdmin`, `BookMarkAdmin`

- **Core Components**:
  - `BaseModel`: Abstract base model for common fields like `id`, `created_at`, and `updated_at`.
  - `PostReadTimeEngine`: Utility to estimate reading time for posts.
  - `drf_yasg`: API documentation generator.

### Routes and Endpoints

#### Account Endpoints
- `POST /api/v1/account/auth/token/register/`: Register a new user.
- `POST /api/v1/account/auth/token/login/`: Obtain JWT tokens.
- `POST /api/v1/account/auth/token/refresh/`: Refresh JWT tokens.
- `GET /api/v1/account/profile/`: Retrieve user profile.
- `GET /api/v1/account/explore/`: Explore user profiles.

#### Blog Endpoints
- `GET /api/v1/blog/post/`: Retrieve posts.
- `POST /api/v1/blog/post/`: Create a new post.
- `GET /api/v1/blog/post-explore/`: Explore public posts.
- `GET /api/v1/blog/post-search/`: Search posts using Elasticsearch.
- `POST /api/v1/blog/clap/`: Clap for a post.
- `POST /api/v1/blog/comment/`: Add a comment to a post.
- `POST /api/v1/blog/bookmark/`: Bookmark a post.
- `POST /api/v1/blog/rating-explore/`: Rate a post.

## Installation Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL
- Redis
- Elasticsearch
- RabbitMQ (for Celery)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd shadium-api
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements/development.txt
   ```

4. **Set Up Environment Variables**: 
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=<your-secret-key>
   ALLOWED_HOSTS=localhost,127.0.0.1
   POSTGRES_DB=shadium
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=127.0.0.1
   POSTGRES_PORT=5432
   REDIS_HOST=127.0.0.1
   REDIS_PORT=6379
   ```

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

## Running the Project

### Development

1. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

2. **Start Redis**:
   ```bash
   redis-server
   ```

3. **Run Celery Worker**:
   ```bash
   celery -A core worker --loglevel=INFO
   ```

4. **Run Celery Beat**:
   ```bash
   celery -A core beat --loglevel=INFO
   ```

### Production

1. **Run Gunicorn**:
   ```bash
   gunicorn core.wsgi:application --bind 0.0.0.0:8000
   ```

2. **Set Up Nginx**: Configure Nginx to proxy requests to Gunicorn.

3. **Run Celery and Beat**: Use a process manager like supervisord or systemd to manage Celery workers and beat.

4. **Elasticsearch**: Ensure Elasticsearch is running on http://localhost:9200.

## Languages & Translation Support

- **Supported Languages**: English (en), Persian (fa)
- **Import languages** using:
  ```bash
  python manage.py import_languages
  ```
- Admin users can adjust prices and content per language in the admin panel.

## Admin Panel Functionality

- **User Management**: Create, update, and delete users.
- **Content Management**: Manage posts, comments, claps, ratings, and bookmarks.
- **Language Settings**: Configure multilingual content.
- **Analytics**: Monitor user activity and post interactions.

## Environment Variables

| Variable | Description |
|----------|-------------|
| SECRET_KEY | Django secret key |
| ALLOWED_HOSTS | Comma-separated list of allowed hosts |
| POSTGRES_DB | PostgreSQL database name |
| POSTGRES_USER | PostgreSQL username |
| POSTGRES_PASSWORD | PostgreSQL password |
| POSTGRES_HOST | PostgreSQL host |
| POSTGRES_PORT | PostgreSQL port |
| REDIS_HOST | Redis host |
| REDIS_PORT | Redis port |

## Dependencies

- **Django**: Web framework
- **PostgreSQL**: Database
- **Redis**: Caching and Celery broker
- **Celery**: Task queue
- **Elasticsearch**: Full-text search engine
- **drf-yasg**: API documentation

## Database

- **Default**: PostgreSQL
- **Tables**:
  - User, Profile
  - Post, Comment, Clap, Rating, BookMark

## Extra Notes

- **Run Tests**:
  ```bash
  python manage.py test
  ```

- **Deployment Tips**:
  - Use gunicorn and nginx for production
  - Secure .env files and use strong secrets

- **Cron Jobs**:
  - Schedule periodic tasks using Celery Beat
