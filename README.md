# Trouble Shooting Week 1 Lab

반도체 설비 Trouble Shooting 1주차 실습 전용 배포 폴더입니다.

## 로컬 실행

```powershell
cd C:\Users\ivk55\cvd-academy-ts-week1
python -m pip install -r requirements.txt
python -m uvicorn main:app --host 127.0.0.1 --port 8001
```

브라우저에서 엽니다.

```text
http://127.0.0.1:8001/ts-week1
```

## Render 배포

이 폴더 전체를 GitHub 저장소로 올린 뒤 Render에서 Blueprint 또는 Web Service로 연결합니다.

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

배포 후 접속 경로:

```text
https://배포주소/ts-week1
```
