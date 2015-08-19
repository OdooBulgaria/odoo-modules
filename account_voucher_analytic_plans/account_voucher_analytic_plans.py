# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015 be-cloud.be
#                       Jerome Sonnet <jerome.sonnet@be-cloud.be>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv

class account_voucher(osv.osv):
    _inherit = "account.voucher"

    _columns = {
        'analytics_id': fields.many2one('account.analytic.plan.instance', 'Analytic Distribution'),
    }
    
class account_voucher_line(osv.osv):
    _inherit = 'account.voucher.line'

    _columns = {
        'analytics_id': fields.many2one('account.analytic.plan.instance', 'Analytic Distribution'),
    }

    def create(self, cr, uid, vals, context=None):
        if 'analytics_id' in vals and isinstance(vals['analytics_id'], tuple):
            vals['analytics_id'] = vals['analytics_id'][0]
        return super(account_voucher_line, self).create(cr, uid, vals, context=context)

    # def move_line_get_item(self, cr, uid, line, context=None):
    #     res = super(account_voucher_line, self).move_line_get_item(cr, uid, line, context=context)
    #     res ['analytics_id'] = line.analytics_id and line.analytics_id.id or False
    #     return res

    # def product_id_change(self, cr, uid, ids, product, uom_id, qty=0, name='', type='out_invoice', partner_id=False, fposition_id=False, price_unit=False, currency_id=False, company_id=None, context=None):
    #     res_prod = super(account_invoice_line, self).product_id_change(cr, uid, ids, product, uom_id, qty, name, type, partner_id, fposition_id, price_unit, currency_id, company_id=company_id, context=context)
    #     rec = self.pool.get('account.analytic.default').account_get(cr, uid, product, partner_id, uid, time.strftime('%Y-%m-%d'), context=context)
    #     if rec and rec.analytics_id:
    #         res_prod['value'].update({'analytics_id': rec.analytics_id.id})
    #     return res_prod