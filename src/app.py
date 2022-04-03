from flask import render_template
from service import matrizes
from service import confinamentos

from flask import Flask
app = Flask(__name__)

list = [1,2,3,4]

@app.route('/')
def index():
    while True:
        return render_template("sensor.html", alo=sensor_1(list))


def sensor_1(num):
    teste = matrizes.getMatrizByRfid("[110, 32, 434, 222]")
    teste2 = confinamentos.getConfinamentoByMatriz(1)
    print(teste2)
    
    return list


if __name__ == "__main__":
    app.run(debug=True)
