from app import db

class Mahasiswa(db.Model):
    npm = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(80), nullable=False)
    tgl_lahir = db.Column(db.DateTime, nullable=False)
    alamat = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Mahasiswa %r>' % self.npm