# Overview
간단한 테스트를 위해 GET API 하나만 제공하는 서버.

# API
- /getHello

# Run
``` bash
\> ./run.bat
or
\> uv run uvicorn app.main:app --host 0.0.0.0 --port 8100 --reload
```

# Docker
``` bash
# build
\> docker build -t t-test-simple-server .

# Run container
\> docker run -p 8100:8100 t-test-simple-server
```