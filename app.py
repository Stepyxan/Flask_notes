from flask import Flask, request, jsonify
from datetime import datetime
import uuid
import settings
from bussiness import NotesEntity, new_note_from_web_dto, note_from_web_dto, note_from_db_dto
from dbservise import NotesService
from settings import uri

app = Flask(__name__)
db = NotesService(uri)
if __name__ == 'main':
  app.run(debug=True)

@app.route('/diary', methods=['POST'])
def diary_post():
    headers = request.headers
    jsn = request.json
    new_res = db.create(new_note_from_web_dto(jsn))
    return note_from_db_dto(new_res).to_web_dto(), 201

@app.route('/diary', methods=['GET'])
def diary_get():
    notes = [note_from_db_dto(note).to_web_dto() for note in db.collection.find({})]
    return {"notes" : notes}, 200
