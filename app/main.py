from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from my Python App!'

@app.route('/api/version')
def version():
    return jsonify({'version': '1.0.0'})

if __name__ == '__main__':
    # For development, not for production deployment directly
    # In production, you'd typically use Gunicorn
    app.run(debug=True, host='0.0.0.0', port=5000)
