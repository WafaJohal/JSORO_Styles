import csv
import json
import datetime 
import os
import sys
from ast import literal_eval
import fnmatch
import operator
import math
import labels

csv_Header=('activity' ,'style','versatility','session','child','time','id', 'nb_ske','JointP_SpineBase_X', 'JointP_SpineMid_X', 'JointP_Neck_X', 'JointP_Head_X', 'JointP_ShoulderLeft_X', 'JointP_ElbowLeft_X', 'JointP_WristLeft_X', 'JointP_HandLeft_X', 'JointP_ShoulderRight_X', 'JointP_ElbowRight_X', 'JointP_WristRight_X', 'JointP_HandRight_X', 'JointP_HipLeft_X', 'JointP_KneeLeft_X', 'JointP_AnkleLeft_X', 'JointP_FootLeft_X', 'JointP_HipRight_X', 'JointP_KneeRight_X', 'JointP_AnkleRight_X', 'JointP_FootRight_X', 'JointP_SpineShoulder_X', 'JointP_HandTipLeft_X', 'JointP_ThumbLeft_X', 'JointP_HandTipRight_X', 'JointP_ThumbRight_X','JointO_SpineBase_X', 'JointO_SpineMid_X', 'JointO_Neck_X', 'JointO_Head_X', 'JointO_ShoulderLeft_X', 'JointO_ElbowLeft_X', 'JointO_WristLeft_X', 'JointO_HandLeft_X', 'JointO_ShoulderRight_X', 'JointO_ElbowRight_X', 'JointO_WristRight_X', 'JointO_HandRight_X', 'JointO_HipLeft_X', 'JointO_KneeLeft_X', 'JointO_AnkleLeft_X', 'JointO_FootLeft_X', 'JointO_HipRight_X', 'JointO_KneeRight_X', 'JointO_AnkleRight_X', 'JointO_FootRight_X', 'JointO_SpineShoulder_X', 'JointO_HandTipLeft_X', 'JointO_ThumbLeft_X', 'JointO_HandTipRight_X', 'JointO_ThumbRight_X',
'JointP_SpineBase_Y', 'JointP_SpineMid_Y', 'JointP_Neck_Y', 'JointP_Head_Y', 'JointP_ShoulderLeft_Y', 'JointP_ElbowLeft_Y', 'JointP_WristLeft_Y', 'JointP_HandLeft_Y', 'JointP_ShoulderRight_Y', 'JointP_ElbowRight_Y', 'JointP_WristRight_Y', 'JointP_HandRight_Y', 'JointP_HipLeft_Y', 'JointP_KneeLeft_Y', 'JointP_AnkleLeft_Y', 'JointP_FootLeft_Y', 'JointP_HipRight_Y', 'JointP_KneeRight_Y', 'JointP_AnkleRight_Y', 'JointP_FootRight_Y', 'JointP_SpineShoulder_Y', 'JointP_HandTipLeft_Y', 'JointP_ThumbLeft_Y', 'JointP_HandTipRight_Y', 'JointP_ThumbRight_Y','JointO_SpineBase_Y', 'JointO_SpineMid_Y', 'JointO_Neck_Y', 'JointO_Head_Y', 'JointO_ShoulderLeft_Y', 'JointO_ElbowLeft_Y', 'JointO_WristLeft_Y', 'JointO_HandLeft_Y', 'JointO_ShoulderRight_Y', 'JointO_ElbowRight_Y', 'JointO_WristRight_Y', 'JointO_HandRight_Y', 'JointO_HipLeft_Y', 'JointO_KneeLeft_Y', 'JointO_AnkleLeft_Y', 'JointO_FootLeft_Y', 'JointO_HipRight_Y', 'JointO_KneeRight_Y', 'JointO_AnkleRight_Y', 'JointO_FootRight_Y', 'JointO_SpineShoulder_Y', 'JointO_HandTipLeft_Y', 'JointO_ThumbLeft_Y', 'JointO_HandTipRight_Y', 'JointO_ThumbRight_Y',
'JointP_SpineBase_Z', 'JointP_SpineMid_Z', 'JointP_Neck_Z', 'JointP_Head_Z', 'JointP_ShoulderLeft_Z', 'JointP_ElbowLeft_Z', 'JointP_WristLeft_Z', 'JointP_HandLeft_Z', 'JointP_ShoulderRight_Z', 'JointP_ElbowRight_Z', 'JointP_WristRight_Z', 'JointP_HandRight_Z', 'JointP_HipLeft_Z', 'JointP_KneeLeft_Z', 'JointP_AnkleLeft_Z', 'JointP_FootLeft_Z', 'JointP_HipRight_Z', 'JointP_KneeRight_Z', 'JointP_AnkleRight_Z', 'JointP_FootRight_Z', 'JointP_SpineShoulder_Z', 'JointP_HandTipLeft_Z', 'JointP_ThumbLeft_Z', 'JointP_HandTipRight_Z', 'JointP_ThumbRight_Z','JointO_SpineBase_Z', 'JointO_SpineMid_Z', 'JointO_Neck_Z', 'JointO_Head_Z', 'JointO_ShoulderLeft_Z', 'JointO_ElbowLeft_Z', 'JointO_WristLeft_Z', 'JointO_HandLeft_Z', 'JointO_ShoulderRight_Z', 'JointO_ElbowRight_Z', 'JointO_WristRight_Z', 'JointO_HandRight_Z', 'JointO_HipLeft_Z', 'JointO_KneeLeft_Z', 'JointO_AnkleLeft_Z', 'JointO_FootLeft_Z', 'JointO_HipRight_Z', 'JointO_KneeRight_Z', 'JointO_AnkleRight_Z', 'JointO_FootRight_Z', 'JointO_SpineShoulder_Z', 'JointO_HandTipLeft_Z', 'JointO_ThumbLeft_Z', 'JointO_HandTipRight_Z', 'JointO_ThumbRight_Z',
'JointO_SpineBase_W', 'JointO_SpineMid_W', 'JointO_Neck_W', 'JointO_Head_W', 'JointO_ShoulderLeft_W', 'JointO_ElbowLeft_W', 'JointO_WristLeft_W', 'JointO_HandLeft_W', 'JointO_ShoulderRight_W', 'JointO_ElbowRight_W', 'JointO_WristRight_W', 'JointO_HandRight_W', 'JointO_HipLeft_W', 'JointO_KneeLeft_W', 'JointO_AnkleLeft_W', 'JointO_FootLeft_W', 'JointO_HipRight_W', 'JointO_KneeRight_W', 'JointO_AnkleRight_W', 'JointO_FootRight_W', 'JointO_SpineShoulder_W', 'JointO_HandTipLeft_W', 'JointO_ThumbLeft_W', 'JointO_HandTipRight_W', 'JointO_ThumbRight_W')

