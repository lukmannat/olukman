from odoo import api, fields, models, _
from datetime import datetime, timedelta


class Penjualan(models.Model):
    _name = 'ocoffeshop.penjualan' 
    _description = 'Ini adalah transkasi penjualan'

    name = fields.Char('No Transaksi', default = "New", readonly=True, store=True)

    notes = fields.Text(default="ini adalah value default untuk field: notes")
    
    def default_tgl(self):
        tgl = fields.Date.today()
        return tgl

    tgl = fields.Date(default=fields.Date.today())
    tgl_kirim = fields.Date(default=datetime.today() + timedelta(days=3))

    customer_id =  fields.Many2one(comodel_name='res.partner', ondelete='restrict')

    total = fields.Float(compute="compute_total", store=True)
    
    
    @api.depends('produk_ids')
    def compute_total(self):
        for record in self:
            total = 0
            for produk in record.produk_ids:
                total += produk.subtotal

            record.total = total

    produk_ids = fields.One2many(comodel_name='ocoffeshop.penjualan.produk', inverse_name='penjualan_id' )

    @api.model
    def create(self, vals):

        if vals.get('name') != '' or vals.get('name') == 'New':

            tanggal_hari_ini = datetime.today().strftime('%Y%m%d')
            name  = self.env['ir.sequence'].next_by_code('penjualan_seq') 

            vals['name'] = "{}-{}".format(name, tanggal_hari_ini)

        return super(Penjualan, self).create(vals)


    def write(self, vals):
        
        return super(Penjualan, self).write(vals)



class PenjualanProduk(models.Model):
    _name = 'ocoffeshop.penjualan.produk' 
    _description = 'Ini adalah produk-produk yang dijual'

    penjualan_id = fields.Many2one(comodel_name='ocoffeshop.penjualan', ondelete='restrict')

    produk_id = fields.Many2one(comodel_name='ocoffeshop.produk', ondelete='restrict')

    state = fields.Selection(string='Status', selection=[
        ('large', 'Large'),
        ('medium', 'Medium'),
        ('small', 'Small'),
    ], related="produk_id.state")


    qty = fields.Integer()
    
    harga_transaksi = fields.Float(related="produk_id.harga", store=True)

    subtotal = fields.Float(compute="compute_subtotal", store=True)


    @api.depends('qty', 'harga_transaksi')
    def compute_subtotal(self):
        print("nama model = ", self._name)
        print("nama description = ", self._description)

        for record in self:
            record.subtotal = record.qty * record.harga_transaksi
