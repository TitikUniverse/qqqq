from flask import *
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/registration', methods=['GET', 'POST'])
def basic():
    response_object = {'status': 'asdf'}
    if request.method == 'POST':
        post_data = request.get_json() # наши данные (емаил, пароль)

        email = post_data.get('login')
        password = post_data.get('password')

        # auth.create_user_with_email_and_password(email, password)

        try:
            response_object['status'] = 'success'
        except:
            response_object['status'] = 'unsuccess'
    return jsonify(response_object)

@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        response_object['status'] = 'success'
        # post_data = request.get_json() # наши данные (емаил, пароль)

        # Тут надо обратиться к Firebase и спросить логин и пароль

        # email = post_data.get('login')
        # password = post_data.get('password')

        try:
            response_object['status'] = 'success'
        except:
            response_object['status'] = 'not success'
        return jsonify(response_object) 


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!') 

        
if __name__ == '__main__':
    app.run()
