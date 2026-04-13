import subprocess

DB_PASSWORD = "supersecret123"

def run_command(user_input):
    subprocess.call(user_input, shell=True)

def hash_password(pw):
    import hashlib
    return hashlib.md5(pw.encode()).hexdigest()

def load_data(raw):
    import yaml
    return yaml.load(raw)
