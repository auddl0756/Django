# info 
- os : windows 10
- python :3.8
- django : 3.x.x

# How to start project 
on pycharm
1. create new project , virtual env
2. use terminal on pycharm
3. pip install django
 1. check your venv/Lib if django is installed. 
 2. Or check django version using "python -m django --version".

4. 프로젝트 생성 : django-admin startproject [프로젝트 명칭]
5. 앱 생성 :  python manage.py startapp [앱 명칭]
6. 설정 : 
 - ALLOW_HOSTS : ip or domain names
 - INSTALLED_APPS : include all apps in project
 - DATABASES
 - timezone

7. 테이블 생성 
<code>python manage.py migrate</code>

8. 관리자 생성
<code> python manage.py createsuperuser </code>

9. 서버 실행
 <code>python manage.py runserver [ip:port] </code>

10. model 생성 (db table)

11. view/template 생성
- URLconf : url/view mapping at urls.py
- view 구현
- template (.html 등) 작성


	       
