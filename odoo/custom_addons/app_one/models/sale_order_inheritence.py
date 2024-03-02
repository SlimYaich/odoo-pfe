from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #Relier Module Sale avec App_one OneToMany
    property_id = fields.Many2one('property')

    #esm methode lezem n'activiw extention odoo debug w n7ottou clique de la souris sur
    #bouton confrim tou yothhrou les info menhom esm methode action_confirm
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside action_confirm method")
        # Logic
        return res




