from visual import *
from visual.graph import *
from visual.controls import *
import numpy as np
import csv
from visual_common.controls import button

map_joints={0:"JointType_SpineBase", 1:"JointType_SpineMid", 2:
"JointType_Neck", 3:"JointType_Head", 4:"JointType_ShoulderLeft", 5:
"JointType_ElbowLeft", 6:"JointType_WristLeft", 7:
"JointType_HandLeft", 8:"JointType_ShoulderRight", 9:
"JointType_ElbowRight", 10:"JointType_WristRight", 11:
"JointType_HandRight", 12:"JointType_HipLeft", 13:
"JointType_KneeLeft", 14:"JointType_AnkleLeft", 15:
"JointType_FootLeft", 16:"JointType_HipRight", 17:
"JointType_KneeRight", 18:"JointType_AnkleRight", 19:
"JointType_FootRight", 20:"JointType_SpineShoulder", 21:
"JointType_HandTipLeft", 22:"JointType_ThumbLeft", 23:
"JointType_HandTipRight", 24:"JointType_ThumbRight"}
header = ("","X.1","X","activity","style","versatility","session","child","time","id","nb_ske","JointP_SpineBase_X","JointP_SpineMid_X","JointP_Neck_X","JointP_Head_X","JointP_ShoulderLeft_X","JointP_ElbowLeft_X","JointP_WristLeft_X","JointP_HandLeft_X","JointP_ShoulderRight_X","JointP_ElbowRight_X","JointP_WristRight_X","JointP_HandRight_X","JointP_HipLeft_X","JointP_KneeLeft_X","JointP_AnkleLeft_X","JointP_FootLeft_X","JointP_HipRight_X","JointP_KneeRight_X","JointP_AnkleRight_X","JointP_FootRight_X","JointP_SpineShoulder_X","JointP_HandTipLeft_X","JointP_ThumbLeft_X","JointP_HandTipRight_X","JointP_ThumbRight_X","JointO_SpineBase_X","JointO_SpineMid_X","JointO_Neck_X","JointO_Head_X","JointO_ShoulderLeft_X","JointO_ElbowLeft_X","JointO_WristLeft_X","JointO_HandLeft_X","JointO_ShoulderRight_X","JointO_ElbowRight_X","JointO_WristRight_X","JointO_HandRight_X","JointO_HipLeft_X","JointO_KneeLeft_X","JointO_AnkleLeft_X","JointO_FootLeft_X","JointO_HipRight_X","JointO_KneeRight_X","JointO_AnkleRight_X","JointO_FootRight_X","JointO_SpineShoulder_X","JointO_HandTipLeft_X","JointO_ThumbLeft_X","JointO_HandTipRight_X","JointO_ThumbRight_X","JointP_SpineBase_Y","JointP_SpineMid_Y","JointP_Neck_Y","JointP_Head_Y","JointP_ShoulderLeft_Y","JointP_ElbowLeft_Y","JointP_WristLeft_Y","JointP_HandLeft_Y","JointP_ShoulderRight_Y","JointP_ElbowRight_Y","JointP_WristRight_Y","JointP_HandRight_Y","JointP_HipLeft_Y","JointP_KneeLeft_Y","JointP_AnkleLeft_Y","JointP_FootLeft_Y","JointP_HipRight_Y","JointP_KneeRight_Y","JointP_AnkleRight_Y","JointP_FootRight_Y","JointP_SpineShoulder_Y","JointP_HandTipLeft_Y","JointP_ThumbLeft_Y","JointP_HandTipRight_Y","JointP_ThumbRight_Y","JointO_SpineBase_Y","JointO_SpineMid_Y","JointO_Neck_Y","JointO_Head_Y","JointO_ShoulderLeft_Y","JointO_ElbowLeft_Y","JointO_WristLeft_Y","JointO_HandLeft_Y","JointO_ShoulderRight_Y","JointO_ElbowRight_Y","JointO_WristRight_Y","JointO_HandRight_Y","JointO_HipLeft_Y","JointO_KneeLeft_Y","JointO_AnkleLeft_Y","JointO_FootLeft_Y","JointO_HipRight_Y","JointO_KneeRight_Y","JointO_AnkleRight_Y","JointO_FootRight_Y","JointO_SpineShoulder_Y","JointO_HandTipLeft_Y","JointO_ThumbLeft_Y","JointO_HandTipRight_Y","JointO_ThumbRight_Y","JointP_SpineBase_Z","JointP_SpineMid_Z","JointP_Neck_Z","JointP_Head_Z","JointP_ShoulderLeft_Z","JointP_ElbowLeft_Z","JointP_WristLeft_Z","JointP_HandLeft_Z","JointP_ShoulderRight_Z","JointP_ElbowRight_Z","JointP_WristRight_Z","JointP_HandRight_Z","JointP_HipLeft_Z","JointP_KneeLeft_Z","JointP_AnkleLeft_Z","JointP_FootLeft_Z","JointP_HipRight_Z","JointP_KneeRight_Z","JointP_AnkleRight_Z","JointP_FootRight_Z","JointP_SpineShoulder_Z","JointP_HandTipLeft_Z","JointP_ThumbLeft_Z","JointP_HandTipRight_Z","JointP_ThumbRight_Z","JointO_SpineBase_Z","JointO_SpineMid_Z","JointO_Neck_Z","JointO_Head_Z","JointO_ShoulderLeft_Z","JointO_ElbowLeft_Z","JointO_WristLeft_Z","JointO_HandLeft_Z","JointO_ShoulderRight_Z","JointO_ElbowRight_Z","JointO_WristRight_Z","JointO_HandRight_Z","JointO_HipLeft_Z","JointO_KneeLeft_Z","JointO_AnkleLeft_Z","JointO_FootLeft_Z","JointO_HipRight_Z","JointO_KneeRight_Z","JointO_AnkleRight_Z","JointO_FootRight_Z","JointO_SpineShoulder_Z","JointO_HandTipLeft_Z","JointO_ThumbLeft_Z","JointO_HandTipRight_Z","JointO_ThumbRight_Z","JointO_SpineBase_W","JointO_SpineMid_W","JointO_Neck_W","JointO_Head_W","JointO_ShoulderLeft_W","JointO_ElbowLeft_W","JointO_WristLeft_W","JointO_HandLeft_W","JointO_ShoulderRight_W","JointO_ElbowRight_W","JointO_WristRight_W","JointO_HandRight_W","JointO_HipLeft_W","JointO_KneeLeft_W","JointO_AnkleLeft_W","JointO_FootLeft_W","JointO_HipRight_W","JointO_KneeRight_W","JointO_AnkleRight_W","JointO_FootRight_W","JointO_SpineShoulder_W","JointO_HandTipLeft_W","JointO_ThumbLeft_W","JointO_HandTipRight_W","JointO_ThumbRight_W","time_rel","armopenness","style2")

