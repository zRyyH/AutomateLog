pip install --no-cache-dir -r requirements.txt
uvicorn api:app --host 127.0.0.1 --port 5000 --reload
pause