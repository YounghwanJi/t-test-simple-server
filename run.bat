@echo off
REM === Run FastAPI ===
REM Usage: run.bat

echo Starting FastAPI [t-test-simple-server]
uv run uvicorn main:app --host 0.0.0.0 --port 8100 --reload
