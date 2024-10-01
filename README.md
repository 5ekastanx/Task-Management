# 📝 Task Management System

A powerful and efficient task management system built with **Django**, **DRF**, **PostgreSQL**, and **Docker**. This application allows users to register, create, and manage tasks with role-based access control. 
 
## 🚀 Features  

- **User Registration & Authentication**: Secure user sign-up, login, and authentication using JWT.
- **Task Creation & Management**: Create, edit, delete, and assign tasks to users.
- **Role-Based Access Control (RBAC)**: Manage permissions based on user roles (e.g., Admin, Manager, Employee).
- **API Documentation**: Full API documentation with Swagger.
- **Dockerized Setup**: Easily deployable with Docker and Docker Compose.
- **PostgreSQL Database**: Robust task storage with PostgreSQL.
- **Heroku Deployment**: Live deployment on [Heroku](https://tasksmanagement-e7729fac3a0e.herokuapp.com/).

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Authentication**: JWT (JSON Web Tokens) using `djangorestframework-simplejwt`
- **Database**: PostgreSQL
- **Deployment**: Docker, Heroku
- **API Docs**: Swagger

## 📂 Project Structure
```bash
task_management/
│
├── task_management/        # Core project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI for deployment
│
├── tasks/                  # Main application
│   ├── models.py           # Database models for tasks
│   ├── serializers.py      # DRF serializers for API
│   ├── views.py            # API views and logic
│   └── urls.py             # URL routing for tasks API
│
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── Procfile                # Heroku deployment configuration
├── manage.py               # Django project manager
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
## 🖥️ Installation & Setup
1. Clone the repository
```bash
git clone https://github.com/5ekastanx/Task-Management.git
cd Task-Management
```
2. Set up environment variables
Create a .env file in the root directory with the following content:
SECRET_KEY=<your_secret_key>
DEBUG=False
ALLOWED_HOSTS=*
DATABASE_URL=<your_postgresql_database_url>
3. Build and run the project using Docker
```bash
docker-compose up --build
```
4. Apply database migrations
```bash
docker-compose exec web python manage.py migrate
```
5. Create a superuser (Admin)
```bash
docker-compose exec web python manage.py createsuperuser
```
6. Access the application
Visit the application at http://localhost:8000.

🧪 Running Tests
To run the tests for this project, use the following command:

```bash
docker-compose exec web python manage.py test
```
🚀 Deployment to Heroku
This project is ready for deployment to Heroku. It uses a Procfile for Heroku configuration.

To deploy:

Install the Heroku CLI and log in.

Create a new Heroku app:

```bash
heroku create your-app-name
```
Push to Heroku:

```bash
git push heroku main
```
Run database migrations on Heroku:

```bash
heroku run python manage.py migrate
```
📜 License
This project is licensed under the MIT License.

🌟 Developed by 5ekastanx. Feel free to explore and contribute!

This `README.md` provides an overview of your project, its features, setup, and deployment instructions, along with a clear folder structure. You can adjust any specific details such as the project URL and your preferred content.