csv_timestmpHeader=('time','id', 'nb_ske','JointP_SpineBase_X', 'JointP_SpineMid_X', 'JointP_Neck_X', 'JointP_Head_X', 'JointP_ShoulderLeft_X', 'JointP_ElbowLeft_X', 'JointP_WristLeft_X', 'JointP_HandLeft_X', 'JointP_ShoulderRight_X', 'JointP_ElbowRight_X', 'JointP_WristRight_X', 'JointP_HandRight_X', 'JointP_HipLeft_X', 'JointP_KneeLeft_X', 'JointP_AnkleLeft_X', 'JointP_FootLeft_X', 'JointP_HipRight_X', 'JointP_KneeRight_X', 'JointP_AnkleRight_X', 'JointP_FootRight_X', 'JointP_SpineShoulder_X', 'JointP_HandTipLeft_X', 'JointP_ThumbLeft_X', 'JointP_HandTipRight_X', 'JointP_ThumbRight_X','JointO_SpineBase_X', 'JointO_SpineMid_X', 'JointO_Neck_X', 'JointO_Head_X', 'JointO_ShoulderLeft_X', 'JointO_ElbowLeft_X', 'JointO_WristLeft_X', 'JointO_HandLeft_X', 'JointO_ShoulderRight_X', 'JointO_ElbowRight_X', 'JointO_WristRight_X', 'JointO_HandRight_X', 'JointO_HipLeft_X', 'JointO_KneeLeft_X', 'JointO_AnkleLeft_X', 'JointO_FootLeft_X', 'JointO_HipRight_X', 'JointO_KneeRight_X', 'JointO_AnkleRight_X', 'JointO_FootRight_X', 'JointO_SpineShoulder_X', 'JointO_HandTipLeft_X', 'JointO_ThumbLeft_X', 'JointO_HandTipRight_X', 'JointO_ThumbRight_X',
'JointP_SpineBase_Y', 'JointP_SpineMid_Y', 'JointP_Neck_Y', 'JointP_Head_Y', 'JointP_ShoulderLeft_Y', 'JointP_ElbowLeft_Y', 'JointP_WristLeft_Y', 'JointP_HandLeft_Y', 'JointP_ShoulderRight_Y', 'JointP_ElbowRight_Y', 'JointP_WristRight_Y', 'JointP_HandRight_Y', 'JointP_HipLeft_Y', 'JointP_KneeLeft_Y', 'JointP_AnkleLeft_Y', 'JointP_FootLeft_Y', 'JointP_HipRight_Y', 'JointP_KneeRight_Y', 'JointP_AnkleRight_Y', 'JointP_FootRight_Y', 'JointP_SpineShoulder_Y', 'JointP_HandTipLeft_Y', 'JointP_ThumbLeft_Y', 'JointP_HandTipRight_Y', 'JointP_ThumbRight_Y','JointO_SpineBase_Y', 'JointO_SpineMid_Y', 'JointO_Neck_Y', 'JointO_Head_Y', 'JointO_ShoulderLeft_Y', 'JointO_ElbowLeft_Y', 'JointO_WristLeft_Y', 'JointO_HandLeft_Y', 'JointO_ShoulderRight_Y', 'JointO_ElbowRight_Y', 'JointO_WristRight_Y', 'JointO_HandRight_Y', 'JointO_HipLeft_Y', 'JointO_KneeLeft_Y', 'JointO_AnkleLeft_Y', 'JointO_FootLeft_Y', 'JointO_HipRight_Y', 'JointO_KneeRight_Y', 'JointO_AnkleRight_Y', 'JointO_FootRight_Y', 'JointO_SpineShoulder_Y', 'JointO_HandTipLeft_Y', 'JointO_ThumbLeft_Y', 'JointO_HandTipRight_Y', 'JointO_ThumbRight_Y',
'JointP_SpineBase_Z', 'JointP_SpineMid_Z', 'JointP_Neck_Z', 'JointP_Head_Z', 'JointP_ShoulderLeft_Z', 'JointP_ElbowLeft_Z', 'JointP_WristLeft_Z', 'JointP_HandLeft_Z', 'JointP_ShoulderRight_Z', 'JointP_ElbowRight_Z', 'JointP_WristRight_Z', 'JointP_HandRight_Z', 'JointP_HipLeft_Z', 'JointP_KneeLeft_Z', 'JointP_AnkleLeft_Z', 'JointP_FootLeft_Z', 'JointP_HipRight_Z', 'JointP_KneeRight_Z', 'JointP_AnkleRight_Z', 'JointP_FootRight_Z', 'JointP_SpineShoulder_Z', 'JointP_HandTipLeft_Z', 'JointP_ThumbLeft_Z', 'JointP_HandTipRight_Z', 'JointP_ThumbRight_Z','JointO_SpineBase_Z', 'JointO_SpineMid_Z', 'JointO_Neck_Z', 'JointO_Head_Z', 'JointO_ShoulderLeft_Z', 'JointO_ElbowLeft_Z', 'JointO_WristLeft_Z', 'JointO_HandLeft_Z', 'JointO_ShoulderRight_Z', 'JointO_ElbowRight_Z', 'JointO_WristRight_Z', 'JointO_HandRight_Z', 'JointO_HipLeft_Z', 'JointO_KneeLeft_Z', 'JointO_AnkleLeft_Z', 'JointO_FootLeft_Z', 'JointO_HipRight_Z', 'JointO_KneeRight_Z', 'JointO_AnkleRight_Z', 'JointO_FootRight_Z', 'JointO_SpineShoulder_Z', 'JointO_HandTipLeft_Z', 'JointO_ThumbLeft_Z', 'JointO_HandTipRight_Z', 'JointO_ThumbRight_Z',
'JointO_SpineBase_W', 'JointO_SpineMid_W', 'JointO_Neck_W', 'JointO_Head_W', 'JointO_ShoulderLeft_W', 'JointO_ElbowLeft_W', 'JointO_WristLeft_W', 'JointO_HandLeft_W', 'JointO_ShoulderRight_W', 'JointO_ElbowRight_W', 'JointO_WristRight_W', 'JointO_HandRight_W', 'JointO_HipLeft_W', 'JointO_KneeLeft_W', 'JointO_AnkleLeft_W', 'JointO_FootLeft_W', 'JointO_HipRight_W', 'JointO_KneeRight_W', 'JointO_AnkleRight_W', 'JointO_FootRight_W', 'JointO_SpineShoulder_W', 'JointO_HandTipLeft_W', 'JointO_ThumbLeft_W', 'JointO_HandTipRight_W', 'JointO_ThumbRight_W')

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


