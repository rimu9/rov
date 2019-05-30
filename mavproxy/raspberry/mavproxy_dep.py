#!/usr/bin/env python
'''depthmodules'''

import time, math, os
import ms5837
from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

sensor = ms5837.MS5837_30BA()

class DepModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(DepModule, self).__init__(mpstate, "dep", "test send module")
        self.dep_value = 9.02
        self.dep_show = 0
        self.dep_falg = 0
       # if not sensor.init():
       #     print "could not init"
       #     exit(1)
       # if not sensor.read():
       #     print "read error"
       #     exit(1)
       # self.freshwaterdepth = sensor.depth()
       # sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
       # self.saltwaterdepth = sensor.depth()
        self.add_command('dep', self.cmd_dep, 'send depth msg')
        self.add_command('spdep', self.cmd_spdep, 'stop send')
        time.sleep(5)


    def cmd_dep(self, args):
        '''send msg'''
        self.dep_falg = 1
        ok = 1
        if self.dep_falg:
           # sensor.read()
           # self.dep_value = sensor.depth()
            if ok:
                print ("depth : %0.2f") % (9.02)
                print "started"
                ok = 0
            self.master.mav.dep_msg_send(self.dep_value, 1)


    def cmd_spdep(self, args):
        '''stop send msg'''
        self.falg = 0
        print ("depth_show= %0.2f") % (self.dep_show)
        # print "stoped"


    def mavlink_packet(self, m):
        '''handle a mavlink packet'''
        mtype = m.get_type()
        if mtype == "DEP_REC":
            self.dep_show = m.dep_rec
            # print ("receive depth: %0.2f") % (m.depth)
            # print "receive succeed"


def init(mpstate):
    '''init module'''
    return DepModule(mpstate)
