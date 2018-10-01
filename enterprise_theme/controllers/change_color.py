    #-*- coding: utf-8 -*-
from odoo import http, _
import logging
import random
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
        _logger.warning('---------------------color (%s).', color)
        print('-------------color',color)
        if os.name == 'nt':
            less_path = repr(__file__).replace('controllers','static')
            less_path = less_path.replace('change_color.py','src\\less\\variables.less')
            less_path = less_path.replace('\\\\','\\')
            less_path = less_path.replace("'","")
            
        else:
            less_path = repr(__file__).replace('/controllers/change_color.py','/static/src/less/variables.less')
            less_path = less_path.replace("'","")
        _logger.warning('---------------------less_path (%s).', less_path)
        if color: 
            
            with open(less_path, 'r') as file:
                data = file.readlines()
                file.close()
            _logger.warning('---------------------data (%s).', data[16])
            print ("color1 " , data[16])
            print ("color2 " , data[18])
            # now change the 2nd line, note that you have to add a newline
            data[16] = '@brand-primary:            %s;\n'%color
            data[18] = '@brand-info:            %s;\n'%color
            # and write everything back
            
            with open(less_path, 'w') as file:
                _logger.warning('---------------------data (%s).', data[18])
                file.writelines( data )
                file.close()
                res.append({'res':1})
        else:
            res.append({'res':0})
        _logger.warning('---------------------res (%s).', res)
        return http.request.make_response(json.dumps(res)) 
    
    
    