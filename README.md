* Designed the code using Django
* How to install django follow the documentation
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-16-04

How to Run
1) python3 manage.py makemigrations
2) python3 manage.py migrate
3) python3 manage.py load_data /tmp/word_search.tsv   # To load input data to db
4) python3 manage.py runserver 0.0.0.0:1147

API query form browser
http://localhost:1147/search/?word=pract

output:

![image](https://user-images.githubusercontent.com/16955073/63015548-df36ac80-beae-11e9-806f-f6dd71b8b001.png)
