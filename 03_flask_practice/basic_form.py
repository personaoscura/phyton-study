from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = '비밀키'

# 📌 1. 라우팅 - 기본 페이지
@app.route("/", methods=["GET", "POST"])
def login():
    # 로그인 처리 (POST) 또는 로그인 폼 출력 (GET)
    pass

# 📌 2. 마이페이지
@app.route("/mypage")
def mypage():
    # 세션에 로그인된 사용자 확인해서 내용 출력
    pass

# 📌 3. 관리자 FLAG 페이지
@app.route("/flag")
def flag():
    # 세션이 admin일 경우에만 FLAG 출력
    pass

# 📌 4. 로그아웃
@app.route("/logout")
def logout():
    # 세션 삭제 후 리디렉트
    pass

if __name__ == "__main__":
    app.run(debug=True)
