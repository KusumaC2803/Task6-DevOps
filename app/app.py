from flask import Flask 
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
cache = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        cache.incr("visits")
        visits = cache.get("visits").decode()
    except:
        visits = "Redis not available"
    return f"Hellon from Flask! Visists: {visits}"

@app.route("/health")
def health():
    return {"status":"healthy"},200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)        