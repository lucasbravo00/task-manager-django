# To-Do List Web Application

This is a simple To-Do List web application built with Django. It allows users to create, edit, view, and delete tasks. The project is designed to help you manage tasks efficiently through an easy-to-use interface.

## Features

- User Authentication (Login and Registration)
- Create, Edit, and Delete Tasks
- View tasks with completion status
- Search for tasks by title

## Requirements

To run this project locally, you'll need:

- Python 3.x
- Django (latest version)

### Installing Dependencies

1. Clone the repository to your local machine:

```bash
git clone https://github.com/lucasbravo00/Task_manager_Django.git
cd Task_manager_Django
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setting Up the Database

Before running the server, you need to apply the database migrations to set up the necessary tables.

1. Run the following command to make migrations:

```bash
python manage.py makemigrations
```

2. Apply the migrations to set up the database:

```bash
python manage.py migrate
```

## Running the Development Server

After setting up the database, you can start the Django development server.

Run this command:

```bash
python manage.py runserver
```

The server will start running at `http://127.0.0.1:8000/`. Open this URL in your browser to see the app in action.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
