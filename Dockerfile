FROM python:3.8.7-buster

# Make a directory for our application
WORKDIR /code

# Install Dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy source code
COPY ./ .

# Run application
CMD ["python", "bot.py"]