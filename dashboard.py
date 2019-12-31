from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def index():
    marudor_spich_url = 'https://marudor.de/Spich'
    vrs_luelsdorferstr_url = 'https://www.vrs.de/am/s/9d2d71cf888a36807bc36f8d45020f90'
    return render_template('index.html', 
            marudor_spich_url=marudor_spich_url,
            vrs_luelsdorferstr_url=vrs_luelsdorferstr_url)

if __name__ == "__main__":
    app.run()