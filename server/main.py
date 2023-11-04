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
    misinfo_xml = root.findAll('.//misinfo')
    misinfo_list = []
    for misinfo_xml_element in misinfo_xml:
        text = misinfo_xml_element.find('.//text').text
        explanation = misinfo_xml_element.find('.//explanation').text
        misinfo_list.append({'text': text, 'explanation': explanation})
    return jsonify(misinfo_list), 200
  except:
    return jsonify({}), 400

if __name__ == '__main__':
  app.run(debug=True)
