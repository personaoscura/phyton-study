from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route("/", methods=["GET", "POST"])
def login():
    # TODO: POST 요청 시 ID 받아서 세션에 저장
    # TODO: 로그인 성공하면 /mypage로 이동
    # TODO: GET 요청일 경우 로그인 폼 보여주기
    if request.method=="POST":
        userid=request.form.get("userid")
        session["user"]=userid
        return redirect("/mypage")
    return '''
        <form method="post">
            ID: <input name="userid"><br>
            <input type="submit" value="로그인">
        </form>
    '''
@app.route("/mypage")
def mypage():
    # TODO: 세션에 user가 있으면 사용자 이름 보여주기
    # TODO: FLAG 페이지 링크와 로그아웃 링크 추가
    # TODO: user가 없으면 로그인 페이지로 안내
    if"user"in session:
        return f'''로그인됨! 사용자: {session['user']}<br>
        <a href='/logout'>로그아웃</a>
        <a href='/flag'>FLAG</a>'''
    else:
        return "로그인 안 됨! <a href='/'>로그인하러 가기</a>"
@app.route("/flag")
def flag():
    # TODO: user가 admin일 경우에만 FLAG 출력
    # TODO: 아닌 경우 접근 거부 메시지
    if session.get("user")=="admin":
        return '''flag = 1334134134'''
    else:
        return'''!!warning!!<br>you are not admin'''
@app.route("/logout")
def logout():
    # TODO: 세션에서 user 삭제 후 /로 이동
    session.pop("user", None)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
