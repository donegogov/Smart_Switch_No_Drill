# server.py
from flask import Flask, render_template
from standart_servo import turnSwitchOnOff, motionDetectOnOff

# create a flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/switch/<int:state>", methods=['POST'])
def setSwitch(state):
    # route for lamp control
    if state == 0:
        turnSwitchOnOff(False)
    elif state == 1:
        turnSwitchOnOff(True)
    else:
        return ('Unknown SWITCH state', 400)
    return ('', 204)

@app.route("/motion/<int:state>", methods=['POST'])
def setMotionMode(state):
    if state == 0:
        motionDetectOnOff(False)
    elif state == 1:
        motionDetectOnOff(True)
    else:
        return ('Unknown SWITCH state', 400)
    return ('', 204)
    
# __name__ will be __main__ only if this file is the entry point
if __name__ == '__main__':
    # run the server on this ip and port 50100
    app.run(host='0.0.0.0', port=50100, debug=True)


