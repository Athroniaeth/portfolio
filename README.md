<div align="center">
    <h1 style="font-size: xx-large; font-weight: bold;">Portfolio</h1>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.12-0">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/License-MIT-f">
    </a>
    <br>
</div>

Pierre Chaumont's portfolio using FastAPI (Python) on the back-end and Tailgrids on the front-end (HTML, Tailwinds).

## Installation

This project uses Miniconda and Poetry for dependency management. To install the dependencies, run the following command:

```bash
poetry install
```

## Usage

To run the project, use the following commands:

```bash
python src
```

## Contribution

To install the development dependencies, run:

```bash
poetry install --dev
```

To add a new dependency, use:

```bash
poetry add <dependency>
```

For development-specific dependencies, use:

```bash
poetry add --group dev <dependency>
```

To activate pre-commit hooks, run:

```bash
poetry run pre-commit install
```

## Structure

```bash
├── README.md         # The file you are currently reading
├── htmlcov           # The coverage report folder
├── pyproject.toml    # The poetry configuration file
├── ruff.toml         # The ruff configuration file (linter, formatter)
├── scripts           # Scripts useful for the project (no CI/CD)
├── src               # The source code folder
│   ├── __init__.py   # Can add global variables
│   ├── __main__.py   # The entry point of the project
└── tests             # The tests folder (pytest)
```

## Tailgrids

This project uses Tailgrids for the front-end. Tailgrids is a combination of Tailwind CSS and Gridsome. It is a simple and efficient way to create static websites.

