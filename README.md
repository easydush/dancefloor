## dancefloor
### backend
`cd backend`

`pip install -r ./requirements.txt`

copy `.env.template` as `.env` and set your variables

`python manage.py migrate`

`python manage.py init_dances`

`python manage.py runserver`

### frontend
`cd frontend`

`yarn`

`yarn serve`
