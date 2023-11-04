from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/find', methods=['POST'])
def find():
  data = request.data
  if not data:
    return jsonify({'error': 'Invalid JSON'}), 400
  try:
    root = ET.fromstring(data)
    text = root.find('.//text').text
    explanation = root.find('.//explanation').text
    return jsonify({'text': text, 'explanation': explanation}), 200
  except:
    return jsonify({}), 400

if __name__ == '__main__':
  app.run(debug=True)
