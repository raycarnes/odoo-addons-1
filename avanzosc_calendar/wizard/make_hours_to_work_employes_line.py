# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from datetime import datetime, timedelta
import time

from osv import osv
from osv import fields

from tools.translate import _
 
class make_hours_to_work_employes_line(osv.osv_memory):

    _name = 'make.hours.to.work.employes.line'
    _description = "Make Hours To Work Employes Line"
 
    _columns = {'make_hours_to_work_employes_id':fields.many2one('make.hours.to.work.employes', 'Template Employes'),
                'employee_id': fields.many2one('hr.employee', 'Employe', ),
                'selected':fields.boolean('Select')
         }
    
make_hours_to_work_employes_line()