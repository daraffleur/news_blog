# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

`docker-compose -f docker-compose-dev.yml build`

#### Before running project

- Create local env file
- Build containers
- Run project

#### Run project

`docker-compose -f docker-compose-dev.yml up`


#### When project is running

- Apply db migrations `make migrations`
- Create superuser `make test_user`. After that you will be able to login into Admin
- Be happy

#### Create new app

`make app name=<app_name>`

#### All commands you can find in `Makefile`
