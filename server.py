# -*- coding:utf-8 -*-
from flask import Flask
from flask import request,render_template
from flask import jsonify
import json
import datetime
import assessment

app = Flask(__name__)

@app.route('/health')
def health():
    return 'success'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def process_register():
    username = request.form.get("userName")
    password = request.form.get("pwd")
    token = request.form.get("token")
    action = request.form.get("action")
    assessment_result = assessment.create_assessment('gcp-wow', '6Ld6yKsgAAAAABnsgsqfxvI1WJzXuZVPhVv0go2R', token, action)
    print(assessment_result)
    score = str(assessment_result.risk_analysis.score)
    #score = str(assessment_result)
    return score 

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
