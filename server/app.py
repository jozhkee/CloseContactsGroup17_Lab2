from flask import Flask, request, jsonify
from peewee import *

app = Flask(__name__)

db = SqliteDatabase("contacts.db")

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    name = TextField()
    phone = TextField()

db.connect()
db.create_tables([Contact])

# Seed default contacts if table is empty
if Contact.select().count() == 0:
    default_contacts = [
        {"name": "Tiago Alexandre Mendes",    "phone": "+351 912 345 678"},
        {"name": "Beatriz Sofia Figueiredo",  "phone": "+351 925 876 543"},
        {"name": "Mateus Henrique Oliveira",  "phone": "+351 933 210 987"},
        {"name": "Valentina Maria Guerreiro", "phone": "+351 964 555 123"},
        {"name": "Gonçalo Nuno Vasconcelos",  "phone": "+351 918 777 444"},
        {"name": "Inês Filipa Cavaco",        "phone": "+351 929 000 111"},
        {"name": "NovaIMS",                   "phone": "+351 213 870 380"},
    ]
    Contact.insert_many(default_contacts).execute()

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = []
    for contact in Contact.select().order_by(Contact.name):
        contacts.append({
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone
        })
    return jsonify(contacts)

@app.route("/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()
    name = data.get("name", "")
    phone = data.get("phone", "")
    contact = Contact.create(name=name, phone=phone)
    return jsonify({
        "message": "Contact added",
        "id": contact.id
    }), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
