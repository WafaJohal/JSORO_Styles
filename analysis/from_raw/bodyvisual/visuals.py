from visual import *
from visual.graph import *
from visual.controls import *
import numpy as np
from utils import *
'''
Created on 5 nov. 2015

@author: wafajohal
'''

class Visual3D:
    def __init__(self):
        
        scene.select()
        scene.background = (0, 0, 0)
        scene.center
        scene.userspin = True
        self.drawInitScene()
        self.joints = []
        self.c1 = curve(pos=vector(0,0,0),radius=0.03)
        self.c2 = curve(pos=vector(0,0,0),radius=0.03)
        self.c3 = curve(pos=vector(0,0,0),radius=0.03)
        for j in map_joints:
            if j ==0 :
                self.joints.append(sphere(pos=vector(0, 0, 0), radius=0.06, color=color.blue))
            else:
                self.joints.append(sphere(pos=vector(0, 0, 0), radius=0.06, color=color.white))
      
    def drawInitScene(self):
        checkerboard = ((0, 1, 0, 1),
                 (1, 0, 1, 0),
                 (0, 1, 0, 1),
                 (1, 0, 1, 0))
        tex = materials.texture(data=checkerboard,
                     mapping="rectangular",
                     interpolate=False)
        box(axis=(0, 0, 1), color=color.cyan, material=tex)  
     
    def drawBody(self,jointp):
        self.c1.pos = [ self.joints[11].pos,
                   self.joints[10].pos, 
                   self.joints[9].pos, 
                   self.joints[8].pos,
                   self.joints[21].pos,
                   self.joints[2].pos,
                   self.joints[1].pos,
                   self.joints[0].pos, 
                   self.joints[17].pos,
                   self.joints[18].pos,
                   self.joints[19].pos,
                   self.joints[20].pos
                   ]
        self.c2.pos=[self.joints[21].pos,
                   self.joints[4].pos, 
                   self.joints[5].pos, 
                   self.joints[6].pos,
                   self.joints[7].pos
                   ]
        self.c3.pos=[self.joints[0].pos,
                   self.joints[12].pos,
                   self.joints[13].pos, 
                   self.joints[14].pos, 
                   self.joints[15].pos,
                   ]
        return
     
    def updateVisuals(self, jointp):
        for j in map_joints:
            self.joints[j].pos = vector(jointp[j])
            #self.drawBody(self.joints)
        
    def updateVisualIdx(self, idx, all_data):
        (metainfo, tstp, time_rel, jointp, jointo) = all_data[idx]
        print(jointp)
        for j in map_joints:
            self.joints[j].pos = vector(jointp[j])
     
class visualFeatures:
    def _init_(self,featureSet):
        self.featureSet=featureSet
    
    