JointType_Count=24

f1 = gdots(color=color.yellow)
f2 = gcurve(color=color.cyan)
all_data=[]
global joints
features={}
drawTrue=False
midx=0


def loadCSVtoVar(fname):
    csvfile = open(fname, 'r')
    bodyfreader = csv.DictReader(csvfile, header)
    bodyfreader.next()
    for row in bodyfreader:
        jointsP = []
        jointsO = []
        cleanRow(row)
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
            ow = float(row[now])
            jointsO.append((ox, oy, oz, ow))
        all_data.append(((row['style'], row['child'], row['session'], row['activity'], row['versatility']), float(row['time']), float(row['time_rel']), jointsP, jointsO))

def cleanRow(row):
    for key, value in row.items():
        if(value=='' or value=='NA'):
            row[key] = '0'      

def loadCSV(fname):
    csvfile = open(fname,'r')
    joints = []
    for j in map_joints:
        joints.append(sphere(pos=vector(0,0,0),radius=0.08,color=color.green))
    bodyfreader = csv.DictReader(csvfile, header)
    bodyfreader.next()
    for row in bodyfreader:
        rate(150)
        #print(row)
        
        for j in map_joints:
            #print("----------------")
            nx = map_joints[j].replace('JointType_','JointP_')+'_X'
            ny = map_joints[j].replace('JointType_','JointP_')+'_Y'
            nz = map_joints[j].replace('JointType_','JointP_')+'_Z'
            nox = map_joints[j].replace('JointType_','JointO_')+'_X'
            noy = map_joints[j].replace('JointType_','JointO_')+'_Y'
            noz = map_joints[j].replace('JointType_','JointO_')+'_Z'
            now = map_joints[j].replace('JointType_','JointO_')+'_W'
            if(row[nx]!='' and row[ny]!='' and row[nz]!='' and row[nx]!='NA' and row[ny]!='NA' and row[nz]!='NA' ):
                x = float(row[nx])
                y = float(row[ny])
                z = float(row[nz])
                
                joints[j].pos = vector(x,y,z)
                #print(joints[j].pos)
                #plotHeadUpDown(float(row['time_rel']),float(row['JointO_Neck_X']),float(row['JointO_Neck_Y']),float(row['JointO_Neck_Z']),float(row['JointO_Neck_W']))
            #arrow(pos=vector(1,0,0), axis = vector(+1,+3,0), color=color.red)

