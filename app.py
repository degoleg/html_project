from flask import Flask


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h3>Смотри, это — моя страничка</h3>
    <p>Страничек много, но эта – моя!</p>
    <p>Фронтенд – мой лучший друг!</p>
    """
    return page_content



if __name__ == ('__main__'):
    app.run()

