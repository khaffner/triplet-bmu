# -*- coding: utf-8 -*-
"""
"""
import ev_diag
from sys import exit
import serial
import configuration as cc

ev_diag.serport = cc.config['DEFAULT']['Port']

try:
    ev_diag.connect()
    ev_diag.serialcon.do_setup(ev_diag.triplet_setup)
    ev_diag.ion.read_bmu_data(ev_diag.serialcon)
    ev_diag.ion.calculate_values()
    ev_diag.serialcon.reset()
    ev_diag.disconnect()
except serial.SerialException:
    print(cc.output_as_str('con error'))
    input(cc.output_as_str('enter2cont'))

ev_diag.ion.save_bmu_data()