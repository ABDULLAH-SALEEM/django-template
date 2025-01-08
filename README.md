# Django Template App

This is a Django project template with a custom authentication system. It includes an app called `auth_manager`, which provides user authentication features like login, signup, and a custom decorator to protect API endpoints that require the user to be authenticated via a token.

## Features

- **Auth Manager App**:
  - **Signup API**: Create a new user account.
  - **Login API**: Login and receive a JWT token for authentication.
  - **Auth Me API**: Fetch the authenticated user’s data using the provided JWT token and a custom decorator to validate the token.

- **Custom Decorator**: Used to authenticate API requests by extracting the token from the request header and validating the user.

## Environment Variables

Before running the project, you need to set up the following environment variables in a `.env` file at the root of the project:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
SECRET_KEY=your_django_secret_key
DJANGO_SECRET_KEY=your_jwt_secret_key
