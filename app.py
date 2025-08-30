import string, random
from flask import Flask, render_template, request, redirect
from models import db, URL

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Home page: shorten URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        new_url = URL(original_url=original_url, short_id=short_id)
        db.session.add(new_url)
        db.session.commit()
        return redirect('/dashboard')
    return render_template('index.html')

# Dashboard: show all URLs
@app.route('/dashboard')
def dashboard():
    urls = URL.query.all()
    return render_template('dashboard.html', urls=urls)

# Redirect: use short URL
@app.route('/<short_id>')
def redirect_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first_or_404()
    return redirect(url.original_url)

if __name__ == "__main__":
    with app.app_context():   # ✅ ensures db is created before running
        db.create_all()
    app.run(debug=True)
