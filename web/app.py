from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# (중요!) 'redis'라는 이름의 호스트에 접속합니다.
# 이 'redis'는 docker-compose.yml에 정의할 서비스 이름입니다.
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # redis DB에서 'hits' 키의 값을 1 증가시킵니다.
    count = redis.incr('hits')
    return f"<h1>Hello, Docker-Compose! 🐳</h1><h3>This page has been visited {count} times.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)