import multiprocessing

from flask import Flask, request
from selenium_main import web_scrap
from multiprocessing import Pool  # Pool import하기

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'


@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    # [todo] 예외처리 필요
    pool = multiprocessing.Pool(3)
    pool.map(web_scrap, url_receive)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
    cpu_count = multiprocessing.cpu_count()
    print("cpu : ", cpu_count)
