# Polls Application

This is a simple poll application built using Django. Users can create polls with multiple choices and vote on them. The application also provides a simple admin interface for managing polls.

## Features

- Create and manage polls
- Add multiple choices to each poll
- Vote on polls
- View poll results

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yashovardhn/polls.git
    ```

2. Navigate to the project directory:

    ```bash
    cd polls
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your web browser and go to `http://127.0.0.1:8000` to see the application running.

## Usage

1. Log in to the admin interface at `http://127.0.0.1:8000/admin` using the superuser credentials you created.

2. Create polls and add choices.

3. Visit `http://127.0.0.1:8000` to view and vote on polls.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please contact [yashovardhn](https://github.com/yashovardhn).

