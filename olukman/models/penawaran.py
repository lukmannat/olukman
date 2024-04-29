from odoo import api, fields, models, _

class Penawaran(models.Model):
    _name = 'olukman.penawaran'
    _description = 'ini model untuk penawaran model siswa'

    name = fields.Char(string='Transaction No')
    tgl = fields.Date()
    total = fields.Float(compute='compute_total', store=True)

    @api.depends('detail_ids')
    def compute_total(self):
        for record in self:
            total = 0
            for detail in record.detail_ids:
                total = total + detail.subtotal
            record.total = total 

    detail_ids = fields.One2many('olukman.penawaran.detail', 'penawaran_id', string='Detail')

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