# DjangoVision

Real-time object detection web app powered by Django and TensorFlow

## Backend Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/Kumala3/DjangoVision.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd django_vision
    ```

3. **Create a new virtual environment**

    ```bash
    python -m venv venv
    ```

    - Activate the virtual environment
        - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

        - **MacOs/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Rename** `.env.dist` to `.env` and replace your environmental variables

    **Example:**
    
    `django_vision/.env`
    ```
    SECRET_KEY=Your_Django_Secret_Key
    DEBUG=False
    ```

6. **Run the project with daphne**

    ```bash
    daphne django_vision.asgi:application
    ```
