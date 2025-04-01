FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install the system dependencies
RUN apt-get update && \
    # Install nodejs for frontend
    apt-get install -y nodejs npm \
    curl nano # Install for debugging / manual editing

# Set the working directory
WORKDIR /app

# Add the lock file to the image (and necessary files for uv sync)
COPY uv.lock /app/uv.lock

# UV need of this files to sync the dependencies
COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
RUN mkdir /app/src/athrerank -p
RUN touch /app/src/athrerank/__init__.py

# Sync the Python dependencies
RUN uv sync --frozen --all-extras  --no-dev

# Add the frontend files
COPY ./front /app/front

# Build the frontend
RUN npm install --prefix /app/front
RUN npm run build --prefix /app/front

# Add the backend files
COPY ./src /app/src/

# Copy config files
COPY ./config.toml /app/config.toml

# Expose the port
EXPOSE 8000

# Run the Python application
CMD ["uv", "run", "src/athrerank"]