<img  src="https://flask.palletsprojects.com/en/stable/_images/flask-horizontal.png" height="100" />

# Flask API

## Project Description
This is a Flask app that has the purpose of learning about Python for building API's, learning about relationships with SQL Alchemy ORM.

## Technologies Used
![Flask](https://img.shields.io/badge/Flask%20-6DB33F?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQL%20Alchemy-00008B?style=for-the-badge&logo=spring-security&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

---

## Project Structure

```
├── api
│   ├── controller
│   ├── dto
│   ├── models
│   ├── schemas
│   └── service
├── config.py
├── docker-compose.yaml
├── migrations
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

### For this project you'll need

1. Python 3.10 or ^ installed in your local machine
2. Docker to build the database image
3. Pip for installing the requirements.txt file libraries

### Ok... now you can install the packages and run the project

1. Clone the repository
    ```
    git clone https://github.com/natanzeraa/flask-api.git
    ```
2. Navigate to projects folder
    ```
    cd flask-api
    ```
3. Create the virtual environment
    ##### Linux/MacOS
    ```
    python3 -m venv venv
    ```
    ##### Windows
    ```
    python -m venv venv
    ```
4. Activate the venv
    ##### Linux/MacOS
    ```
    source venv/bin/activate
    ```
    ##### Windows
    ```
    venv\Scripts\activate
    ```
5. Install the necessary packages
    ```
    pip install -r requirements.txt
    ```
6. Setup the Flask environment variable
    ##### Linux/MacOS
    ```
    export FLASK_APP=run.py
    echo $FLASK_APP
    ```
    ##### Windows
    ```
    $env:FLASK_APP = "run.py" 
    echo $env:FLASK_APP
    ```
7. Run the database build command
    ```
    docker compose up --build
    ```
8. Run migrations to populate database
    ```
    flask db migrate
    ```
9. Update database with new models
    ```
    flask db upgrade
    ```
10. Run the API
    ```
    python3 run.py
    ```

---


<div align="center">
<h6>Authors</h6>
    <table>
        <tbody>
            <tr>
                <td>
                    <div align="center">
                    <img src="https://avatars.githubusercontent.com/u/172435339?v=4/150" alt="Author's Photo" style="border-radius: 50%; width: 80px; height:80px;">
                    <h3>Natan Oliveira</h3>
                    <h6>Backend Developer</h6>
                    <a href="https://www.linkedin.com/in/natan-oliveira-71023822b/">
                        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
                    </a>
                    </div>
                </td>
                <td>
                    <div align="center">
                    <img src="https://avatars.githubusercontent.com/u/88974466?v=4" alt="Author's Photo" style="border-radius: 50%; width: 80px; height:80px;">
                    <h3>Jhonatan Paz</h3>
                    <h6>Data Analyst/Developer</h6>
                    <a href="https://www.linkedin.com/in/jhonatan-paz/">
                        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
                    </a>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</div>
