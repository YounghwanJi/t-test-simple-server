# Overview
다른 서버에서 API 호출 테스트를 위한 Mock CRUD API를 제공하는 서버입니다.
실제 데이터베이스 연동 없이 즉시 JSON 응답을 반환합니다.
(by claude code)

# API Endpoints

## 테스트 엔드포인트
- `GET /getHello` - Hello 메시지 반환

## Items CRUD API (Mock)

### 1. 아이템 생성
```
POST /api/items
Content-Type: application/json

Request Body:
{
  "name": "Sample Item",
  "description": "Item description (optional)",
  "price": 1000 (optional)
}

Response (201 Created):
{
  "id": 1,
  "name": "Sample Item",
  "description": "Item description",
  "price": 1000,
  "created": true
}
```

### 2. 단일 아이템 조회
```
GET /api/items/{id}

Response (200 OK):
{
  "id": 1,
  "name": "Sample Item 1",
  "description": "This is a mock item for testing",
  "price": 1100
}
```

### 3. 아이템 목록 조회
```
GET /api/items?limit=10&offset=0

Response (200 OK):
{
  "items": [
    {
      "id": 1,
      "name": "Sample Item 1",
      "description": "Description for item 1",
      "price": 1100
    },
    ...
  ],
  "total": 10,
  "offset": 0,
  "limit": 10
}
```

### 4. 아이템 수정
```
PUT /api/items/{id}
Content-Type: application/json

Request Body:
{
  "name": "Updated Item (optional)",
  "description": "Updated description (optional)",
  "price": 2000 (optional)
}

Response (200 OK):
{
  "id": 1,
  "name": "Updated Item",
  "description": "Updated description",
  "price": 2000,
  "updated": true
}
```

### 5. 아이템 삭제
```
DELETE /api/items/{id}

Response (200 OK):
{
  "id": 1,
  "deleted": true,
  "message": "Item 1 has been deleted"
}
```

# Run

## 로컬 실행
``` bash
# Windows
> ./run.bat

# 또는 직접 실행
> uv run uvicorn main:app --host 0.0.0.0 --port 8100 --reload
```

서버 실행 후 접속:
- API 서버: http://localhost:8100
- Swagger UI: http://localhost:8100/docs
- ReDoc: http://localhost:8100/redoc

## Docker로 실행

### 방법 1: docker 명령 사용
``` bash
# 이미지 빌드
> docker build -t t-test-simple-server .

# 컨테이너 실행
> docker run -p 8100:8100 t-test-simple-server

# 백그라운드 실행
> docker run -d -p 8100:8100 --name t-test-simple-server t-test-simple-server

# 컨테이너 중지
> docker stop t-test-simple-server

# 컨테이너 삭제
> docker rm t-test-simple-server
```

### 방법 2: docker-compose 사용 (권장)
``` bash
# 서비스 시작 (백그라운드)
> docker-compose up -d

# 서비스 중지
> docker-compose down

# 로그 확인
> docker-compose logs -f

# 서비스 재시작
> docker-compose restart

# 이미지 재빌드 후 시작
> docker-compose up -d --build
```

# Testing Examples

## curl 예제
```bash
# POST - 아이템 생성
curl -X POST http://localhost:8100/api/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Item","price":500}'

# GET - 단일 조회
curl http://localhost:8100/api/items/1

# GET - 목록 조회
curl "http://localhost:8100/api/items?limit=5&offset=0"

# PUT - 수정
curl -X PUT http://localhost:8100/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated Item"}'

# DELETE - 삭제
curl -X DELETE http://localhost:8100/api/items/1
```

# Features
- ✅ FastAPI 기반 고성능 API 서버
- ✅ 완전한 CRUD 작업 지원 (POST, GET, PUT, DELETE)
- ✅ Pydantic을 통한 자동 요청 검증
- ✅ Mock 데이터 즉시 반환 (DB 불필요)
- ✅ 자동 생성 API 문서 (Swagger UI, ReDoc)
- ✅ Docker 및 Docker Compose 지원