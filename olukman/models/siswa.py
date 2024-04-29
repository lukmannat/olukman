from odoo import api, fields, models, _

class Siswa(models.Model):
    _name = 'olukman.siswa'
    _description = 'ini adalah master siswa'

    name = fields.Char()
    jumlah_pelajaran = fields.Integer(string='jumlah pelajaran yang diambil')
    tinggi = fields.Integer()
    hobby = fields.Selection(string='Kesukaannya apa?', selection=[
        ('makan','Makan'),
        ('renang','Renang'),
        ('menari','Menari'),
        ])

    keterangan = fields.Text(readonly=True, default='Ini defaultnya', store=True)

    harga =fields.Float("Harga yang disepakati")