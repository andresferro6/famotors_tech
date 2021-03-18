# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:10:07 2021

@author: User
"""

# =============================================================================
# 
# =============================================================================
import qrcode
# Link for website
input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')

# =============================================================================
# 
# =============================================================================
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('You are the love of my life')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('angela.png')

# =============================================================================
# 
# =============================================================================
import qrcode
from datetime import datetime

frame = {
          'codigo_ingreso': ['id_unico_buscar_base'], 
          'hora_ingreso': [str(datetime.now())],
          'placa': ['JIZ768'],
          'tipo_vehiculo': ['CARRO']
        }

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(frame)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('dataframe.png')





