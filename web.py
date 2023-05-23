from flask import Flask, render_template, request

app = Flask(__name__)


# 创建了网址/show/info和函数的对应关系
# 在浏览器上访问/show/info就会自动执行index
@app.route("/show/info", methods=["GET"])
def index():
    return render_template("homepage.html")


@app.route("/get/more")
def get_more():
    return render_template("more.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user = request.form.get("user")
        psw = request.form.get("psw")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        skill_list = request.form.getlist("good at")
        more = request.form.getlist("more")

        print(user, psw, gender, hobby_list, city, skill_list, more)

        return "注册成功"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # print(request.form)
        user = request.form.get("username")
        password = request.form.get("password")
        print(user, password)
        return "登录成功"



# @app.route("/do/reg", method=["GET"])
# def do_register():
#     # 接收用户通过get形式发送过来的数据
#     print(request.args)
#     # 给用户返回结果
#     return "注册成功"


# @app.route("/post/reg", methods=["POST"])
# def post_register():
    # 接收用户通过形式发送过来的数据
    # 获取全部数据
    # print(request.form)

    # 获取想要的数据
    # user = request.form.get("user")
    # psw = request.form.get("psw")
    # gender = request.form.get("gender")
    # hobby_list = request.form.getlist("hobby")
    # city = request.form.get("city")
    # skill_list = request.form.getlist("good at")
    # more = request.form.getlist("more")
    #
    # print(user, psw, gender, hobby_list, city, skill_list, more)
    #
    # return "注册成功"


if __name__ == '__main__':
    app.run()
