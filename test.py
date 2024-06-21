# test_redis_connection.py
import os
import redis
from dotenv import load_dotenv
load_dotenv()
# Fetch environment variables
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
print(f"Redis configuration - Host: {REDIS_HOST}, Port: {REDIS_PORT}, SSL: False")
# Connect to Redis
try:
    r = redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        ssl=False  # Set to True if required by your Redis server
    )
    r.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")
print(1)
