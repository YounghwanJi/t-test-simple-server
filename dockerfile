# Python 3.12를 기본 이미지로 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 프로젝트 파일 복사
COPY pyproject.toml uv.lock* ./

# 의존성 설치
RUN uv sync --frozen --no-dev

# 애플리케이션 코드 복사
COPY main.py ./

# 포트 노출
EXPOSE 8100

# 애플리케이션 실행
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100"]