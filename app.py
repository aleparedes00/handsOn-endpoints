import os
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    versions_list = ['2.0', '1.0', '0.1']
    if request.method == 'GET':
      return json.dumps(versions_list)
    else:
      return "I just don't get it"

@app.route('/ping')
def pinging():
    r = "Boum boum\nBoum boum\nBoum boum"
    return json.dumps(r)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