For replicate Tailwind CSS, use the following commands (or this [tutorial](https://tailgrids.com/docs/installation/html)):

Install Tailwind and generate the config file.

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Install TailGrids.

```bash
npm i tailgrids
```

Update the tailwind.config.js file with the TailGrids plugin.
    
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.html", "./src/static/**/*.js"],
  theme: {},
  variants: {
    extend: {},
  },
  plugins: [require("tailgrids/plugin")],
};
```

Add Tailwind CSS directives to your CSS file. (path : `static/inputs.css`)

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Generate the CSS file with the build command.

```javascript
{
  "devDependencies": {
    "tailwindcss": "^3.4.6"
  },
  "dependencies": {
    "tailgrids": "^2.2.6"
  },
  "scripts": {
    "build": "npx tailwindcss -i ./src/static/input.css -o ./src/static/output.css --watch"
  }
}
```

Then, we will have to run the build command:

```bash
npm run build
```

## OVH Installation
For installing from zero this project on OVH Cloud, you need to buy before
- OVH Cloud Instances (Discovery is sufficient)
- Domain name (by exemple 'pierrechaumont.fr' with sub-domain 'www')

### OVH Cloud Instances

1. Select '`Discovery`' instances D2-2 (5,50€/month)
2. Select localisation (by exemple 'Gravelines', 'GRA11')
3. Select Ubuntu 24.04 LTS
4. Select SSH key (create one if you don't have)
   - Open CMD, run `ssh-keygen -t rsa`
   - Set the path to save the key (by exemple 'C:\Users\USERNAME\.ssh\id_rsa')
   - Set a passphrase (a good password)
   - Give to OVH the public key (by exemple 'C:\Users\USERNAME\.ssh\id_rsa.pub')
5. Select one instance (valid default parameters)
6. Select the '`Public network`'
7. Select facturation (by exemple 'Hourly billing' if you want can stop the instance without paying)

### Connection to the instance

In the list of instances, select the one you just created and click on name, you will be redirected to the instance page.
Get '`Information of connection`' SSH at botom right of the page, you will have the IP address of the instance.

```bash
Information of connection
ssh ubuntu@57.128.65.49
```

Go to your terminal and run the command with the IP address of your instance.

```bash
ssh ubuntu@57.128.65.49
```

Validate the connection by typing '`yes`' and press '`Enter`'. (save the fingerprint)
Then, enter the passphrase of your SSH key.

Install python3 and pip3 on the instance.

```bash
sudo apt update -y
sudo apt install python3-pip -y
```

Create a virtual environment and install the dependencies.
Import the git repository on the instance. (we'll just create a “portfolio” folder with just one `main.py` file)

Create a folder for the project.

```bash
mkdir portfolio
cd portfolio
```

Install the virtual environment, create it, and activate it.
Warning, without venv, Ubuntu don't support pip3 install in the user folder.

```bash
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies.

```bash
pip install fastapi uvicorn
```

```bash
nano main.py
```

In the `main.py` file, copy the following code:

```python
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

# Redirect HTTP to HTTPS
@app.middleware("http")
async def redirect_http_to_https(request: Request, call_next):
    if request.url.scheme == "http":
        url = request.url.replace(scheme="https")
        return RedirectResponse(url)
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
```

To make this project work you will need to generate a certificate. You can use Let's Encrypt for that.
Warning, you can't generate a certificate for an IP address, you need a domain name. (by exemple 'pierrechaumont.fr')
Warning, you must target the domain name without 'www' for the certificate. ('www' is sub domain, certificate for this sub domaine don't are recognized for non-sub domain)

We use certbot for that, certbot need to have server on port 80, you can't start FastAPI and generation certificate in the same time.
We use Nginx for that, Nginx is a web server that can be used as a reverse proxy, load balancer, mail proxy, and HTTP cache. Certbot have module for Nginx.
There no conflict of port with Nginx and Certbot.

For install Nginx, run the following command:

```bash
sudo apt-get update -y
sudo apt-get install certbot -y
sudo apt-get install python3-certbot -y
```

Create Ngix configuration file for the project.

```bash
sudo mkdir /etc/nginx/
sudo mkdir /etc/nginx/sites-available

sudo nano /etc/nginx/sites-available/pierrechaumont.fr
```

In the file, copy the following code:

```nginx
# Redirect HTTP to HTTPS for non-www
server {
    listen 80;
    server_name pierrechaumont.fr;

    location /.well-known/acme-challenge/ {
        root /var/www/html;
    }

    location / {
        return 301 https://pierrechaumont.fr$request_uri;
    }
}

# Redirect HTTP to HTTPS for www
server {
    listen 80;
    server_name www.pierrechaumont.fr;

    location /.well-known/acme-challenge/ {
        root /var/www/html;
    }

    location / {
        return 301 https://www.pierrechaumont.fr$request_uri;
    }
}

# HTTPS server block for non-www
server {
    listen 443 ssl;
    server_name pierrechaumont.fr;

    ssl_certificate /etc/letsencrypt/live/pierrechaumont.fr/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pierrechaumont.fr/privkey.pem;

    location /.well-known/acme-challenge/ {
        root /var/www/html;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# HTTPS server block for www
server {
    listen 443 ssl;
    server_name www.pierrechaumont.fr;

    ssl_certificate /etc/letsencrypt/live/pierrechaumont.fr/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pierrechaumont.fr/privkey.pem;

    location /.well-known/acme-challenge/ {
        root /var/www/html;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Start Nginx server.

```bash
sudo apt update
sudo apt install nginx -y

sudo systemctl restart nginx
```

For test if it's work, follow these steps:
```bash
sudo mkdir -p /var/www/html/.well-known/acme-challenge
echo "test" | sudo tee /var/www/html/.well-known/acme-challenge/test
```

With your browser, test these URLs:
- http://pierrechaumont.fr/.well-known/acme-challenge/test
- http://www.pierrechaumont.fr/.well-known/acme-challenge/test

You must create redirection of the domain name (pierrechaumont.fr) to the IP address of the instance.
You can do that in the OVH manager, in the DNS zone of the domain name.
- Add a new record of type 'A' with the name '@' and the IP address of the instance.
- Add a new record of type 'A' with the name 'www' and the IP address of the instance.
- Delete all another 'A' and 'AAAA'
- 
Certbot will check that domain access to Nginx server, he drop a file in the folder `/var/www/html/` and check if the file is accessible by the domain name.

Generate the certificate with Certbot.

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d pierrechaumont.fr -d www.pierrechaumont.fr -v --test-cert
```

Answer the questions, and you will have your certificate.
- Valid email : `pierre.chaumont@hotmail.fr`
- Accept the terms of service : `Y`
- Accept the sharing of your email : `Y`

Valid the mail address by clicking on the link in the mail.

Normally, you have the certificate in the folder `/etc/letsencrypt/live/pierrechaumont.fr/`
- ssl-keyfile = /etc/letsencrypt/live/pierrechaumont.fr/privkey.pem
- ssl-certfile = /etc/letsencrypt/live/pierrechaumont.fr/fullchain.pem

For each FastAPI server, you must specify the path of the certificate and the key.

Launch the FastAPI server.
Warning with port 80/443, you need to have root access to use this port. When you use sudo,
Ubuntu lost the virtual environment, you need to specify the path of the python interpreter.
You must use 443 for the HTTPS server, for redirect HTTP to HTTPS, you must start two servers with two different ports.

Before stop Nginx server, after that you can start FastAPI server.
```bash
sudo systemctl stop nginx
```

```bash
sudo /home/ubuntu/portfolio/venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile /etc/letsencrypt/live/pierrechaumont.fr/privkey.pem --ssl-certfile /etc/letsencrypt/live/pierrechaumont.fr/fullchain.pem &
```

With your browser, test these URLs:
- http://pierrechaumont.fr (domaine redirection to HTTPS)
- https://pierrechaumont.fr (domaine work with HTTPS)
- http://www.pierrechaumont.fr (sub-domaine redirection to domaine and redirection to HTTPS)
- https://www.pierrechaumont.fr (sub-domaine redirection to domaine and work with HTTPS)
