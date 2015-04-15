# Quadrus Practicum

## Viewing the website

Simply visit http://quadruspracticum.com/

## Running the code

To run the code, you'll need to install Python 2.7, Django 1.7, and Pillow

```
pip install Django==1.7
pip install pillow
```

Then, simply navigate to the directory containing manage.py, and run:

```
python manage.py runserver
```

The server should run on port 8000. You should be able to visit http://localhost:8000/ to see the site.

## Setting up a production webserver

I personally chose Apache 2.4 to serve this project. Hosted in the AWS Cloud, on Amazon EC2 (VPS), with an Amazon RDS MySQL instance covering the backend database. The /static and /media files are hosted direct from Apache, the fancy Django is hosted with WSGI, Python 2.7, Django 1.7. Version control is with git, hosted on GitHub, obviously, because you're reading this. Vehicles, Orders, and People can be managed through the Django Admin page (http://quadruspracticum.com/admin/) with the username "admin" and the password "!QAZasas4867". The MySQL backend is easily maintained with phpMyAdmin (http://quadruspracticum.com/pma/), with the username "root" and the password "!QAZasas4867".  Image uploads are handled in part by Pillow. The MySQL connector is "mysqlclient". Page load speeds are dramatically improved by caching with a local install of memcached. Originally, I used ElastiCache, but it doubled the page load times compared to a local cache. Now, cached pages are generated in under 3ms.
