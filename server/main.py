from flask import Flask, request, jsonify
from flask_cors import CORS
import xml.etree.ElementTree as ET
import traceback

from completion import query, format_query
from parser import get_content

app = Flask(__name__)
cors = CORS(app,
            resources={r"/find": {"origins": "*"}},
            allow_headers=['Content-Type', 'content-type'])


@app.route('/find', methods=['POST'])
def find():
  data = request.json
  if not data:
    return jsonify({'error': 'Invalid JSON'}), 400
  try:
    title, main_text, author, source = get_content(data)
    formatted_query = format_query(title, main_text, author, source)
    completion = query(formatted_query)
    xml = '<root>' + completion['results'][0] + '</root>'
    root = ET.fromstring(xml)
    misinfo_xml = root.findall('.//info')
    misinfo_list = []
    for misinfo_xml_element in misinfo_xml:
        text = misinfo_xml_element.find('.//text').text.strip().strip('\n')
        explanation = misinfo_xml_element.find('.//explanation').text.strip().strip('\n')
        sources = [source.find('.//source').text.strip().strip('\n') for source in misinfo_xml_element.findall('.//sources')]
        misinfo_list.append({'text': text, 'explanation': explanation, 'sources': sources})
    return jsonify({'segments': misinfo_list}), 200
  except:
    traceback.print_exc()
    return jsonify({'error': 'Failed to parse'}), 400


if __name__ == '__main__':
  app.run(debug=True, port=5000)
