library(psych)
require(ggplot2)

########## compute eucledian angles
features$head_rollx<-atan((2*(features$NeckQx*features$NeckQy + features$NeckQz*features$NeckQw))/(1-2*(features$NeckQy*features$NeckQy + features$NeckQz*features$NeckQz))) #x
features$head_pitchy<-asin(2*(features$NeckQx*features$NeckQz - features$NeckQy*features$NeckQw)) #y
features$head_yawz<-atan((2*(features$NeckQx*features$NeckQw + features$NeckQy*features$NeckQz))/(1-2*(features$NeckQw*features$NeckQw + features$NeckQz*features$NeckQz))) #z

features$torso_rollx<-atan((2*(features$TorsoQx*features$TorsoQy + features$TorsoQz*features$TorsoQw))/(1-2*(features$TorsoQy*features$TorsoQy + features$TorsoQz*features$TorsoQz))) #x
features$torso_pitchy<-asin(2*(features$TorsoQx*features$TorsoQz - features$TorsoQy*features$TorsoQw)) #y
features$torso_yawz<-atan((2*(features$TorsoQx*features$TorsoQw + features$TorsoQy*features$TorsoQz))/(1-2*(features$TorsoQw*features$TorsoQw + features$TorsoQz*features$TorsoQz))) #z

######### child data



###################################
in_interact2 <- read.csv("~/Dropbox/DATA/STYLEBOT/new_data.csv") ### wafa's bf
in_interact <- read.csv("~/Dropbox/DATA/STYLEBOT/bodys_data.csv") ### bodies

features <- subset(in_interact2,  (child == 4) | (child ==  5) | (child ==  6) | (child ==  7) | (child ==  8) | (child == 10) | (child == 11) | (child == 12) | (child == 13) | (child == 15) | (child == 16))
postures <- subset(in_interact, (child == 4) | (child ==  5) | (child ==  6) | (child ==  7) | (child ==  8) | (child == 10) | (child == 11) | (child == 12) | (child == 13) | (child == 15) | (child == 16))

write.csv(features, "~/Dropbox/DATA/STYLEBOT/features_fulls.csv")
write.csv(postures, "~/Dropbox/DATA/STYLEBOT/postures_fulls.csv")

all_child <- read.csv("~/Dropbox/DATA/STYLEBOT/all_child.csv") ### wafa's bf
features <- subset(all_child,  (child == 4) | (child ==  5) | (child ==  6) | (child ==  7) | (child ==  8) | (child == 10) | (child == 11) | (child == 12) | (child == 13) | (child == 15) | (child == 16))

features <- read.csv("~/Dropbox/DATA/STYLEBOT/features_fulls.csv") ### wafa's bf
postures <- read.csv("~/Dropbox/DATA/STYLEBOT/postures_fulls.csv") ### bodies
summary(all_child)
head(postures)

feapos <- merge(postures, features, by=c('time','child','session','style','activity','versatility','id','nb_ske'), all.x=TRUE)
feapos <- merge(in_interact, postures, by='time')
summary(postures$time)
summary(feapos$time)

write.csv(feapos, "~/Dropbox/DATA/STYLEBOT/mergefeapos_fulls.csv")

zfeatures <- data.frame()
attach(features)
zfeatures <- features[,c('time','child','session','style','activity','versatility','id','nb_ske','style2')]
zfeatures$SchegloffBPdistance <- scale(features$SchegloffBPdistance, center = TRUE, scale = TRUE)
zfeatures$style2 <- features$style2
summary(features)


attach(features)
attach(postures)

############################
#### DESCRIPTIVE ANALYISS
fname<-'~/Dropbox/WRITING/MonThese/Figures/plots/Stylebot/'
#style
summary(style2)
png(paste(fname,'style_all_interact.png',sep=""), width=400,height=400)
pie(summary(style2),col=c(red[1],blue[1]), main="# of capture data frames by style")
dev.off()

#activity
summary(activity)
png(paste(fname,'activity_all_interact.png',sep=""), width=400,height=400)
pie(summary(activity),col=rainbow(6), main="repartition of capture data frames by event")
dev.off()

