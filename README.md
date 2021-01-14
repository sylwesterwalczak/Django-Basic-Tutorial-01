>Description in **English** below &#8595;&#8595;&#8595;

# Django Basic Tutorial [PL]

Cześć, w tym poradniku pokazuje, w jaki sposób napisać swoją pierwszą aplikacje blogowa  w oparciu o framework **Django** oraz jak połączyć ja z każdym dowolny szablonem HTML . 
Po obejrzeniu tej serii, zdobędziesz umiejętność napisania pięknie wyglądającej oraz w pełni funkcjonalnej aplikacji blogowej.

Orginalny szablon: https://startbootstrap.com/theme/clean-blog


### Instalacja


1. Pobierz aplikacje:
	``` 
	git clone https://github.com/sylwesterwalczak/Django-Basic-Tutorial-01.git
	```
2. Wybierz folder aplikcji :
	```
	cd ./Django-Basic-Tutorial-01-main
	```
3. Stwórz wirtualne środowisko :
	> **env** to nazwa środowiska/pliku
	```
	virtualenv env
	```
	lub 
	```
	python -m virtualenv env
	```
4. Aktywuj środowisko:
	> Mac OS oraz Linux:
	```
	source env/bin/activate
	```
	> Windows:
	```
	env/Scripts/activate
	```
5. Wejdz w folder /techblog:
	```
	(env): cd techblog
	```
6.  Przeprowadź pierwszą migracje:
	```
	(env): python manage.py migrate
	```
7.  Utwórz administratora:
	```
	(env): python manage.py createsuperuser
	```
8.  Uruchom aplikacje:
	```
	(env): python manage.py runserver
	```
8.  Polecenie utworzenia nowych migracji:
	```
	(env): python manage.py makemigrations
	```
9.  Deaktywacja środowiska po zakończonej pracy:
	```
	(env): deactivate
	```


### Funkcje

- Dodawanie wpisów
- Edytowanie wpisów
- Usuwanie wpisów
- Dodawanie użytkowników

  
# Django Basic Tutorial [ENG]

Hi, in this tutorial I show you how to write your first blog application based on the **Django** framework and how to combine it with any HTML template.
After watching this series, you will gain the ability to write a beautiful looking and fully functional blog application.

Original template: https://startbootstrap.com/theme/clean-blog


### Installation


1. Download the application:
	```
	git clone https://github.com/sylwesterwalczak/Django-Basic-Tutorial-01.git
	```
2. Select the application folder:
	```
	cd ./Django-Basic-Tutorial-01-main
	```
3. Create a virtual environment:
	> **env** is the name of the environment / file
 
	```
	virtualenv env
	```
	or
	```
	python -m virtualenv env
	```
4. Activate the environment:
	> Mac OS and Linux:
	```
	source env/bin/activate
	```
	> Windows:
	```
	env/Scripts/activate
	```
5. Go to the / techblog folder:
```
(env): cd techblog
```
6. Perform your first migration:
```
(env): python manage.py migrate
```
7. Create an administrator:
```
(env): python manage.py createsuperuser
```
8. Launch the applications:
```
(env): python manage.py runserver
```
8. Command to create new migrations:
```
(env): python manage.py makemigrations
```
9. Deactivation of the environment after the end of work:
```
(env): deactivate
```


### Functions

- Adding post
- Editing post
- Deleting post
- Adding users
