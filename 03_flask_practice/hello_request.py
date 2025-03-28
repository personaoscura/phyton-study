from flask import Flask, request

app = Flask(__name__)

# 이름 입력 폼을 보여주는 페이지
@app.route("/")
def index():
    return '''
        <form action="/greet" method="post">
            이름: <input type="text" name="username"><br>
            나이: <input type="number" name="userage"><br>
            <input type="submit" value="인사하기">
        </form>
    '''

# 폼 제출을 처리하고 인사하는 페이지
@app.route("/greet", methods=["POST"])
def greet():
    username = request.form["username"]
    userage=request.form["userage"]
      # 폼에서 입력한 값 가져오기
    return f"안녕하세요, {username}님!{userage}살이시군요!"

if __name__ == "__main__":
    app.run(debug=True)
