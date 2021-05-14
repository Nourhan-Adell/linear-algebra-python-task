#base file
FROM python
WORKDIR /app
COPY . .
RUN pip install numpy
CMD python app.py