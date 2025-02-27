from fileinput import filename

from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def greet():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    result = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    result = list(map(lambda string: f'<b>{string}</b>', result))
    return '<br><br>'.join(result)


@app.route('/image_mars')
def image_mars():
    img_src = 'https://avatars.mds.yandex.net/i?id=8acf03fb25a73bbf9777e648f1a3c3b4_l-4470294-images-thumbs&n=13'
    img_width = 300
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <meta charset="UTF-8"/>
        <title>Привет, Марс!</title>
      </head>
      <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{img_src}" width={img_width}px>
        <p>Вот она какая, красная планета.</p>
      </body>
    </html>
    '''


@app.route('/promotion_image')
def promotion_image():
    img_width = 300
    result = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    colors = [
        'alert alert-primary',
        'alert alert-danger',
        'alert alert-warning',
        'alert alert-success',
        'alert alert-info'
    ]
    result = list(map(lambda i: f'<div class="{colors[i]}"><b>{result[i]}</b></div>', range(len(result))))
    return f'''
        <!DOCTYPE html>
        <html lang="ru">
          <head>
            <meta charset="UTF-8"/>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}"/>
            <title>Колонизация</title>
          </head>
          <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.jpg')}" width={img_width}px>
            {''.join(result)}
          </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
