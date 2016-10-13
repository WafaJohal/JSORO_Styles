import csv
from utils import *
import math
import numpy as np
from visual import *
from visual.graph import *
from visual.controls import *
from visuals import *
import operator
from transformations import*
'''
Created on 14 nov. 2015

@author: wafajohal
'''
types=["dynamic","static"]

print('script big')


class BodyAnalysis():

    def __init__(self,fname):
        self.fname= fname
        self.all_data=[]
        self.features={}
        self.loadCSVtoVar()
        self.visual3D = Visual3D()
        self.demo = sphere(pos=(0,0,0),color=color.green, radius=0.03)
        self.weights= [0] * 25
        self.weights[1] = 39.7
        self.weights[8] = 5.8
        self.weights[9] = 2.6
        self.weights[10] = 1.6
        self.weights[4] = 5.8
        self.weights[5] = 2.6
        self.weights[6] = 1.6
        self.weights[16] = 10
        self.weights[17] = 4.6
        self.weights[18] = 1.45
        self.weights[12] = 10
        self.weights[13] = 4.6
        self.weights[14] = 1.45
        self.weights[3] = 8.2
        #print(sum(self.weights))
        self.f1 = gcurve(color=color.yellow)
        self.f2 = gcurve(color=color.cyan)
        self.mybox= box(pos=(0,0,0), length=0, height=0, width=0, opacity=0.5, color=color.red)
        self.extremities= [11 , #map_joints["JointType_HandRight"],
                           7, #map_joints["JointType_HandLeft"],
                           3, #map_joints["JointType_Head"],
                           19, #map_joints["JointType_FootRight"],
                           15]# map_joints["JointType_FootLeft"]]

        pass

    def loadCSVtoVar(self):
        csvfile = open(self.fname, 'r')
        bodyfreader = csv.DictReader(csvfile, header)
        bodyfreader.next()
        for row in bodyfreader:
            jointsP = []
            jointsO = []
            self.cleanRow(row)
            for j in map_joints:
            # print("----------------")
                nx = map_joints[j].replace('JointType_', 'JointP_') + '_X'
                ny = map_joints[j].replace('JointType_', 'JointP_') + '_Y'
                nz = map_joints[j].replace('JointType_', 'JointP_') + '_Z'
                nox = map_joints[j].replace('JointType_', 'JointO_') + '_X'
                noy = map_joints[j].replace('JointType_', 'JointO_') + '_Y'
                noz = map_joints[j].replace('JointType_', 'JointO_') + '_Z'
                now = map_joints[j].replace('JointType_', 'JointO_') + '_W'
                # if(row[nx]!='' and row[ny]!='' and row[nz]!='' and row[nx]!='NA' and row[ny]!='NA' and row[nz]!='NA' ):
                x = float(row[nx])
                y = float(row[ny])
                z = float(row[nz])
                jointsP.append((x, y, z))
                # if(row[nox]!='' and row[noy]!='' and row[noz]!='' and row[nx]!='NA' and row[ny]!='NA' and row[nz]!='NA' ):
                ox = float(row[nox])
                oy = float(row[noy])
                oz = float(row[noz])
                if row[now] :
                    ow = float(row[now])
                else :
                    ow = 0

                jointsO.append((ox, oy, oz, ow))
            self.all_data.append(((row['style'], row['child'], row['session'], row['activity'], row['versatility']), float(row['time']), float(row['time_rel']), jointsP, jointsO))
        self.idx=0
        csvfile.close()

    def cleanRow(self,row):
        for key, value in row.items():
            if(value=='' or value=='NA'):
                row[key] = '0'


    def playData(self):
        print("play data")
        fname='/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/all_ske_feat.csv'
        with open(fname, 'w+') as f:  # Just use 'w' mode in 3.x
            (metainfo, tstp, time_rel, jointp, jointo) = self.all_data[0]
            (style, child, session, activity, versatility)  = metainfo
            print(metainfo)
            self.features.update({"activity":activity})
            self.features.update({"session":session})
            self.features.update({"versatility":versatility})
            self.features.update({"child":child})
            self.features.update({"style":style})
            self.features.update({"time":tstp})
            self.features.update({"time_rel":time_rel})
            self.computeFeatures(0)
            w = csv.DictWriter(f, self.features.keys())
            w.writeheader()
            for i in range(len(self.all_data)-1):
                print("==========", i)
                #rate(150)
                (metainfo, tstp, time_rel, jointp, jointo) = self.all_data[i]
                (style, child, session, activity, versatility) = metainfo
                print(metainfo)
                self.features.update({"activity":activity})
                self.features.update({"session":session})
                self.features.update({"versatility":versatility})
                self.features.update({"child":child})
                self.features.update({"style":style})
                self.features.update({"time":tstp})
                self.features.update({"time_rel":time_rel})
                #print(jointp)
                #self.visual3D.updateVisuals(jointp)
                self.computeFeatures(i)
                #self.plotFeature(1,"volume",i)
                #print(self.features)
                #if( self.idx-2>=0 and self.idx+2 < len(self.all_data)):
                    #(value,type) = self.features["jerk"]
                    #self.demo.pos=value
                    #self.plotFeature(1,"jerk_JointType_HandRight",self.idx)
                    #self.plotFeature(2, "jerk_JointType_HandLeft",self.idx)
                #print(self.features.keys())
                w.writerow(self.features)


