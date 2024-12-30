from app.model.mahasiswa import Mahasiswa
from app import response
from flask import request, jsonify
from app import db

def index():
    try:
        mahasiswa = Mahasiswa.query.all()
        data = transform(mahasiswa)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.bad_request(message="An error occured while fetching mahasiswa")
    
def store():
    try:
        npm = request.json['npm']
        name = request.json['nama']
        tgl_lahir = request.json['tgl_lahir']
        alamat = request.json['alamat']
        mahasiswa = Mahasiswa(npm=npm, nama=name, tgl_lahir=tgl_lahir, alamat=alamat)
        db.session.add(mahasiswa)
        db.session.commit()
        return jsonify({"message": "Mahasiswa created successfully"})
    except Exception as e:
        print(e)
        return response.bad_request(message="An error occured while creating mahasiswa")
        
def transform(mahasiswa):
    data = []
    for mhs in mahasiswa:
        data.append({
            "npm": mhs.npm,
            "nama": mhs.nama,
            "tgl_lahir": mhs.tgl_lahir,
            "alamat": mhs.alamat
        })
    return data

def update(npm):
    try:
        npm = request.json['npm']
        name = request.json['nama']
        tgl_lahir = request.json['tgl_lahir']
        alamat = request.json['alamat']
        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()
        
        if mahasiswa:
            mahasiswa.npm = npm
            mahasiswa.nama = name
            mahasiswa.tgl_lahir = tgl_lahir
            mahasiswa.alamat = alamat
            db.session.commit()
            return response.ok("", "Mahasiswa updated successfully")
        else:
            return response.error("Mahasiswa not found", 404)
        
    except Exception as e:
        print(e)
        return response.error("An error occured while updating mahasiswa", 500)
    
def singleTransform(mahasiswa):
    data = {
        "npm": mahasiswa.npm,
        "nama": mahasiswa.nama,
        "tgl_lahir": mahasiswa.tgl_lahir,
        "alamat": mahasiswa.alamat
    }
    return data
    
def show(npm):
    try:
        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()

        if not mahasiswa:
            return response.badRequest([], "Mahasiswa not found")
        
        data = singleTransform(mahasiswa)
        return response.ok(data, "Mahasiswa retrieved successfuly")

    except Exception as e:
        print(f"An error request: {e}")