def computeEulerAngles(fname):
	csvfile = open(fname,'r')
	fout = fname[:fname.find('.')]+'_euler.csv'
	csvfileout = open(fout,'w')
	writer = csv.DictWriter(csvfileout, csv_Header)
	bodyfreader = csv.DictReader(csvfile,csv_Header)
	count=0
	bodyfreader.next()
	for row in bodyfreader:
		row2 = row
		for j in map_joints:
			#print("----------------")
			nx = map_joints[j].replace('JointType_','JointO_')+'_X'
			ny = map_joints[j].replace('JointType_','JointO_')+'_Y'
			nz = map_joints[j].replace('JointType_','JointO_')+'_Z'
			nw = map_joints[j].replace('JointType_','JointO_')+'_W'
			#print(row[nx],row[ny],row[nz],row[nw])
			if(row[nx]!='' and row[ny]!='' and row[nz]!='' and row[nw]!=''):
				#print(float(row[nx]))
				#print(float(row[ny]))
				#print(float(row[nz]))
				#print(float(row[nw]))
				x = (2*(float(row[nx])*float(row[ny]) + float(row[nz])*float(row[nw])))/(1-2*(float(row[ny])*float(row[ny]) + float(row[nz])*float(row[nz]))) #X
				y = 2*(float(row[nx])*float(row[nz]) - float(row[ny])*float(row[nw])) #Y
				z = (2*(float(row[nx])*float(row[nw]) + float(row[ny])*float(row[nz])))/(1-2*(float(row[nw])*float(row[nw]) + float(row[nz])*float(row[nz]))) #Z
				if( x>=-1.0 or x<=1.0):
					row2[nx]=math.atan(x)
				else :
					row2[nx] = 'NA'
				if( abs(y+1.0)<=0 or abs(y-1.0)<=0):
					print(y)
					row2[ny]=math.asin(y)
				else:
					row2[ny] = 'NA'
				if( z>=-1.0 or z<=1.0):
					row2[nz]=math.atan(z)
				else:
					row2[nz] = 'NA'
				row2[nw]=0
		writer.writerow(row2)
		count+=1
		print(count)
	print "fniito"
	csvfileout.close()
	csvfile.close()
	
