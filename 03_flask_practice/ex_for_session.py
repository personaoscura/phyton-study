from flask import Flask, request, session, redirect  # session과 redirect 모듈 사용

app = Flask(__name__)
app.secret_key = 'secret123'  # 세션을 사용하려면 필수로 설정해야 함 (암호화 키)

# 로그인 페이지
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userid = request.form.get("userid")  # 폼으로 입력받은 ID 추출
        session["user"] = userid  # 세션에 'user'라는 키로 사용자 ID 저장
        return redirect("/mypage")  # 로그인 후 마이페이지로 이동

    # GET 요청일 경우 로그인 폼을 보여줌
    return '''
        <form method="post">
            ID: <input name="userid"><br>
            <input type="submit" value="로그인">
        </form>
    '''

# 마이페이지 - 로그인한 사용자만 접근 가능
@app.route("/mypage")
def mypage():
    if "user" in session:  # 세션에 'user' 키가 있는지 확인 (로그인 여부 확인)
        return f"로그인됨! 사용자: {session['user']}<br><a href='/logout'>로그아웃</a>"
    else:
        return "로그인 안 됨! <a href='/'>로그인하러 가기</a>"

# 로그아웃 처리
@app.route("/logout")
def logout():
    session.pop("user", None)  # 세션에서 'user' 키 삭제 (로그아웃 처리)
    return redirect("/")  # 다시 로그인 페이지로 이동

if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드 활성화 (코드 수정 시 자동 재실행)
