# gallery_now_2

고품격 국내 전시 커뮤니티 gallery now 의 2번째 버전입니다 😊

### 기존 gallery now 대비 변경점 목록 (2024.01.21)

Python 버전 변경 : 3.9 -> 3.12
Django 버전 변경 : 3.2.18 -> 4.2.9
DB 변경 : sqlite3 -> MySQL

```bash
# mysqlclient 설치
pip install mysqlclient
# load timezone info
mysql_tzinfo_to_sql tz_dir(/usr/share/zoneinfo.default/)
```

# gallery_now

I want to rest !!

##

0. 장고 설치
   `pip install django==3.2.18`
1. 의존성 파일 생성
2. 프로젝트 생성`django-admin startproject [프로젝트명] .`( `.` 현재위치)
3. 앱 생성 `python manage.py startapp articles`
4. .gitignore 생성
5. settings.py 작성

   - app 등록
   - extensions 추가
   - STATIC, MEDIA 세팅

6. 로컬 개발환경 및 smart 커밋 메세지 세팅 !

   - [x] 김신혜
   - [x] 이수정
   - [x] 전성재
   - [x] 최계수

## local 개발 환경 setting 튜토리얼

1. repository clone 및 가상환경 생성

```bash
# clone remote
git clone https://github.com/IWTR-3/gallery_now.git
cd gallery_now

# virtual env setting
python -m venv .venv
source .venv/bin/activate
pip  install -r requirements.txt

# add commit message template
git config --local commit.template .github/.gitmessage.txt
```

2. commit & push

```bash
# branch from develop
git checkout -b feature/{ 기능 또는 이슈 } develop
```

> 작업 중간중간 의미 단위 커밋 자주해주세요.

```bash
git add <path or file>
git commit
```

> 푸시 .. 전에 develop 머지하기 !

```bash
git pull origin develop:develop
git merge --ff develop
```

> 컨플릭트 해소 후 다시 커밋해주세요.

```bash
git commit --reedit-message=<commit>
git push origin feature/{ 기능 또는 이슈 }
```

3. pull request