def distance3D(x,y,z,a,b,c):
	return math.sqrt((x-a)*(x-a)+(y-b)*(y-b)+(z-c)*(z-c))

def computeMotionEnergy(fname):
	alpha=0.1
	csvfile = open(fname,'r')
	fout = fname[:fname.find('.')]+'_MotionEnergy.csv'
	csvfileout = open(fout,'w')
	new_header = ('motion_energy',)+tuple(csv_Header)
	#print(new_header)
	writer = csv.DictWriter(csvfileout, new_header)
	bodyfreader = csv.DictReader(csvfile,csv_Header)
	count=0
	me=0
	prev_row= bodyfreader.next()
	for row in bodyfreader:
		row2 = row
		if(prev_row['child']!=row['child']):
			prev_row=row
			for j in map_joints:
				#print("----------------")
				nx = map_joints[j].replace('JointType_','JointP_')+'_X'
				ny = map_joints[j].replace('JointType_','JointP_')+'_Y'
				nz = map_joints[j].replace('JointType_','JointP_')+'_Z'
				if(row[nx]!='' and row[ny]!='' and row[nz]!=''):
					d= distance3D(float(row[nx]),float(row[ny]),float(row[nz]),float(prev_row[nx]),float(prev_row[ny]),float(prev_row[nz]))
					if(d>=0.001):
						me+=d
			row2={'motion_energy':me}
			row2.update(row)
			prev_row=row
		else : 
			#prev_row = somme(current_joints,prev_joints,0.1,0.9) # somme current*0.1+previous=0.9
			for j in map_joints:
				#print("----------------")
				nx = map_joints[j].replace('JointType_','JointP_')+'_X'
				ny = map_joints[j].replace('JointType_','JointP_')+'_Y'
				nz = map_joints[j].replace('JointType_','JointP_')+'_Z'
				if(row[nx]!='' and row[ny]!='' and row[nz]!=''):
					d= distance3D(float(row[nx]),float(row[ny]),float(row[nz]),float(prev_row[nx]),float(prev_row[ny]),float(prev_row[nz]))
					if(d>=0.001):
						me+=d
					prev_row[nx]=alpha*float(row[nx])+(1-alpha)*float(prev_row[nx])
					prev_row[ny]=alpha*float(row[ny])+(1-alpha)*float(prev_row[ny])
					prev_row[nz]=alpha*float(row[nz])+(1-alpha)*float(prev_row[nz])
			row2={'motion_energy':me}
			#print(row)
			row2.update(row)
		writer.writerow(row2)
		me=0
		count+=1
		print(count)
	print "fniito"
	csvfileout.close()
	csvfile.close()
	
