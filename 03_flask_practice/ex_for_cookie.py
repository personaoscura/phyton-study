from flask import Flask, request, make_response

app = Flask(__name__)

# 쿠키를 설정해주는 라우트
@app.route("/set")
def set_cookie():
    resp = make_response("쿠키가 설정되었습니다! 이제 /admin 접속해보세요.")
    resp.set_cookie("auth", "admin")  # 쿠키 이름: auth, 값: admin
    return resp

# 관리자 페이지
@app.route("/admin")
def admin():
    auth = request.cookies.get("auth")  # auth라는 쿠키를 가져옴

    if auth == "admin":
        return "🎉 FLAG: You are admin!"
    else:
        return "⛔ 너 관리자 아님! 쿠키 확인해봐라~"

if __name__ == "__main__":
    app.run(debug=True)