#versatity
summary(versatility)
png(paste(fname,'versatility_all_interact.png',sep=""), width=400,height=400)
pie(summary(versatility),col=heat.colors(2), main="# of capture data frames by versatility")
dev.off()

# sesiion
summary(session)
png(paste(fname,'versatility_all_interact.png',sep=""), width=400,height=400)
pie(session,col=rainbow(2), main="# of capture data frames by versatility")

#child
summary(child)
png(paste(fname,'child_all_interact.png',sep=""), width=400,height=400)
pie(summary(factor(child)),col=rainbow(16), main="# of capture data frames per child")
dev.off()
#######################################

################ z treatments##########
###linking
# dsitances
features$zJointDistance <- scale(features$JointDistance, center = TRUE, scale = TRUE)
features$zSchegloffBPdistance<- scale(features$SchegloffBPdistance, center = TRUE, scale = TRUE)
postures$zJointP_SpineMid_X<- scale(postures$JointP_SpineMid_X, center = TRUE, scale = TRUE)
postures$zJointP_SpineMid_Z<- scale(postures$JointP_SpineMid_Z, center = TRUE, scale = TRUE)
postures$zJointP_Head_X<- scale(postures$JointP_Head_X, center = TRUE, scale = TRUE)
postures$zJointP_Head_Z<- scale(postures$JointP_Head_Z, center = TRUE, scale = TRUE)
test <- cbind(features$zJointDistance,features$zSchegloffBPdistance,features$style2)
destest<-describeBy(test[,-3],group=style2)
destest$Authoritative["mean"]

test2 <- cbind(postures$zJointP_SpineMid_X,postures$zJointP_SpineMid_Z,postures$zJointP_Head_X, postures$zJointP_Head_Z,postures$style2)
destest2<-describeBy(test[,-3],group=style2)
destest2$Authoritative["mean"]

forestplot(c("JointDistance","schegloffd","spinex","spinez","headx","headz"), 
           mean = cbind(HRQoL$Sweden[, "coef"], HRQoL$Denmark[, "coef"]),
           lower = cbind(HRQoL$Sweden[, "lower"], HRQoL$Denmark[, "lower"]),
           upper = cbind(HRQoL$Sweden[, "upper"], HRQoL$Denmark[, "upper"]),
           clip =c(-.125, 0.075),
           col=fpColors(box=c("blue", "darkred")),
           xlab="Linking index")
#####################################

#############################   STYLES
red=c("#F8766D","#ffa29c","#ffe0de")
blue=c("#00BFC4","#7ed4d6","#b4f3f4")
############### Liking
fname<-'~/Dropbox/WRITING/MonThese/Figures/plots/Stylebot/Liking_all_interact/'

### Proxemic Distance
describeBy(features$SchegloffBPdistance, group=features$style)
describeBy(features$JointDistance, group=features$style)
describeBy(postures$JointP_SpineMid_X, group=postures$style)
describeBy(postures$JointP_SpineMid_Z, group=postures$style)
describeBy(postures$JointP_Head_X, group=postures$style)
describeBy(postures$JointP_Head_Z, group=postures$style)

ggplot(postures, aes(x = postures$JointP_SpineMid_X, y = postures$JointP_SpineMid_Z, colour = style)) + geom_point() + facet_grid(~style)
Lateral_Distance= postures$JointP_SpineMid_X
Frontal_Distance=postures$JointP_SpineMid_Z
postures$style2 <- factor(postures$style, labels = c("Authoritative", "Permissive"))
features$style2 <- factor(features$style, labels = c("Authoritative", "Permissive"))
png(paste(fname,'positionxz.png',sep=""), width=400,height=400)
p <- ggplot(postures, aes(Lateral_Distance,Frontal_Distance) )
h3<-p + stat_bin2d(bins=100) + scale_fill_gradientn(colours=heat.colors(100), 
                                                    trans="log",guide=FALSE)+facet_grid(~style2) 
dev.off()

