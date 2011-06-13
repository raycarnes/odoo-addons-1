# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc, OpenERP Professional Services   
#    Copyright (C) 2010-2011 Avanzosc S.L (http://www.avanzosc.com). All Rights Reserved
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
{
    "name": "Avanzosc Product Lot Workflow",
    "version": "1.0",
    "depends": ["base",
                "stock"],
    "author": "Avanzosc (Urtzi Odriozola)",
    "category": "Custom Module",
    "description": """
    This module provide :
    * A workflow engine in order to trace lot state.
    """,
    "init_xml": [],
    'update_xml': ["stock_prodlot_view.xml",
                   "stock_prodlot_workflow.xml",
                   "res_partner_view.xml"
                   ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}