#def writeFeaturesToCSV(self,fname):



    def computeFeatures(self,idx):
        (metainfo, tstp, time_rel, joints, jointo) = self.all_data[idx]
        if( idx-1>=0 or idx+1 < len(self.all_data)):
            (metainfo0, tstp0, time_rel0, joints0, jointo0) = self.all_data[idx-1]
            (metainfo2, tstp2, time_rel2, joints2, jointo2) = self.all_data[idx+1]
            self.computeWholeBodyAcc(self.all_data[idx -1], self.all_data[idx], self.all_data[idx+1])
            self.computeWholeBodyVel(self.all_data[idx -1], self.all_data[idx+1])
            self.computeWholeQoM(self.all_data[idx -1], self.all_data[idx+1])
            self.computeWholeQoM3D(self.all_data[idx -1], self.all_data[idx+1])
            self.computeheadMotionVel(time_rel0, jointo0[2], time_rel2, jointo2[2])
            if( idx-2>=0 or idx+2 < len(self.all_data)-1):
                self.computeWholeBodyJerk(self.all_data[idx+2],self.all_data[idx+1],self.all_data[idx-1],self.all_data[idx-2])

        else:
            if( idx-2>=0 or idx+2 < len(self.all_data)):
                for j in range(len(map_joints)):
                    name="jerk_"+map_joints[j]
                    self.features.update({name:'NA'})
            else:
                for j in range(len(map_joints)):
                    name="acc_"+map_joints[j]
                    self.features.update({name:'NA'})
                    name="vel_"+map_joints[j]
                    self.features.update({name:'NA'})
            self.features.update({'QoM':'NA'})
            self.features.update({'QoM3D':'NA'})
            self.features.update({'headNod':'NA'})
            self.features.update({'headShake':'NA'})


        com =self.computeCOM(joints)
        self.computeVolume(self.computeBoundingBox(joints))
        self.computeExtensiveness(joints, com)
        self.computeheadMotion(jointo[2])
        self.computeShoulderEr(joints[2],joints[8],joints[4], joints[9],joints[5])
        self.computeTorsoLeaningAngle(joints[2],joints[0])
        legsjoints=[joints[i] for i in [16,17,18,19,12,13,14,15]]
        self.computeLegExtensivenss(legsjoints)
        self.computeJointDistance(joints)
        self.computeBodyDistances(joints)
        self.computeDisplacements(joints)
        self.computeAsymetries(joints)


        ##TODO computer per period feratures

        #
        #print(self.features["com"])

    ''' TOOLS FUNCTIONS'''
    def plotFeature(self, id, featname,time_rel):
        value = self.features[featname]
        if(id==1):
            self.f1.plot(pos=(time_rel,value))
        else :
            self.f2.plot(pos=(time_rel,value))

    def distance(self, jointa, jointb):
        (xa,ya,za)= jointa
        (xb, yb, zb)= jointb
        return math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)+(zb-za)*(zb-za))

    def distance2D(self, jointa, jointb):
        (xa, za)= jointa
        (xb, zb)= jointb
        return math.sqrt((xb-xa)*(xb-xa)+(zb-za)*(zb-za))

    def rotation(self, jointOa, jointOb):
        return np.vdot(jointOa, jointOb)

    def eucledian(self, jointO):
        (x,y,z,w)=jointO
        return euler_from_quaternion((w,x,y,z), axes='sxyz')

    def relativeJointAngle(self,jp1,jpcenter,jp2):
        (x1,y1,z1)=jp1
        (xc,yc,zc)=jpcenter
        (x2,y2,z2)=jp2
        v1 = (x1-xc, y1-yc, z1-zc)
        v2 = (x2-xc, y2-yc, z2-zc)
        cosang = np.dot(v1,v2)
        sinang = np.linalg.norm(np.cross(v1, v2))
        return np.arctan2(sinang, cosang)

    ''' Features '''
    ''' VELOCITY OF MOTION'''
    def computeVelocity(self,t2, pt2, t0, pt0):
        (vx,vy,vz) = self.computeVelocity3D(t2,pt2, t0, pt0)
        velocity = math.sqrt(vx*vx+vy*vy+vz*vz)
        return velocity

    def computeVelocity3D(self,time2, pt2, time0, pt0):
        (x2, y2, z2)=pt2
        (x0, y0, z0)=pt0
        dt = time2-time0
        if(dt==0):
            dt=1
        vx=x2-x0/(2*dt)
        vy=y2-y0/(2*dt)
        vz=z2-z0/(2*dt)
        return (vx,vy,vz)

    def computeWholeBodyVel(self,data_m1,data_p1):
        (metainfo0, tstp0, time_rel0, joints0, jointo0) = data_m1
        (metainfo2, tstp2, time_rel2, joints2, jointo2) = data_p1
        for j in range(len(map_joints)):
            velocity = self.computeVelocity(time_rel2,joints2[j] , time_rel0,joints0[j])
            name="vel_"+map_joints[j]
            self.features.update({name:velocity})

    ''' ACCELERATION OF MOTION'''
    def computeAcceleration(self,time2, p2, time0, p0, time1, p1):
        (ax,ay,az)= self.computeAcceleration3D(time2, p2, time0, p0, time1, p1)
        return math.sqrt(ax*ax+ay*ay+az*az)

    def computeAcceleration3D(self,time2, p2, time0, p0, time1, p1):
        dt= time2-time0
        (x2, y2, z2) = p2
        (x1, y1, z1) = p1
        (x0, y0, z0) = p0
        if(dt==0):
            dt=1
        ax=(x2-2*x1+x0)/(dt*dt)
        ay=(y2-2*y1+y0)/(dt*dt)
        az=(z2-2*z1+z0)/(dt*dt)
        return (ax,ay,az)

    def computeWholeBodyAcc(self,data_m1,data_0, data_p1):
        (metainfo0, tstp0, time_rel0, joints0, jointo0) = data_m1
        (metainfo1, tstp1, time_rel1, joints1, jointo1) = data_0
        (metainfo2, tstp2, time_rel2, joints2, jointo2) = data_p1
        for j in range(len(map_joints)):
            acceleration = self.computeAcceleration(time_rel2,joints2[j] , time_rel0,joints0[j], time_rel1,joints1[j])
            name="acc_"+map_joints[j]
            self.features.update({name:acceleration})

    ''' JERKINESS OF MOTION'''
    def computeJerk(self,pt2, pt1, pt_1, pt_2):
        (time2, (x2, y2, z2))=pt2
        (time1, (x1, y1, z1))=pt1
        (time_1, (x_1, y_1, z_1))=pt_1
        (time_2, (x_2, y_2, z_2))=pt_2
        dt=time2-time_2
        if(dt==0):
            dt=1
        jx = (x2 - 2*x1 + 2*x_1 - x_2)/dt
        jy = (y2 - 2*y1 + 2*y_1 - y_2)/dt
        jz = (z2 - 2*z1 + 2*z_1 - z_2)/dt
        return math.sqrt(jx*jx + jy*jy + jz*jz)

    def computeWholeBodyJerk(self,data_p2,data_p1, data_m1, data_m2):
        (metainfop2, tstpp2, time_relp2, jointsp2, jointop2) = data_p2
        (metainfop1, tstpp1, time_relp1, jointsp1, jointop1) = data_p1
        (metainfom1, tstpm1, time_relm1, jointsm1, jointom1) = data_m1
        (metainfom2, tstpm2, time_relm2, jointsm2, jointom2) = data_m2
        for j in range(len(map_joints)):
            jerk = self.computeJerk((time_relp2,jointsp2[j]) , (time_relp1,jointsp1[j]), (time_relm1,jointsm1[j]), (time_relm2,jointsm2[j]))
            name="jerk_"+map_joints[j]
            self.features.update({name:jerk})

    ''' QUANTITY OF MOTION'''
    def computeQoM3D(self, t2, jointpt2, t0,jointpt0):
        qom=(0.0,0.0,0.0)
        for i in range(len(jointpt2)):
            b= tuple([self.weights[i]*v for v in self.computeVelocity3D(t2, jointpt2[i], t0,jointpt0[i])])
            a= qom
            qom = tuple(map(operator.add, a, b))
        qom= tuple([a/sum(self.weights) for a in qom])
        return qom

    def computeWholeQoM3D(self,data_m1,data_p1):
        (metainfo0, tstp0, time_rel0, joints0, jointo0) = data_m1
        (metainfo2, tstp2, time_rel2, joints2, jointo2) = data_p1
        (x,y,z)= self.computeQoM3D(time_rel2, joints2, time_rel0,joints0)
        self.features.update({"QoM3D_x":x})
        self.features.update({"QoM3D_y":y})
        self.features.update({"QoM3D_z":z})

    def computeQoM(self,t2,jointpt2,t0 ,jointpt0):
        qom=0.0
        for i in range(len(jointpt2)):
            qom += self.weights[i]*self.computeVelocity(t2,jointpt2[i], t0, jointpt0[i])
        qom/= sum(self.weights)
        return qom

    def computeWholeQoM(self,data_m1,data_p1):
        (metainfo0, tstp0, time_rel0, joints0, jointo0) = data_m1
        (metainfo2, tstp2, time_rel2, joints2, jointo2) = data_p1
        self.features.update({"QoM":self.computeQoM(time_rel2,joints2,time_rel0, joints0)})

    ''' BOUDING BOX'''
    def computeBoundingBox(self,joints):
        minx= min([joint[0] for joint in joints])
        maxx= max([joint[0] for joint in joints])
        miny= min([joint[1] for joint in joints])
        maxy= max([joint[1] for joint in joints])
        minz= min([joint[2] for joint in joints])
        maxz= max([joint[2] for joint in joints])
        #self.features.update({"boundingBox":minx, maxx, miny, maxy, minz, maxz),"visual",box)})
        return (minx, maxx, miny, maxy, minz, maxz)

    ''' VOLUME'''
    def computeVolume(self,boundingbox):
        (minx, maxx, miny, maxy, minz, maxz)=boundingbox
        volume=math.sqrt((maxx-minx)*(maxx-minx) + (maxy-miny)*(maxy-miny) + (maxz-minz)*(maxz-minz))
        self.features.update({"volume":volume})
        #self.features.update({"bbox":(minx, maxx, miny, maxy, minz, maxz)})
        self.features.update({"bbox_minx":minx})
        self.features.update({"bbox_maxx":maxx})
        self.features.update({"bbox_miny":miny})
        self.features.update({"bbox_maxy":maxy})
        self.features.update({"bbox_minz":minz})
        self.features.update({"bbox_maxz":maxz})
        return volume

    ''' CENTER OF MASS'''
    def CoM(self,jointsweights,joints):
        com=(0.0,0.0,0.0)
        for i in range(len(jointsweights)):
            b= tuple([jointsweights[i]*a for a in joints[i]])
            a= com
            com = tuple(map(operator.add, a, b))
        com= tuple([a/sum(jointsweights) for a in com])
        return com

    def computeCOM(self,joints):
        (comx,comy,comz) = self.CoM(self.weights, joints)
        self.features.update({"com_x":comx})
        self.features.update({"com_y":comy})
        self.features.update({"com_z":comz})
        return (comx,comy,comz)


    # this is computed for a whole period of time
    ''' DISTANCE COVERED BY COM '''
    def computeDistanceCovered(self,idmin, idmax):
        p0 =(0.0,1.5)
        distance =0.0
        for i in range(idmin, idmax):
            (metainfo, tstp, time_rel, joints, jointo) = self.all_data[i]
            (x,y,z) = self.COM(self.weights,joints)
            distance+= self.distance2D(p0, (x,z))
        self.features.update({"distanceCOM":distance})
        return distance

    ''' AREA COVERED BY COM '''
    def computeAreaCovered(self,idmin, idmax):
        minx= 0.0
        maxx = 0.0
        minz = 1.5
        maxz = 1.5
        for i in range(idmin, idmax):
            (metainfo, tstp, time_rel, joints, jointo) = self.all_data[i]
            (x,y,z) = self.COM(self.weights,joints)
            if(x<= minx):
                minx = x
            if(z<= minz):
                minx = x
            if(x>= maxx):
                maxx = x
            if(z>= maxz):
                maxz = x
        self.features.update({"distanceCOM":(minx,maxx,minz,maxz)})
        return (minx,maxx,minz,maxz)

    ''' EXTENSIVENESS MAX '''
    def extensivenessMax(self, extremities_joints, com):
        max=0
        #print(com)
        for joint in extremities_joints:
            if(self.distance(joint,com)>=max):
                max=self.distance(joint,com)
        return max

    ''' EXTENSIVENESS WEIGHTED SUM'''
    def extensivenessWSum(self,extremities_joints, com):
        sum=0
        for joint in extremities_joints:
            sum+=self.distance(joint,com)
        return sum

    def computeExtensiveness(self,joints, com):
        extremities_joints = [joints[i] for i in self.extremities]
        max= self.extensivenessMax(extremities_joints,com)
        self.features.update({"extensiveMax":max})
        sum= self.extensivenessWSum(extremities_joints,com)
        self.features.update({"extensiveWSum":sum})
        return max,sum

    ''' HEAD SHAKES  & NODS'''
    def computeheadMotion(self, head_jointo):
        (x,y,z)= self.eucledian(head_jointo)
        print(x,y,z)
        head_shake = y
        head_nods = x
        self.features.update({"headNod":head_nods})
        self.features.update({"headShake":head_shake})
        return (head_nods,head_shake)

    def computeheadMotionVel(self, t0, head_jointo0, t2, head_jointo2):
        (x0,y0,z0)= self.eucledian(head_jointo0)
        (x2,y2,z2)= self.eucledian(head_jointo2)
        print(x0,y0,z0)
        (x,y,z) = self.computeVelocity3D(t2, (x2,y2,z2), t0, (x0,y0,z0))
        self.features.update({"headVel_x":x})
        self.features.update({"headVel_y":y})
        self.features.update({"headVel_z":z})
        return (x,y,z)

    ''' SHOULDER ERECTION'''
    def computeShoulderEr(self,jneck,jshouldR, jshouldL, jelbowR, jelbowL):
        leftang = self.relativeJointAngle(jelbowL, jshouldL, jneck)
        rightang = self.relativeJointAngle(jelbowR, jshouldR, jneck)
        averageang = (leftang+rightang) /2
        self.features.update({"shouldersAnim":averageang})
        return averageang

    ''' TORSO LEAN ANGLE'''
    def computeTorsoLeaningAngle(self,jneck,jspine):
        (xs,ys,zs)= jspine
        (xn,yn,zn)= jneck
        vert = (xs,yn,zs)
        leanangle= self.relativeJointAngle(jneck,jspine, vert)
        self.features.update({"torsoLean":leanangle})
        return leanangle

    ''' LEGS EXTENSIVENESS '''
    def computeLegExtensivenss(self, legjoints):
        legsweights = [10,15,15,10,10,15,15,10]
        legsCoM= self.CoM(legsweights,legjoints)
        extremities_joints = [legjoints[1],legjoints[2],legjoints[3],legjoints[5],legjoints[6],legjoints[7]]
        max = self.extensivenessMax( extremities_joints, legsCoM)
        sum = self.extensivenessWSum( extremities_joints, legsCoM)
        self.features.update({"legsExtensiveMax":max})
        self.features.update({"legsExtensiveWSum":sum})
        return max,sum

    ''' SOME JOINTS BODY DISTANCE'''
    def computeJointDistance(self, joints):
        elbowsd = (self.distance(joints[5], joints[0]))+(self.distance(joints[9], joints[0]))/2
        self.features.update({"elbowDist":elbowsd})
        handd = (self.distance(joints[7], joints[0]))+(self.distance(joints[11], joints[0]))/2
        self.features.update({"handDist":handd})
        return elbowsd, handd

    ''' LATERAL AND FRONTAL BODY DISTANCES '''
    def computeBodyDistances(self,joints):
        fdistance = 0.0
        ldistance = 0.0
        for joint in joints:
            (x,y,z) = joint
            fdistance += z
            ldistance += x
        fdistance /= len(joints)
        ldistance /= len(joints)
        self.features.update({"frontalDistance":fdistance})
        self.features.update({"lateralDistance":ldistance})
        return fdistance, ldistance

    ''' DISPLACEMENT OF SOME JOINTS REGARDING THEIR ROOT JOINT'''
    def computeDisplacements(self,joints):
        feetD= (self.distance(joints[15], joints[0])+self.distance(joints[17], joints[0]))/2
        handD= (self.distance(joints[11], joints[9])+self.distance(joints[7], joints[4]))/2
        headD= self.distance(joints[3], joints[2])
        self.features.update({"feetDispl":feetD})
        self.features.update({"handDispl":handD})
        self.features.update({"headDispl":headD})
        return feetD,handD,headD

    def actionPresence(self,joints1,joints0, epsilon=90):
        action=[]
        for j1,j0 in (joints1,joints0):
            if(self.distance(j1,j0)>epsilon):
                action.append(1)
            else:
                action.append(0)
        return action


    #def computeAlignement(self):
    ''' COMPUTE ASYMETRIES OF JOINTS'''
    def computeAsymetry(self,joint1, joint2, jointr1, jointr2):
        (x1,y1,z1)=joint1
        (xr1,yr1,zr1)=jointr1
        (x2,y2,z2)=joint2
        (xr2,yr2,zr2)=jointr2
        v1 = (x1-xr1, y1-yr1, z1-zr1)
        v2 = (x2-xr2, y2-yr2, z2-zr2)
        asym=  np.dot(v1,v2)
        return asym

    def computeAsymetries(self, joints):
        elbowAsym = self.computeAsymetry(joints[5], joints[9], joints[4], joints[8])
        self.features.update({"elbowAsym":elbowAsym})
        handAsym = self.computeAsymetry(joints[7], joints[11], joints[4], joints[8])
        self.features.update({"handAsym":handAsym})
        wristAsym = self.computeAsymetry(joints[6], joints[10], joints[4], joints[8])
        self.features.update({"wristAsym":wristAsym})
        footAsym = self.computeAsymetry(joints[15], joints[19], joints[12], joints[16])
        self.features.update({"footAsym":footAsym})
        ankleAsym = self.computeAsymetry(joints[14], joints[18], joints[12], joints[16])
        self.features.update({"ankleAsym":ankleAsym})
        kneeAsym = self.computeAsymetry(joints[13], joints[17], joints[12], joints[16])
        self.features.update({"kneeAsym":kneeAsym})
        return elbowAsym,handAsym,wristAsym,footAsym,ankleAsym,kneeAsym

    def computeHandTouch(self,joints, handidx):
            threshold = self.distance(joints[handidx],joints[handidx-1])*2
            hand_arr=[]
            fdistance=0.0
            hand_joint = joints[handidx];
            for j in  range(len(map_joints) - 4):
                if(j!=handidx and j!=handidx-1 and j!=handidx-2):
                    distance = self.distance(hand_joint,joints[j]);
                    if fdistance <=threshold :
                        hand_arr.push_back(joints[j])
            return hand_arr


    def computeEclueadianAngles(self,x, y, z, w):
        rollx = math.atan((2*(x*y + z*w))/(1-2*(y*y + z*z))) #x
        pitchy = asin(2*(x*z - y*w)) #y
        yawz= atan((2*(x*w + y*z))/(1-2*(w*w + z*z))) #z
        return (rollx, pitchy, yawz)






print("hello")
#fname="~/Dropbox/DATA/STYLEBOT/postures_fulls.csv"
fname="/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_all.csv"
#fname="/Users/wafajohal/Dropbox/DATA/STYLEBOT/child4_dance.csv"
print(fname)
boda=BodyAnalysis(fname)
boda.idx = 0
boda.playData()
