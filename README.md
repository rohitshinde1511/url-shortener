# URL Shortener (Flask + SQLite)

A simple URL shortener web app built with **Flask** and **SQLite**.  
Users can enter a long URL and get a shortened version that redirects back to the original.

---

## 🚀 Features
- Shorten any valid URL into a random 6-character code.
- Dashboard to view all shortened URLs.
- Redirect to original URL when visiting the short link.
- Built with **Flask**, **SQLAlchemy**, and **Jinja2 templates**.
- Lightweight and beginner-friendly.

---

## 🛠️ Tech Stack
- Python 3.10+
- Flask 3.x
- SQLite (via SQLAlchemy)
- HTML + Jinja2 templates
- Optional: CSS in `/static`

---

## 📂 Project Structure

url-shortener/
├─ app.py # main Flask app
├─ models.py # database models
├─ templates/ # HTML templates
│ ├─ index.html
│ └─ dashboard.html
├─ static/ # CSS/JS (optional)
├─ requirements.txt # dependencies
├─ .env # env vars (optional)
└─ .gitignore


---

## ⚡ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/rohitshinde1511/url-shortener.git
cd url-shortener


### 2. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
python app.py

Visit → http://127.0.0.1:5000

### 📖 Usage

(1) Go to the home page, enter a URL, and click Shorten.

(2) A random short ID will be generated.

(3) Visit /dashboard to see all shortened links.

(4) Access http://127.0.0.1:5000/<short_id> to be redirected to the original URL.

###. 🔮 Future Improvements

* Add user authentication (login/signup).

* Track number of clicks for each URL.

* Allow custom short codes.

* Add Bootstrap styling

Built by Rohit Shinde