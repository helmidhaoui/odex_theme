    #-*- coding: utf-8 -*-
from odoo import http, _
import logging
import json
import os
from odoo.http import request
import requests
_logger = logging.getLogger(__name__)

class ChangeColor(http.Controller):
    
    
            
    @http.route('/change_color', type='http', auth='public')
    def change_Color(self,**post):
        res=[]
        color = post.get('color')
        if os.name == 'nt':
            less_path = repr(__file__).replace('controllers','static')
            less_path = less_path.replace('change_color.py','src\\less\\variables.less')
            less_path = less_path.replace('\\\\','\\')
            less_path = less_path.replace("'","")
            
        else:
            less_path = repr(__file__).replace('/controllers/change_color.py','/static/src/less/variables.less')
            less_path = less_path.replace("'","")
        if color: 
            
            with open(less_path, 'r') as file:
                data = file.readlines()
                file.close()
            # now change the 2nd line, note that you have to add a newline
            data[16] = '@brand-primary:            %s;\n'%color
            data[18] = '@brand-info:            %s;\n'%color
            # and write everything back
            try:
                file =  open(less_path, 'w') 
                
            except Exception as e:
                _logger.warning('---------------------e (%s).', e)
            with open(less_path, 'w') as file:
                file.writelines( data )
                file.close()
                res.append({'res':1})
        else:
            res.append({'res':0})
        return http.request.make_response(json.dumps(res)) 
    
    
    