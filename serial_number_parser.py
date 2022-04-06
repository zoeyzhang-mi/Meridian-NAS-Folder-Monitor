# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:22:15 2020

@author: William
"""
import numpy as np
import argparse
import os
#import sys

def parse_args(sn):
    parser = argparse.ArgumentParser()
    parser.add_argument('-sn','--serial_number', default=sn, 
                        type=str, help='serial number of the module in hex')
    parser.add_argument('-mpi','--from_mpi', default=False,
                        type=bool, help='is serial number from mpi output')
    parser.add_argument('--data_dir', default=os.path.join('wafermap'), 
                        type=str, help='directory of the data')
    parser.add_argument('--wafermap', default='bobcat45wafermap.npy', 
                        type=str, help='directory of the data')
    return parser.parse_args()

def serial_parser(args):
    mapping = np.load(os.path.join(args.data_dir, args.wafermap))
    serial = args.serial_number
    if serial[:2] == 'SN':
        serial = serial[2:]
    if args.from_mpi:
        year = int(serial[:2])
        week = int(serial[2:4])
        location = int(serial[4:6])
    else:
        year = int(serial[:2],16)
        week = int(serial[2:4],16)
        location = int(serial[4:6],16)
    wafer, die = divmod(int(serial[-6:],16)+6250, 250)
    coord = mapping[die]
    x = coord[0]
    y = coord[1]
    del mapping
    return year, week, location, wafer, die, x, y
    
if __name__=='__main__':
    #sys.argv=[""]
    args = parse_args('SN14220100AEF1')
    
    year, week, location, wafer_num, die, x, y = serial_parser(args)
    print('Year:', year, '| Week:', week, '| Location:', location, 
          '| Wafer number:', wafer_num, '| x_coordinate:', x, 
          '| y_coordinate:', y)
    