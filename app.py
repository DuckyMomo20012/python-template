from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

print("Hello World")

SECRET_KEY = env.str("SECRET_KEY")

print(f"My secret key: {SECRET_KEY}")
