from app import app
from app.controller import MahasiswaController
from flask import request

@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    if request.method == 'GET':
        return MahasiswaController.index()
    else:
        return MahasiswaController.store()

@app.route('/mahasiswa/<npm>', methods=['PUT', 'GET', 'DELETE'])
def productDetail(npm):
    if request.method == 'GET':
        return MahasiswaController.show(npm)
    elif request.method == 'PUT':
        return MahasiswaController.update(npm)
    elif request.method == 'DELEETE':
        return MahasiswaController.delete(npm)
    