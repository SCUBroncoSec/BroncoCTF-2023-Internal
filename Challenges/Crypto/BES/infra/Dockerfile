FROM python:latest
COPY . /infra
WORKDIR /infra
RUN pip install pycryptodome
ENTRYPOINT ["python"]
CMD ["bes.py"]
EXPOSE 8080