FROM node:18-alpine
WORKDIR /app
COPY . .
RUN pip install requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
