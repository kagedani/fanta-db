# Fanta-db

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/kagedani/fanta-db)
![GitHub contributors](https://img.shields.io/github/contributors/kagedani/fanta-db)
![GitHub stars](https://img.shields.io/github/stars/kagedani/fanta-db?style=social)
![GitHub forks](https://img.shields.io/github/forks/kagedani/fanta-db?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/kagedani?style=social)

Fanta db is a `lightweight process` to import into a local docker postgreSQL `statistics for italian fantasy football of the last N seasons`.
Additional line of information text about what the project does. Your introduction should be around 2 or 3 sentences. Don't go overboard, people won't read it.

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed the latest version of [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
* You have installed the latest version of [Conda](https://docs.conda.io/en/latest/) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
* You have installed at least Python 3.6
* You have a `Windows/Linux` machine. On Mac this is not tested
* You have an official account on [Leghe Fantacalcio](www.fantacalcio.it)

Nevertheless, if you are not interested in getting your hands dirty into the app code, you can just launch everything as a docker compose file, so the only requirements needed in this case is:
* [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

## Fanta db setup

To start the setup you need to clone the repository: 
```
git clone https://github.com/kagedani/fanta-db.git
```

### Local Setup

Open the source folder of the project using your favourite IDE (Visual Studio and Pycharm are my favourites).

Create the conda environment starting from the env file `env.yml` located in the project source folder
```
conda env create -f env.yml -n <env-name>
```
At this point the only thing you need is to create a configuration in your IDE to exploit the conda env created and define a couple of env vars (as described in the next section).

### Docker compose setup 

You need to do absolutely nothing except running

```
docker compose up -d
```

in the `docker-compose/all`. Then you can access the database that keeps running. 

## Using Fanta db

To use Fanta db, follow these steps:

* Change directory to docker-compose/database and launch the postgreSQL with:
```
docker compose up -d
```

Once launched, you can just run the main.py file located into the `build` folder.

### Configurations

The base configurations for the application are: 
```python
ENV = "default"
APP_NAME = "fanta-db-23"
EMPTY_STRING = ""
APP_EXEC_ID = EMPTY_STRING
MAX_CONNECT_TIMEOUT = 30
MAX_RESPONSE_TIMEOUT = 30
FANTACALCIO_IT_ENDPOINT = "https://www.fantacalcio.it"
FANTACALCIO_IT_LOGIN_PATH = "/api/v1/User/login"
FANTACALCIO_IT_DOWNLOAD_PATH = "/api/v1/Excel/stats/{SEASON}/1"
FANTACALCIO_IT_DOWNLOAD_CONFIG = {
    "2324": "18",
    "2223": "17",
    "2122": "16",
    "2021": "15"
}
USERNAME = os.getenv("FANTA_USERNAME") or "default"
PSW = os.getenv("FANTA_PSW") or "default"
LOG_CONFIG = {
    "default": {
        "file_level": "INFO",
        "file_path": f"./src/log/{APP_NAME}.json",
        "console_level": "DEBUG"
    }
}
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://fanta_db_username:fanta_db_password@{os.getenv('DB_HOST')}/fanta_db"
SESSION_MAKER = None
```

As you can see, `DB_HOST`, `FANTA_USERNAME` and `FANTA_PSW` are taken from the env, so to use the application you need to export these values as environments variables.
`DB_HOST` just need to be equal to 'localhost' if you prefer to run the app locally without exploit the docker compose complete file.

## Next features

- [x] Single docker compose to run everything
- [ ] Test coverage

## Contributing to Fanta db
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to Fanta db, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@kagedani](https://github.com/kagedani) 📖

## Contact

If you want to contact me you can reach me at daniele.uboldi.job@gmail.com.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [MIT License](https://choosealicense.com/licenses/mit/).