from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fish.db'
db = SQLAlchemy(app)

class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100))
    family = db.Column(db.String(100))
    max_size = db.Column(db.Float)  # in centimeters
    min_tank_size = db.Column(db.Integer)  # in liters
    temperature_range = db.Column(db.String(50))  # in Celsius
    ph_range = db.Column(db.String(50))
    diet = db.Column(db.Text)
    temperament = db.Column(db.String(50))
    description = db.Column(db.Text)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Fish {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    fish_list = Fish.query.order_by(Fish.name).all()
    return render_template('index.html', fish_list=fish_list)

@app.route('/add', methods=['GET', 'POST'])
def add_fish():
    if request.method == 'POST':
        new_fish = Fish(
            name=request.form['name'],
            scientific_name=request.form['scientific_name'],
            family=request.form['family'],
            max_size=float(request.form['max_size']),
            min_tank_size=int(request.form['min_tank_size']),
            temperature_range=request.form['temperature_range'],
            ph_range=request.form['ph_range'],
            diet=request.form['diet'],
            temperament=request.form['temperament'],
            description=request.form['description']
        )
        db.session.add(new_fish)
        db.session.commit()
        flash('Fish added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_fish.html')

@app.route('/fish/<int:id>')
def view_fish(id):
    fish = Fish.query.get_or_404(id)
    return render_template('view_fish.html', fish=fish)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_fish(id):
    fish = Fish.query.get_or_404(id)
    if request.method == 'POST':
        fish.name = request.form['name']
        fish.scientific_name = request.form['scientific_name']
        fish.family = request.form['family']
        fish.max_size = float(request.form['max_size'])
        fish.min_tank_size = int(request.form['min_tank_size'])
        fish.temperature_range = request.form['temperature_range']
        fish.ph_range = request.form['ph_range']
        fish.diet = request.form['diet']
        fish.temperament = request.form['temperament']
        fish.description = request.form['description']
        db.session.commit()
        flash('Fish updated successfully!', 'success')
        return redirect(url_for('view_fish', id=fish.id))
    return render_template('edit_fish.html', fish=fish)

@app.route('/delete/<int:id>')
def delete_fish(id):
    fish = Fish.query.get_or_404(id)
    db.session.delete(fish)
    db.session.commit()
    flash('Fish deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 