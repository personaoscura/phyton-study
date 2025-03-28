from flask import Flask, request  # Flask 앱과 요청 데이터를 다루는 request 불러오기

app = Flask(__name__)  # Flask 애플리케이션 객체 생성

# 루트 페이지("/")에서 GET과 POST 요청 모두 처리
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # 폼으로 전달된 POST 데이터 중 name="userid" 값을 가져옴
        userid = request.form.get("userid")
        # 폼으로 전달된 POST 데이터 중 name="password" 값을 가져옴
        password = request.form.get("password")
        # 사용자에게 입력된 결과를 HTML로 출력
        return f"입력된 ID: {userid}, 비밀번호: {password}"

    # GET 요청일 경우 → HTML 폼을 사용자에게 보여줌
    return '''
        <h2>로그인</h2>
        <form method="post">  <!-- 폼을 POST 방식으로 서버에 전송 -->
            ID: <input type="text" name="userid"><br>  <!-- 사용자 ID 입력 -->
            PW: <input type="password" name="password"><br>  <!-- 사용자 비밀번호 입력 -->
            <input type="submit" value="로그인">  <!-- 전송 버튼 -->
        </form>
    '''

# 이 파일을 직접 실행할 경우 Flask 서버 실행
if __name__ == "__main__":
    app.run(debug=True)  # debug=True로 하면 코드 바꿀 때 자동 재시작 + 에러 보기 쉬움
