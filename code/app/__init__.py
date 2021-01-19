from flask import Flask, jsonify, abort, make_response, request
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect('test.db')
tasks = [
    {
        'id': 1,
        'title': u'闻小武',
        'description': u'上高首富, 资本家, 豪车豪宅, 千亿资产, 股市兴风作浪者',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo',methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/tasks',methods=['POST'])
def creat_task():
    # if not request.json or not in request.json :
    #     abort(404)

    task = {
        'id':tasks[-1]['id'] + 1,
        'title':request.args['title'],
        'description':request.args.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({'task':task})

# @app.route('/todo/<int:task_id>',methods=['GET'])
# def get_task(task_id):
#     task = filter(lambda t: t['id'] == task_id, tasks)
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ =='__main__':
    app.run(debug=True)