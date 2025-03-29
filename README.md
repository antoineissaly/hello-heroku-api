# Simple Flask "Hello World" API on Heroku

A basic demonstration project showing how to create a minimal Python Flask API and deploy it publicly using Heroku. This serves as a starting point for building and deploying simple Python web applications.

---

## Features

* Minimal Flask API setup using Python.
* Two simple endpoints:
    * `/`: Returns "Hello, World!"
    * `/api/hello`: Returns "Hello, API World!"
* Configured for easy Heroku deployment using Gunicorn.
* Uses Conda for local environment management (optional, venv also works).

---

## Technologies Used

* **Language:** Python 3.10
* **Framework:** Flask
* **WSGI Server:** Gunicorn
* **Platform:** Heroku
* **Version Control:** Git / GitHub
* **Environment (Local):** Conda

---

## Local Setup

Follow these steps to run the project on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/antoineissaly/hello-heroku-api
    cd hello-heroku-api
    ```

2.  **Create and Activate Conda Environment:**
    *(This project was developed using Conda, but you can adapt for venv if preferred)*
    ```bash
    conda create --name hello-heroku python=3.10
    conda activate hello-heroku
    ```

3.  **Install Dependencies:**
    The required packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

---

## Running Locally

1.  **Start the Flask Development Server:**
    Make sure your `hello-heroku` conda environment (or equivalent) is activated.
    ```bash
    python app.py
    ```
    * **Note:** The local development server in this project's `app.py` is configured to run on port `6000`.

2.  **Access the Application:**
    Open your web browser or use a tool like `curl`:
    * `http://127.0.0.1:6000/` -> Should display "Hello, World!"
    * `http://127.0.0.1:6000/api/hello` -> Should display "Hello, API World!"

---

## Deployment to Heroku

This application is ready for deployment to Heroku.

1.  **Prerequisites:**
    * [Heroku Account](https://signup.heroku.com/)
    * [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed and logged in (`heroku login`)
    * Git repository initialized and code committed.

2.  **Create Heroku App:**
    If you haven't already created an app on Heroku for this project:
    ```bash
    heroku create your-unique-app-name # Or heroku create for a random name
    ```

3.  **Push to Heroku:**
    Deploy the code from your `main` branch:
    ```bash
    git push heroku main
    ```
    Heroku will detect the Python app, install dependencies from `requirements.txt`, and launch the web process defined in the `Procfile` using Gunicorn.

4.  **Open Deployed App:**
    ```bash
    heroku open
    ```

---

## API Endpoints

* **`GET /`**
    * **Description:** Returns a simple plain text welcome message.
    * **Response:**
        * Status: `200 OK`
        * Body: `Hello, World!`
        * Content-Type: `text/html; charset=utf-8`

* **`GET /api/hello`**
    * **Description:** Returns a simple plain text API message.
    * **Response:**
        * Status: `200 OK`
        * Body: `Hello, API World!`
        * Content-Type: `text/html; charset=utf-8`

---

## Project Structure

hello-heroku-api/
├── .git/             # Git directory
├── .gitignore        # Specifies intentionally untracked files that Git should ignore
├── app.py            # Main Flask application code
├── Procfile          # Heroku process definition (how to run the app)
├── README.md         # This file
└── requirements.txt  # Python package dependencies