def readData(index):
    joints[index];
    
def plotHeadUpDown(timerel,x,y,z,w):
    (x,y,z)=computeEclueadianAngles(x, y, z, w)
    #graph1 = gdisplay()
    f1.plot(pos=(timerel,(x*180/math.pi)))
    f2.plot(pos=(timerel,(y*180/math.pi)))
   

def computeVelocity(pt2, pt0):
    (time2, x2, y2, z2)=pt2
    (time0, x0, y0, z0)=pt0
    vx=x2-x0/(2*time2-time0)
    vy=y2-y0/(2*time2-time0)
    vz=z2-z0/(2*time2-time0)
    #for each joint compute the velocity and return it
    return math.sqrt(vx*vx+vy*vy+vz*vz)

def computeAcceleration(time2, x2, y2, z2, time0, x0, y0, z0, time1, x1, y1, z1):
    dt= time2-time0
    ax=(x2-2*x1+x0)/(dt*dt)
    ay=(y2-2*y1+y0)/(dt*dt)
    az=(z2-2*z1+z0)/(dt*dt)
    #for each joint compute the velocity and return it
    return math.sqrt(ax*ax+ay*ay+az*az)

def computeJerk(pt2, pt1, pt_1, pt_2):
    (time2, x2, y2, z2)=pt2
    (time1, x1, y1, z1)=pt1
    (time_1, x_1, y_1, z_1)=pt_1
    (time_2, x_2, y_2, z_2)=pt_2
    dt=time2-time_2
    jx = (x2 - 2*x1 + 2*x_1 - x_2)/dt
    jy = (y2 - 2*y1 + 2*y_1 - y_2)/dt
    jz = (z2 - 2*z1 + 2*z_1 - z_2)/dt
    return math.sqrt(jx*jx + jy*jy + jz*jz)
         
         
def computeQoM(jointsweights,jointpt):
    qom=0.0
    for i,(pt2,pt0) in jointpt:
        qom+=jointsweights[i]*computeVelocity(pt2,pt0)
    qom/= sum(jointsweights)
    return qom

def computeBoundingBox(joints):
    minx= min([joint[0] for joint in joints])
    maxx= max([joint[0] for joint in joints])
    miny= min([joint[1] for joint in joints])
    maxy= max([joint[1] for joint in joints])
    minz= min([joint[2] for joint in joints])
    maxz= max([joint[2] for joint in joints])
    return (minx, maxx, miny, maxy, minz, maxz)

def computeVolume(boundingbox):
    (minx, maxx, miny, maxy, minz, maxz)=boundingbox
    return sqrt((maxx-minx)*(maxx-minx) + (maxy-miny)*(maxy-miny) + (maxz-minz)*(maxz-minz))
    

def drawBoundingBox(joints):
    (minx, maxx, miny, maxy, minz, maxz)=computeBoundingBox(joints)
    features["boundingbox"]=box((minx, maxx, miny, maxy, minz, maxz))

def computeDisplacement(jointk, jointl):
    return distance(jointk, jointl)

def drawDisplacement(jointk,jointl):
    features["displacement"]=arrow(jointk,jointl)

def distance(jointa, jointb):
    (xa,ya,za)= jointa
    (xb, yb, zb)= jointb
    return math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)+(zb-za)*(zb-za))

def rotation(jointOa, jointOb):
    return np.vdot(jointOa, jointOb)

def CoM(jointsweights,joints):
    com=0.0
    for i,(x,y,z) in joints:
        com+=jointsweights[i]*(x,y,z)
    com/= sum(jointsweights)
    return com
    
def actionPresence(joints1,joints0, epsilon=90):
    action=[]
    for j1,j0 in (joints1,joints0):
        if(distance(j1,j0)>epsilon):
            action.append(1)
        else:
            action.append(0)
    return action
    
#def CoMDisplacement(joints1,joints0, epsilon):
    #todo

def eucledian(jointO):
    jointE= jointO
    return jointE
def torsoOrientationEucledian(jointO):
    return eucledian(jointO)
def neckOrientationEucledian(jointO):
    return eucledian(jointO)

def computeJointDistance():
    return 0
def computeLeanAngles():
    #return foward, side
    return 0
def computeAlignement():
#          AddToSerialization("RightHandState",RightHandState);
#         AddToSerialization("AlignedFeetLeft",AlignedFeetLeft);
#         AddToSerialization("AlignedHandsLeft",AlignedHandsLeft);
#         AddToSerialization("AlignedLegsLeft",AlignedLegsLeft);
#         AddToSerialization("AlignedFeetRight",AlignedFeetRight);
#         AddToSerialization("AlignedHandsRight",AlignedHandsRight);
#         AddToSerialization("AlignedLegsRight",AlignedLegsRight);
    return