def computeMeanVelocity(fname):
	csvfile = open(fname,'r')
	bodyfreader = csv.DictReader(csvfile,csv_Header)

#2 session separees
def labelizeBodyFeatures(child, fname, offset):
	csvtimein = open(fname, 'r')
	fout = fname[:fname.find('.')]+'_labelized.timestamp'
	csvfileout = open(fout, 'w')
	(Enfant,Style,Versatility,Session,start,q1,q1_f,d,d_f,q2,q2_f,fin)=labels.children[child]
	
	timereader = csv.reader( csvtimein)
	fieldnames_timesin = timereader.next()
	timereader = csv.DictReader( csvtimein,fieldnames_timesin)
	labelized_header=("activity","style", "versatility","session","child")+tuple(fieldnames_timesin)
	fieldnames_labelout = (labelized_header)

	writer = csv.DictWriter(csvfileout, fieldnames_labelout)
	writer.writeheader()
	count =0
	first=0.0
	for row in timereader:
		timestamp = float(row["time"])
		#if(timestamp>= (start-offset) and timestamp<= (fin-offset)):
		#	print(timestamp>= (start-offset) and timestamp<= (fin-offset))
		if(timestamp< (start-offset)):
			current_dict = {"activity":"before","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		elif((q1!='na' and q1_f!='na') and timestamp>= (q1-offset) and timestamp<= (q1_f-offset)):
			current_dict = {"activity":"quiz1","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		elif((q2!='na' and q2_f!='na') and timestamp>= (q2-offset) and timestamp<= (q2_f-offset)):
			current_dict = {"activity":"quiz2","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		elif((d!='na' and d_f!='na') and timestamp>= (d-offset) and timestamp<= (d_f-offset)):
			current_dict = {"activity":"dance","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		elif(timestamp>= (start-offset) and timestamp<= (fin-offset)):
			current_dict = {"activity":"explain","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		elif(timestamp>= (fin-offset)):
			current_dict = {"activity":"after","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		else :
			current_dict = {"activity":"unknown","style":Style,"versatility":Versatility,"session":Session,"child":Enfant}
		current_dict.update(row)
		writer.writerow(current_dict)
		count +=1
		last = timestamp
		if(count==1):
			first = timestamp
	print fout
	print first
	print 'Q1 \t'+str(q1-offset)
	#print (Enfant,Style,Versatility,Session,start-offset,q1-offset,q1_f-offset,d-offset,d_f-offset,q2-offset,q2_f-offset,fin-offset)
	print 'Q2 \t'+str(q2-offset)
	print last
	print "fniito"
	csvfileout.close()
	csvtimein.close()


# les 2 sessions sur le meme fichier
def labelizeBodyFeatures2(childs1,childs2, fname, offset):
	csvtimein = open(fname, 'r')
	fout = fname[:fname.find('.')]+'_labelized.timestamp'
	csvfileout = open(fout, 'w')
	(Enfant1,Style1,Versatility1,Session1,start1,q11,q1_f1,d1,d_f1,q21,q2_f1,fin1)=labels.children[childs1]
	(Enfant2,Style2,Versatility2,Session2,start2,q12,q1_f2,d2,d_f2,q22,q2_f2,fin2)=labels.children[childs2]
	timereader = csv.reader( csvtimein)
	fieldnames_timesin = timereader.next()
	timereader = csv.DictReader( csvtimein,fieldnames_timesin)
	labelized_header=("activity","style", "versatility","session","child")+tuple(fieldnames_timesin)
	fieldnames_labelout = (labelized_header)

	writer = csv.DictWriter(csvfileout, fieldnames_labelout)
	writer.writeheader()
	count =0
	first=0.0
	for row in timereader:
		timestamp = float(row["time"])
		#if(timestamp>= (start-offset) and timestamp<= (fin-offset)):
		#	print(timestamp>= (start-offset) and timestamp<= (fin-offset))
		if(timestamp< (start1-offset)):
			current_dict = {"activity":"before","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif((q11!='na' and q1_f1!='na') and timestamp>= (q11-offset) and timestamp<= (q1_f1-offset)):
			current_dict = {"activity":"quiz1","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif((q21!='na' and q2_f1!='na') and timestamp>= (q21-offset) and timestamp<= (q2_f1-offset)):
			current_dict = {"activity":"quiz2","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif((d1!='na' and d_f1!='na') and timestamp>= (d1-offset) and timestamp<= (d_f1-offset)):
			current_dict = {"activity":"dance","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif(timestamp>= (start1-offset) and timestamp<= (fin1-offset)):
			current_dict = {"activity":"explain","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif(timestamp>= (fin1-offset) and timestamp< (start2-offset)):
			current_dict = {"activity":"intersession","style":Style1,"versatility":Versatility1,"session":Session1,"child":Enfant1}
		elif((q12!='na' and q1_f2!='na') and timestamp>= (q12-offset) and timestamp<= (q1_f2-offset)):
			current_dict = {"activity":"quiz1","style":Style2,"versatility":Versatility2,"session":Session2,"child":Enfant2}
		elif((q22!='na' and q2_f2!='na') and timestamp>= (q22-offset) and timestamp<= (q2_f2-offset)):
			current_dict = {"activity":"quiz2","style":Style2,"versatility":Versatility2,"session":Session2,"child":Enfant2}
		elif((d2!='na' and d_f2!='na') and timestamp>= (d2-offset) and timestamp<= (d_f2-offset)):
			current_dict = {"activity":"dance","style":Style2,"versatility":Versatility2,"session":Session2,"child":Enfant2}
		elif(timestamp>= (start2-offset) and timestamp<= (fin2-offset)):
			current_dict = {"activity":"explain","style":Style2,"versatility":Versatility2,"session":Session2,"child":Enfant2}
		elif(timestamp>= (fin2-offset)):
			current_dict = {"activity":"after","style":Style2,"versatility":Versatility2,"session":Session2,"child":Enfant2}
		else :
			current_dict = {"activity":"unknown","style":"unknown","versatility":"unknown","session":0,"child":Enfant1}
		current_dict.update(row)
		writer.writerow(current_dict)
		count +=1
		last = timestamp
		if(count==1):
			first = timestamp
	print fout
	print first
	#print (Enfant1,Style1,Versatility1,Session1,start1-offset,q11-offset,q1_f1-offset,d1-offset,d_f1-offset,q21-offset,q2_f1-offset,fin1-offset)
	#print (Enfant2,Style2,Versatility2,Session2,start2-offset,q12-offset,q1_f2-offset,d2-offset,d_f2-offset,q22-offset,q2_f2-offset,fin2-offset)
	print last
	print "fniito"
	csvfileout.close()
	csvtimein.close()


def findIdsSkeletons(fname):
	csvfile = open(fname, 'r')
	csvreader= csv.reader( csvfile, delimiter=' ')
	indiv_ids=[]
	for row in csvreader:
		print row[0]
		if(row[1]=='0'):
			#print 'noone'
			pass
		else:
			current = row[2].replace('nan',"0")
			#print row
			jsonl = json.loads(current)
			for i in range(len(jsonl)):
				instance=jsonl[i]
				if(instance['id'] not in indiv_ids):
					indiv_ids.append(instance['id'])
	csvfile.close()
	return indiv_ids
	
		
def splitJSONPerBody(fname):
	indiv_ids = findIdsSkeletons(fname)
	print indiv_ids
	csvfile = open(fname, 'r')
	csvreader= csv.reader( csvfile, delimiter=' ')
	
	all_files= indiv_ids
	all_filenames= indiv_ids
	
	for ids in  range(len(all_files)): 
		mfilename =fname[:fname.find('.')]+'_'+str(indiv_ids[ids])+'.json'
		all_filenames[ids] = mfilename
		jsonfile = open(mfilename, 'w+')
		jsonfile.write('[')
		all_files[ids] =jsonfile
		#print all_filenames	

	for row in csvreader:
		mtime = row[0]
		nb_ske = row[1]
		if(row[1]=='0'):
			pass
		else :
			current = row[2].replace('nan',"0")
			jsonl = json.loads(current)
			#instance = jsonl[0]
			for i in range(len(jsonl)):
				instance=jsonl[i]
				#print instance
				#for(instance['id'] in indiv_ids):
				#print instance['id']
				#atrouve = 'body_features_'+instance['id']+'.json'
				#f = all_filenames.index(atrouve)
				jsonout = instance
				jsonout["time"]=mtime
				jsonout["nb_ske"]=nb_ske
				json.dump(jsonout, all_files[i])
				all_files[i].write(',\n')
		
	#print indiv_ids
	for ids in range(len(indiv_ids)): 
		all_files[ids].write(']')
		all_files[ids].close()
	csvfile.close()

def jsontoCSV(fname):
	json_inputf=open(fname,'r')
	csvfname=fname.replace('.json','.csv')
	csv_outputf=open(csvfname,'w+')
	writer = csv.DictWriter(csv_outputf, csv_timestmpHeader)
	writer.writeheader()
	countline = 0
	
	with open(fname,'r') as json_inputf:
		for line in json_inputf:
			#print(line)
			if countline==0:
				line = line.replace('[{"JointsOrientations','{"JointsOrientations')
			line = line.replace(',\n','')
			if(line[0]==']'):
				break
			jline=json.loads(line)
			ftime = float(jline['time'])
			userid=int(jline['id'])
			nb_ske=int(jline['nb_ske'])
			csv_row={'time':ftime,'id':userid, 'nb_ske':nb_ske}
			for i in range(0,24):
				[px,py,pz] =jline['Joints'][map_joints[i]]
				[ox,oy,oz,ow] =jline['JointsOrientations'][map_joints[i]]
				csv_joint={map_joints[i].replace('JointType_','JointP_')+'_X':px}
				csv_joint.update({map_joints[i].replace('JointType_','JointP_')+'_Y':py})
				csv_joint.update({map_joints[i].replace('JointType_','JointP_')+'_Z':pz})
				csv_joint.update({map_joints[i].replace('JointType_','JointO_')+'_X':ox})
				csv_joint.update({map_joints[i].replace('JointType_','JointO_')+'_Y':oy})
				csv_joint.update({map_joints[i].replace('JointType_','JointO_')+'_Z':oz})
				csv_joint.update({map_joints[i].replace('JointType_','JointO_')+'_W':ow})
				csv_row.update(csv_joint)
			countline+=1
			print(countline)
			writer.writerow(csv_row)
	json_inputf.close()
	csv_outputf.close()


if __name__ == "__main__":
	#rootdir = sys.argv[1]
	#for root, dirnames, filenames in os.walk(rootdir):
	#		#for filename in fnmatch.filter(filenames, 'body_joints.timestamp'):
	#		for filename in fnmatch.filter(filenames, 'body_joints_*.json'):
	#			fname = os.path.join(root, filename)
	#			print fname
	#			#splitJSONPerBody(fname)
	#			jsontoCSV(fname)
	#			#splitComposedData(fname)
	##fname = sys.argv[1]
	##offset = sys.argv[2]
	#labes=sys.argv[3]
	##childs1 = sys.argv[3]
	##childs2 = sys.argv[4]
	#labelizeBodyFeatures(labes,fname,float(offset))
	##labelizeBodyFeatures2(childs1,childs2, fname, float(offset))
	fname=sys.argv[1]
	#computeEulerAngles(fname)
	computeMotionEnergy(fname)
