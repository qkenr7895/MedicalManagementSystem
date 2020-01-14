# 1. 개요
병원과 환자, 약국을 연결해주는 어플리케이션
# 2. 실행
### 2-1) 이미지 빌드
    $docker build -t qkenr7895/medical_management_system .
### 2-2) 이미지 실행
    $docker run -p 8000:8000 qkenr7895/medical_management_system:latest 
### 2-3) DB 구축
    $python manage.py makemigrations
    $python manage.py migrate
    $python pharmace_bulk.py
    $python hospital_bulk.py
    $python user_bulk.py
### 2-4) 접속
    127.0.0.1:8000/account/signin

# 3. 설명
자세한 사항은 description.pdf 확인
