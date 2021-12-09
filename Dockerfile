FROM python
WORKDIR /examples
ADD . /examples
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]