Lateral_Distance= postures$JointP_Head_X
Frontal_Distance=postures$JointP_Head_Z
p <- ggplot(postures, aes(Lateral_Distance,Frontal_Distance) )
h3<-p + stat_bin2d(bins=100) + scale_fill_gradientn(colours=heat.colors(100), ,guide=FALSE)+facet_grid(~style2) 


png(paste(fname,'jointdistance.png',sep=""), width=400,height=400)
  p <- ggplot(features, aes(factor(style2),JointDistance))
   p + geom_boxplot(aes(fill=factor(features$style2))) + guides(fill=FALSE) 
dev.off()
aov.distance.style <- anova(lm(JointDistance~features$style2))
print(aov.distance.style)
png(paste(fname,'zjointdistance.png',sep=""), width=400,height=400)
  features$zJointDistance <- scale(features$JointDistance, center = TRUE, scale = TRUE)
  p <- ggplot(zfeatures, aes(factor(zfeatures$style2),zfeatures$JointDistance))
  p + geom_boxplot(aes(fill=factor(zfeatures$style2))) + guides(fill=FALSE)+ylim(-1,1)
dev.off()


p <- ggplot(features, aes(factor(features$style2),SchegloffBPdistance))
h3 <-p + geom_boxplot(aes(fill=factor(features$style2))) + guides(fill=FALSE)
zfeatures$SchegloffBPdistance <- scale(features$SchegloffBPdistance, center = TRUE, scale = TRUE)
p <- ggplot(zfeatures, aes(factor(zfeatures$style2),SchegloffBPdistance))
h3 <-p + geom_boxplot(aes(fill=factor(zfeatures$style2))) + guides(fill=FALSE)+ylim(-1,1)

p <- ggplot(postures, aes(factor(style2), postures$JointP_SpineMid_Z))
h3<-p + geom_boxplot(aes(fill=factor(postures$style2)))  +guides(fill=FALSE)
p <- ggplot(postures, aes(factor(style2), postures$JointP_SpineMid_X))
h3<-p + geom_boxplot(aes(fill=factor(postures$style2)))  +guides(fill=FALSE) + coord_flip()

### Forward Lean
describeBy(features$KinectLeanY, group=features$style2)
p <- ggplot(features, aes(factor(style2),KinectLeanY))
h3 <- p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)+  ylab("Forward Lean") + theme(axis.title.x = element_blank())    
zfeatures$KinectLeanY <- scale(features$KinectLeanY, center = TRUE, scale = TRUE)
p <- ggplot(zfeatures, aes(factor(style2),KinectLeanY))
h3 <- p + geom_boxplot(aes(fill=factor(zfeatures$style2)))  +guides(fill=FALSE)+  ylab("Forward Lean") + theme(axis.title.x = element_blank())    


describeBy(features$calBLA_z,group=features$style2)
p <- ggplot(features, aes(factor(style2),calBLA_z))
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)+  ylab("Forward Lean") + theme(axis.title.x = element_blank())    
zfeatures$calBLA_z <- scale(features$calBLA_z, center = TRUE, scale = TRUE)
p <- ggplot(zfeatures, aes(factor(style2),calBLA_z))
h3<-p + geom_boxplot(aes(fill=factor(zfeatures$style2)))  +ylim(-1,1)+guides(fill=FALSE)+  ylab("Forward Lean") + theme(axis.title.x = element_blank())    

p <- ggplot(features, aes(factor(style2), features$torso_rollx))+  ylab("Torso forward Lean") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)
zfeatures$torso_rollx <- scale(features$torso_rollx, center = TRUE, scale = TRUE)
p <- ggplot(features, aes(factor(style2), features$torso_rollx))+  ylab("Torso forward Lean") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)+ylim(-1,1)

### Body Orientation, 
p <- ggplot(features, aes(factor(style2), features$calBLA_y))
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE) +  ylab("Sideways Torque") + theme(axis.title.x = element_blank())    

p <- ggplot(features, aes(factor(style2), features$SchegloffBPhipTorque))+  ylab("Sideways Hip Torque") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)

p <- ggplot(features, aes(factor(style2), features$SchegloffBPtorsoTorque))+  ylab("Sideways Torso Torque") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)