def extensiveness(extremities_joints, com):
    max=0
    for joint in extremities_joints:
        if(distance(joint,com)>=max):
            max=distance(joint,com)
    return max
def extensiveness2(extremities_joints, com):
    sum=0
    for joint in extremities_joints:
        sum+=distance(joint,com)
    return sum

def armsShape(body_center,hand_e):
    return distance(body_center,hand_e)
def elbowFlexion(joint_hand, joint_elbow, joint_shoulder):
    #np.linalg.norm(joint_hand.x-joint_el)
    return 0

def computeHandTouch(joints, handidx):
        threshold = distance(joints[handidx],joints[handidx-1]);
        hand_arr=[]
        fdistance=0.0
        hand_joint = joints[handidx];
        for j in  range(JointType_Count - 4):
            if(j!=handidx and j!=handidx-1 and j!=handidx-2):
                distance = distance(hand_joint,joints[j]);
                if fdistance <=threshold :
                    hand_arr.push_back(joints[j])
        return hand_arr

def computeAsymetry(jname):
#     AddToSerialization("HandAsym", HandAsym);
#         AddToSerialization("WristAsym", WristAsym);
#         AddToSerialization("ElbowAsym",ElbowAsym);
#         AddToSerialization("FootAsym",FootAsym);
#         AddToSerialization("AnkleAsym",AnkleAsym);
#         AddToSerialization("KneeAsym",KneeAsym);
    return 0    

      
      #  AddToSerialization("SpineOrientation",sSpineOrientation);
      #  AddToSerialization("BodyLeanAngle", sBodyLeanAngle);
      #  AddToSerialization("SchegloffBP",sSchegloffBP);



    
def computeEclueadianAngles(x, y, z, w):
    rollx = math.atan((2*(x*y + z*w))/(1-2*(y*y + z*z))) #x
    pitchy = asin(2*(x*z - y*w)) #y
    yawz= atan((2*(x*w + y*z))/(1-2*(w*w + z*z))) #z
    return (rollx, pitchy, yawz)

##################   body decriotrs





def setChild(childid):
    return all_data.index(childid)

#################### DRAWING FUNCTIONS
def drawTime(time):
    idx = [frame[2] for frame in all_data]
    print(idx.index(time))
    drawFrameidx(idx.index(time))
 
 
def drawInitScene():
     checkerboard = ( (0,1,0,1),
                 (1,0,1,0),
                 (0,1,0,1),
                 (1,0,1,0) )
     tex = materials.texture(data=checkerboard,
                     mapping="rectangular",
                     interpolate=False)
     box(axis=(0,0,1), color=color.cyan, material=tex)
 
    
def drawFrameidx(idx):
    (metainfo,tstp,time_rel,jointp,jointo) =all_data[idx]
    print(jointp)
    for j in map_joints:
        joints[j].pos = vector(jointp[j])
  
def test(mid):
    while(mid<len(all_data)):
        rate(150)
        (metainfo,tstp,time_rel,jointp,jointo) =all_data[mid]
        drawFrameidx(mid)
        print(metainfo)
        mid+=1
            
def dosmh(qlq):
    print(qlq)
if __name__ == "__main__":
    fname="/Users/wafajohal/Dropbox/DATA/STYLEBOT/child4_dance.csv"
    loadCSVtoVar(fname)
    drawInitScene()
    print(time.clock())
    print(all_data[500][0])
    scene.select()
    scene.background = (0,0,0)
    scene.center
    scene.userspin = True
    joints=[]
    midx=0
    for j in map_joints:
        joints.append(sphere(pos=vector(0,0,0),radius=0.08,color=color.green))
    c = controls(title='Controlling the Scene',x=0, y=0, width=300, height=300, range=100)
    #menu = c.menu()
    #menu.items.append( ('4', lambda: setChild(4)) )
    #userspin=True
    #mint=min( frame[2] for frame in all_data)
    #maxt=max( frame[2] for frame in all_data)
    #slid = slider(pos=(-90,-80), min=mint, max=maxt, length=(maxt-mint), action=lambda: drawTime(slid.getvalue()))
    #slid.min=mint
    #slid.max=maxt
    #slid.length=slid.max-slid.min
    #slid.action('drawTime(0)')
    #drawTime(10)
    
  
    b1 = button(pos=(0,0),color=color.blue, action=lambda: test(midx))    
    t1 = toggle(pos=(40,-30), width=10, height=10, text0='Red', text1='Cyan', action=lambda: test(midx))

