from flask import Flask, render_template, jsonify, abort
import json

# ჩავტვირთოთ მონაცემთა ბაზა
file_path = "rooms.json"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        rooms_db = json.load(file)
except FileNotFoundError:
    print(f"შეცდომა: ფაილი '{file_path}' ვერ მოიძებნა.")
    rooms_db = []
except json.JSONDecodeError:
    print(f"შეცდომა: არასწორი JSON ფორმატი.")
    rooms_db = []

app = Flask(__name__)

@app.route('/')
def index():
    # გადავცემ მონაცემებს, რომ for ციკლით გამოიტანოს ოთახები
    return render_template('index.html', rooms_db=rooms_db)

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/room/<int:room_id>')
# ოთახის id ის მიხედვით გამომაქვს ინფორმაცია, თუ ოთახი არაა, გამომაქვს 404 შეცდომა
def room_detail(room_id):
    room = next((r for r in rooms_db if r.get('id') == room_id), None)
    if room is None:
        abort(404)
    return render_template('room.html', room=room)

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.errorhandler(404)
# გამოვიტანოთ 404 შეცდომის გვერდი
def page_not_found(e):
    message = "გარემოებების უცნაური დამთხვევის გამო, თქვენ მოხვდით არარსებულ გვერდზე."
    return render_template('404.html', message=message), 404

if __name__ == '__main__':
    app.run(debug=True)