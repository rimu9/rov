#!/usr/bin/env python
'''module depth'''

import time, math, os
from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

class DepModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(DepModule, self).__init__(mpstate, "dep", "test receive")
        self.depth = 0
        self.dep_send = 6.6
        self.add_command('dep', self.cmd_dep, "show depth information")


    def cmd_dep(self, args):
        '''show depth value'''
        print("depth : %0.2f") % (self.depth)
        self.master.mav.dep_msg_send(self.dep_send, 1)


    def mavlink_packet(self, m):
        '''handle a mavlink packet'''
        mtype = m.get_type()
        if mtype == "DEP_REC":
            self.depth = m.dep_rec
            print "receive successfully"


def init(mpstate):
    '''initialize module'''
    return DepModule(mpstate)
