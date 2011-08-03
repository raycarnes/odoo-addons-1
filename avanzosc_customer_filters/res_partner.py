# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class res_partner(osv.osv):

    _inherit = 'res.partner'
 
    _columns = {
            'contact': fields.related('address', 'name', type='char', string='Contact'),
    }
    
res_partner()

class res_partner_job(osv.osv):

    _inherit = 'res.partner.job'
 
    _columns = {
            'is_default': fields.boolean('Default'),
    }
    
#    def onchange_default(self, cr, uid, ids, uncheck=False):
#        res = {}
#        if uncheck:
#            res = {
#                'is_default': False,
#            }
#            self.write(cr, uid, ids, res)
#        else:
#            for job in self.browse(cr, uid, ids):
#                for job2 in job.address_id.job_ids:
#                    if job.id != job2.id:
#                        self.onchange_default(cr, uid, [job2.id], True)
#
#        return True
    
res_partner_job()

class res_partner_address(osv.osv):
    
    _inherit = 'res.partner.address'
    
    def _set_name(self, cr, uid, ids, fields, arg, context=None):
        if context is None:
            context = {}

        if not ids:
            return {}
        res = {}
        contact_obj = self.pool.get('res.partner.contact')
        for address in self.browse(cr, uid, ids):
            for job in address.job_ids:
                if job.is_default:
                    name = contact_obj.name_get(cr, uid, [job.contact_id.id])
                    if name:
                        res[job.address_id.id] = name[0][1]
        
        if not len(res):
            return {}
        return res
    
    _columns = {
        'name': fields.function(_set_name, method=True, type='char', size=64, string='Contact Name', store=True),
    }
    
res_partner_address()