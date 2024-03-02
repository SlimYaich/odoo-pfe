from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Property Record'
    _inherit = ['mail.thread' , 'mail.activity.mixin']

    name = fields.Char(required=1, default='New', size=12)
    description = fields.Text(tracking=1)
    postcode = fields.Char(required=1)
    date_availability = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_Price = fields.Float()
    diff = fields.Float(compute='_compute_diff' , store=1 )
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ],  # default='north'
    )

    # Relation Entre Property et Owner
    owner_id = fields.Many2one('owner')

    # Relation Entre Property et tag
    tag_ids = fields.Many2many('tag')

    # fi champs owner_address et owner_phone yjibli automatiquement address wel phone mta3 owner
    #read only : on peut le modifier
    # store : update automatiquement dans la base de donnée

    owner_address = fields.Char(related='owner_id.address' , readonly=0 , store=1)
    owner_phone = fields.Char(related='owner_id.phone' , readonly=0 , store=1)



    # ADD STATE
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ], default='draft')

    _sql_constraints = [
        ('unique_name', 'unique ("name")', 'This name is exist!')
    ]

    line_ids = fields.One2many('property.line', 'property_id')



    @api.depends('expected_price' , 'selling_Price' , 'owner_id.phone')
    def _compute_diff(self):
        for rec in self:
            print(rec)
            print("inside _compute_diff method")
            rec.diff = rec.expected_price - rec.selling_Price

    @api.onchange('expected_price' )
    def _onchange_expected_price(self):
        for rec in self:
            print(rec)
            print("inside _onchange_expected_price method")
            return {
                'warning' : {'title' : 'warning' , 'message' : 'negative value' , 'type' : 'notification'}
            }

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('PLease add valid number of bedrooms!')

    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create method")
        # Logic
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
        print("inside search method")
        return res

    # UPDATE  METHOD
    def write(self, vals):
        res = super(Property, self).write(vals)
        print("inside write method")
        return res

    # DELETE METHOD
    def unlink(self):
        res = super(Property, self).unlink()
        print("inside unlink method")
        return res

    # ACTION BOUTON STATE : DRAFT
    def action_draft(self):
        for rec in self:
            print("inside draft : action")
            rec.state = 'draft'
            # rec.write({
            #   'state' : 'draft'
            # })

    # ACTION BOUTON STATE : PENDING
    def action_pending(self):
        for rec in self:
            print("inside pending : action")
            rec.write({
            'state' : 'pending'
             })
    # ACTION BOUTON STATE : SOLD
    def action_sold(self):
        for rec in self:
            print("inside sold : action")
            rec.state = 'sold'

    # Adding One2many Lines & Notebook and Pages Tabs.
    class PropertyLine(models.Model):
        _name = 'property.line'

        property_id = fields.Many2one('property')
        area = fields.Float()
        description = fields.Char()
