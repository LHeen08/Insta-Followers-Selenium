FROM python:3.10.12-buster

# Make a directory for our application
WORKDIR /code

# Install Dependencies
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

# Copy source code
COPY ./ .

# Run application
CMD ["python", "src/bot.py"]