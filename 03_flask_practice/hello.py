# Flask 모듈에서 Flask 클래스 불러오기
from flask import Flask

# Flask 애플리케이션 인스턴스 생성
# __name__은 현재 파일 이름이며, Flask가 이걸 통해 경로를 잡음
app = Flask(__name__)

# "/" 경로로 접속했을 때 실행할 함수 등록
@app.route("/")
def home():  # home() 함수는 실제로 실행될 로직을 담음
    return "Hello, Flask!"  # 브라우저에 표시될 문자열을 반환

# 이 파일이 직접 실행된 경우에만 아래 코드 실행됨
if __name__ == "__main__":
    # Flask 서버 실행 + 디버그 모드 켜기 (자동 리로드 + 에러 페이지 보기 가능)
    app.run(debug=True)