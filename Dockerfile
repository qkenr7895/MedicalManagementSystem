FROM python:3.7.0
ARG PROJECT_DIR="/medical_management_system"
COPY . ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install requests
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000