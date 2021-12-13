FROM python:3.9.7-alpine3.14
WORKDIR /examples
ADD . /examples
RUN pip install -r requirements.txt --use-feature=2020-resolver
CMD ["python3", "main.py"]