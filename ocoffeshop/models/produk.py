# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Produk(models.Model):
    _name = 'ocoffeshop.produk' 

    _description = 'Ini adalah master produk'

    no_transaksi = fields.Char(string="Kode Produk")

    name = fields.Char('Nama Produk', required=True)

    harga = fields.Float()

    state = fields.Selection(string='Status', selection=[
        ('large', 'Large'),
        ('medium', 'Medium'),
        ('small', 'Small'),
    ])

    notes = fields.Text(readonly=True)


