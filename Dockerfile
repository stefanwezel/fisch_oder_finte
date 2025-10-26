# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=game.py

# Expose the port the app runs on
EXPOSE 5000

# Add a health check (verifies the container is responding)
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:5000/ || exit 1

# Set an environment variable based on the MODE argument
ARG MODE
ENV MODE=${MODE}

# Print the MODE value to verify it's set correctly
RUN echo "MODE is set to ${MODE}"

# Default command depending on MODE
CMD if [ "$MODE" = "development" ]; then \
        export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run --host=0.0.0.0; \
    else \
        gunicorn --bind 0.0.0.0:5000 game:app; \
    fi
