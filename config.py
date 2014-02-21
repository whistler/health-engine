import os

environment = os.getenv('ENVIRONMENT', "development")
development = False

if environment == "production":
    pass
else:
    pass
    development = True