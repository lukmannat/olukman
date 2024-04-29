from odoo import api, fields, models, _
from datetime import datetime, timedelta


class Penawaran(models.Model):
    _name = 'olukman.penawaran'
    _description = 'ini model untuk penawaran model siswa'

    name = fields.Char('Transaction No', default ='New' , readonly=True)
    notes = fields.Text(default="ini adalah value default untuk field: notes")
    
    def default_tgl(self):
        tgl = fields.Date.today()
        return tgl

    tgl = fields.Date(default=fields.Date.today())
    tgl_kirim = fields.Date(default=datetime.today() + timedelta(days=3))


    total = fields.Float(compute='compute_total', store=True)

    @api.depends('detail_ids')
    def compute_total(self):
        for record in self:
            total = 0
            for detail in record.detail_ids:
                # total = total + detail.subtotal
                total += detail.subtotal
            record.total = total 

    detail_ids = fields.One2many('olukman.penawaran.detail', 'penawaran_id', string='Detail')

    # @api.model
    # def create(self,vals):

    #     if vals.get('name') != '' or vals.get('name') == 'New':
        
    #         tanggal_hari_ini = datetime.today().strftime('%Y%m%d')
    #         name = self.env['ir.sequence'].next_by_code

class PenawaranDetail(models.Model):
    _name = 'olukman.penawaran.detail'
    _description = 'ini model detail untuk mealakukan penawaran oleh siswa'

    penawaran_id = fields.Many2one(string='', comodel_name='olukman.penawaran', ondelete='restrict')   

    siswa_id = fields.Many2one(comodel_name='olukman.siswa', ondelete='restrict')

    harga_detail = fields.Float(string='', related='siswa_id.harga', store=True)

    qty = fields.Integer(string='')
    subtotal = fields.Float(string='', compute='compute_subtotal', store=True)

    @api.depends('qty','harga_detail')
    def compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.harga_detail