p <- ggplot(features, aes(factor(style2), features$SchegloffBPshoulderTorque))+  ylab("Sideways Shoulder Torque") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)

p <- ggplot(features, aes(factor(style2), features$torso_pitchy)) +  ylab("Torso Torque") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)

p <- ggplot(features, aes(factor(style2), features$torso_yawz)) +  ylab("Torso sideways Lean") + theme(axis.title.x = element_blank())    
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)

### Observation (stability of necks orientation in Robot area)
p <- ggplot(features, aes(factor(style2), features$head_rollx*180/pi))## 
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE) +  ylab("Head Roll") + theme(axis.title.x = element_blank())    

p <- ggplot(features, aes(factor(style2), features$head_pitchy*180/pi))
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +guides(fill=FALSE)+  ylab("Head Pitch") + theme(axis.title.x = element_blank())    


############################# RELAXATION
fname<-'~/Dropbox/WRITING/MonThese/Figures/plots/Stylebot/Relaxing_all_interact/'
### Sideways Lean
describeBy(features$KinectLeanX, group=features$style2)
png(paste(fname,'sideways_leanK.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2),KinectLeanX))
h3 <- p + geom_boxplot(aes(fill=factor(features$style2))) +coord_flip() +guides(fill=FALSE)+  ylab("Sideways Lean") + theme(axis.title.y = element_blank())    
h3
dev.off()

png(paste(fname,'blAX.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$BodyLeanAnglex))
h3<-p + geom_boxplot(aes(fill=factor(features$style2)))  +coord_flip() +guides(fill=FALSE)+  ylab("Sideways Lean") + theme(axis.title.y = element_blank())    
h3
dev.off()

### Arm-Posistion Asymetry, 
describeBy(features$HandAsym, group=features$style2)
png(paste(fname,'handAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2),HandAsym))
h3 <- p + geom_boxplot(aes(fill=factor(features$style2)))+ ylim(0,1)+ guides(fill=FALSE)+  ylab("Hands Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()
anova(lm())

describeBy(features$WristAsym, group=features$style2)
png(paste(fname,'wristAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$WristAsym))
h3<-p + geom_boxplot(aes(fill=factor(features$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Wrist Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()

describeBy(features$ElbowAsym, group=features$style2)
png(paste(fname,'elbowAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$ElbowAsym))
h3<-p + geom_boxplot(aes(fill=factor(features$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Elbow Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()

for(i in c(4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16)){
  print(i)
  achild<-subset(in_interact, child==i)
  name<-paste(fname,'elbowAsym',sep="" )
  name<-paste(name,i,sep="")
  name<-paste(name,'png',sep='')
  png(paste(name, width=400,height=400))
  p <- ggplot(features, aes(factor(style), features$ElbowAsym))
  h3<-p + geom_boxplot(aes(fill=factor(features$style))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Elbow Asymmetry") + theme(axis.title.x = element_blank())    
  h3
  dev.off()
  name<-paste(fname,'handAsym',sep="" )
  name<-paste(name,i,sep="")
  name<-paste(name,'png',sep='')
  png(paste(name, width=400,height=400))
  p <- ggplot(features, aes(factor(style), features$ElbowAsym))
  h3<-p + geom_boxplot(aes(fill=factor(features$style))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Hand Asymmetry") + theme(axis.title.x = element_blank())    
  h3
  dev.off()
  name<-paste(fname,'wristAsym',sep="" )
  name<-paste(name,i,sep="")
  name<-paste(name,'png',sep='')
  png(paste(name, width=400,height=400))
  p <- ggplot(features, aes(factor(style), features$ElbowAsym))
  h3<-p + geom_boxplot(aes(fill=factor(features$style))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Hand Asymmetry") + theme(axis.title.x = element_blank())    
  h3
  dev.off()
  line <- readline()
}


###LegPosition Asymmetry,  
describeBy(features$FootAsym, group=features$style2)
png(paste(fname,'feetAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2),FootAsym))
h3 <- p + geom_boxplot(aes(fill=factor(features$style2)))+ ylim(0,1)+ guides(fill=FALSE)+  ylab("Feet Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()

describeBy(features$AnkleAsym, group=features$style2)
png(paste(fname,'ankleAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$AnkleAsym))
h3<-p + geom_boxplot(aes(fill=factor(features$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Ankle Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()

describeBy(features$KneeAsym, group=features$style2)
png(paste(fname,'kneeAsym.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$KneeAsym))
h3<-p + geom_boxplot(aes(fill=factor(features$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Knee Asymmetry") + theme(axis.title.x = element_blank())    
h3
dev.off()

###Forward Lean, 
#cf above

###Neck Relaxation, 


###Hand Relaxation, 
#0 unknow
#1 not treacked
#2 open
#3 closed
#4 lasso
features <- all_child
features$LeftHandState<- factor(features$LeftHandState)
features$RightHandState<- factor(features$RightHandState)
features$LeftHandStatus<- factor(features$LeftHandState)
features$RightHandStatus<- factor(features$RightHandState)
features$RightHandStatus[features$RightHandStatus == 0] <- NA
features$RightHandStatus[features$RightHandStatus == 1] <- NA
features$LeftHandStatus[features$LeftHandStatus == 0] <- NA
features$LeftHandStatus[features$LeftHandStatus == 1] <- NA
attach(features)
summary(features$LeftHandStatus)
autoritaf <- subset(features, style=='auto')
permf <- subset(features, style=='perm')
autoritaf <- subset(all_child, style=='auto')
permf <- subset(all_child, style=='perm')

png(paste(fname,'lefthandstate.png',sep=""), width=400,height=400)
h3<-pie(c("open"=1330, "closed"=5104,"lasso"=608), col=red, border=FALSE, main="Left Hand Status")
h3
dev.off()


resume <-summary(permf$LeftHandStatus)
png(paste(fname,'lefthandstateperm.png',sep=""), width=400,height=400)
pie(c("open"=resume[[3]], "closed"=resume[[4]],"lasso"=resume[[5]]), col=blue, border=FALSE, main="Left Hand Status")
dev.off()
resume[5]
#(resume[[3]]+resume[[4]]+resume[5]])
1084/(1084+4468+776)

resume <- summary(autoritaf$RightHandStatus)
png(paste(fname,'righthandstateauto.png',sep=""), width=400,height=400)
pie(c("open"=resume[[3]], "closed"=resume[[4]],"lasso"=resume[[5]]), col=red, border=FALSE, main="Right Hand Status")
dev.off()

resume <- summary(permf$RightHandStatus)
png(paste(fname,'righthandstateperm.png',sep=""), width=400,height=400)
pie(c("open"=resume[[3]], "closed"=resume[[4]],"lasso"=resume[[5]]), col=blue, border=FALSE, main="Right Hand Status")
dev.off()

###Arm Openness, 
postures$armopenness <- sqrt((postures$JointP_HandRight_X-postures$JointP_HandLeft_X)*(postures$JointP_HandRight_X-postures$JointP_HandLeft_X)+
                               (postures$JointP_HandRight_Y-postures$JointP_HandLeft_Y)*(postures$JointP_HandRight_Y-postures$JointP_HandLeft_Y)+
                             (postures$JointP_HandRight_Z-postures$JointP_HandLeft_Z)*(postures$JointP_HandRight_Z-postures$JointP_HandLeft_Z))
describeBy(postures$armopenness, group=postures$style2)
png(paste(fname,'armopeness.png',sep=""), width=400,height=400)
p <- ggplot(postures, aes(factor(style2), postures$armopenness))
h3<-p + geom_boxplot(aes(fill=factor(postures$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Arm Openness") + theme(axis.title.x = element_blank())    
h3
dev.off()

postures$armopennessbis <- sqrt((postures$JointP_WristRight_X-postures$JointP_WristLeft_X)*(postures$JointP_WristRight_X-postures$JointP_WristLeft_X)+
                               (postures$JointP_WristRight_Y-postures$JointP_WristLeft_Y)*(postures$JointP_WristRight_Y-postures$JointP_WristLeft_Y)+
                               (postures$JointP_WristRight_Z-postures$JointP_WristLeft_Z)*(postures$JointP_WristRight_Z-postures$JointP_WristLeft_Z))
describeBy(postures$armopennessbis, group=postures$style2)
png(paste(fname,'armopeness-writs.png',sep=""), width=400,height=400)
p <- ggplot(postures, aes(factor(style2), postures$armopennessbis))
h3<-p + geom_boxplot(aes(fill=factor(postures$style2))) + ylim(0,1) +guides(fill=FALSE)+  ylab("Arm Openness") + theme(axis.title.x = element_blank())    
h3
dev.off()


###Rocking rate
plot(x= features$time_rel, y=features$KinectLeanY,col=features$style2, type = 'l')
quiz1<-subset(features, activity == "quiz1")
quiz2<-subset(features, activity == "quiz2")
dances<-subset(features, activity == "dance")
quiz_features <-rbind(quiz1,quiz2)
rocking_forback <-diff(features$KinectLeanY)
features$rock<- rbind(0,rocking_forback)

require(data.table)
rockingdf <- data.table(features)
rockingdf$rocking<-rockingdf[ , list(child,style2,time,time_rel,activity,Diff=diff(rockingdf$KinectLeanY))  ]
ggplot(rockingdf, aes(x=time_rel, y=rocking))+geom_line(aes(color=style2))+ facet_wrap(~child, ncol=4)


ggplot(quiz_features, aes(x=time_rel, y=KinectLeanY))+geom_line(aes(color=style2))+ facet_wrap(~child, ncol=4)

#################### COLD/WARM


#################### DOMINANCE
fname<-'~/Dropbox/WRITING/MonThese/Figures/plots/Stylebot/Dominance_all_interact/'
### Volume
theme_set(theme_gray(base_size = 18))
describeBy(features$calcvolume, group=features$style2)
png(paste(fname,'bodyvolume.png',sep=""), width=400,height=400)
p <- ggplot(features, aes(factor(style2), features$calcvolume))
h3<-p + geom_boxplot(aes(fill=factor(features$style2))) + ylim(0,0.5) +guides(fill=FALSE)+  ylab("Body Volume") + theme(axis.title.x = element_blank())    
h3
dev.off()

p <- ggplot(in_interact, aes(factor(style), calcvolume))
h3<-p + geom_boxplot(aes(fill=factor(style))) + ylim(0,0.5) +guides(fill=FALSE)+  ylab("Body Volume") + theme(axis.title.x = element_blank())    
h3
p <- ggplot(in_interact, aes(factor(style), calcvolume))
h3<-p + geom_boxplot(aes(fill=factor(style))) + ylim(0,0.5) +guides(fill=FALSE)+  ylab("Body Volume") + theme(axis.title.x = element_blank())  +facet(~child)  
h3



### self touch
summary(features$LeftHandTouch)
names(features)
hand_touch <- data.frame(features[c("style", "style2", "versatility", "activity", "session", "child", "time", "time_rel", "LeftHandTouch", "RightHandTouch")])
write.csv(hand_touch, "~/Dropbox/DATA/STYLEBOT/handtouch_fulls.csv")
hand_touch <- read.csv("~/Dropbox/DATA/STYLEBOT/handtouch_fulls.txt", sep='\t')
levels(hand_touch$LeftHandTouch1)
levels(hand_touch$RightHandTouch1)
#############################################
#############################   VERSATILITY
##############################################
names(postures)


######LOW LEVEL MOTION DES
## for each session/child, determine
### duraction of each activity
attach(postures)
child <- factor(child)
duration <- function(){
  for(i in levels(child))
    print(i)
    achild<-subset(postures, child==i and session ==1)
    
    desc<-describeBy(achild$time, group=achild$activity)
    min(achild$time)
    max(achild$time)
    achild$time_rel<-achild$time - min(achild$time)
    new_data<-rbind(new_data,achild)
}






######################## TOOLS
#colors
gg_color_hue <- function(n) {
     hues = seq(15, 375, length=n+1)
     hcl(h=hues, l=65, c=100)[1:n]
 }