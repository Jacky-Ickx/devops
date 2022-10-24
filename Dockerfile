FROM python:3.10-slim

LABEL maintainer="inf20058@lehre.dhbw-stuttgart.de"

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

# install python dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# set working directory and copy files into container
WORKDIR /app
COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

