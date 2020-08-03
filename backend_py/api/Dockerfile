FROM python
RUN mkdir -p /api
COPY requirements.txt /api
WORKDIR /api
RUN pip install -r requirements.txt
COPY . /api
ENV SECRETKEY=eteration
ENV DBLOCATION=postgresql://postgres:eteration@20.52.58.77:5432/api
CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:81", "--timeout", "120", "api:api"]
EXPOSE 81
