# 1. 기반이 될 이미지 (파이썬 3.9 슬림 버전)
FROM python:3.9-slim

# 2. 컨테이너 내부의 작업 폴더 설정
WORKDIR /app

# 3. 필요한 라이브러리 목록 파일 복사
COPY requirements.txt .

# 4. 라이브러리 설치
RUN pip install -r requirements.txt

# 5. 나머지 코드 복사
COPY . .

# 6. 컨테이너가 실행될 때 이 명령어를 실행
CMD ["python", "app.py"]