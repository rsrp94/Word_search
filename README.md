How to Run
1) python3 manage.py makemigrations
2) python3 manage.py migrate
3) python3 manage.py load_data /tmp/word_search.tsv   # To load input data to db
4) python3 manage.py runserver 0.0.0.0:1147

API query form browser
http://localhost:1147/search/?word=pract

