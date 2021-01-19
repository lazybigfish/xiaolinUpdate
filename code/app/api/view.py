
from flask import make_response,jsonify,request
from app.api import api

@api.route('/v1.0/test/',methods = ['GET','POST'])

def test():

    #获取参数
    # if request.method == "POST":
    # 		# 获取表单参数
    #    username = request.form.get("username")
    #    password = request.form.get("password")
    # 		# 获取json参数
    #    data = request.get_json()
    # else:
    # 		# 获取get参数
    #    username = request.args.get("username")
    #    password = request.args.get("password")

    data = {'username': 'xxx', 'password': 'xxxx'}
    response = jsonify(code=200,
                       msg="success",
                       data=data)
    return response