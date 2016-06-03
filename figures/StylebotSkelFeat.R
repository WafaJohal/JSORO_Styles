all_child <- read.csv("~/Dropbox/DATA/STYLEBOT/allchild_feat.csv")
postures_fulls <- read.csv("~/Dropbox/DATA/STYLEBOT/postures_fulls.csv")
attach(all_child)
attach(postures_fulls)
library(ggplot2)
summary(all_child)

quiz1<-subset(all_child, activity == "quiz1")
quiz2<-subset(all_child, activity == "quiz2")
dances<-subset(all_child, activity == "dance")
explanations<-subset(all_child, activity == "explain")
quiz_features <-rbind(quiz1,quiz2)

poly<-subset(all_child, versatility== "poly")
spe<-subset(all_child, versatility== "spe")

mydata<- poly
#############################
quiz1<-subset(mydata, activity == "quiz1")
quiz2<-subset(mydata, activity == "quiz2")
dances<-subset(mydata, activity == "dance")
explanations<-subset(mydata, activity == "explain")
quiz_features <-rbind(quiz1,quiz2)

pie(summary(style),col=rainbow(2), main="# of capture data frames by style")
pie(summary(activity),col=rainbow(6), main="repartition of capture data frames by event")
pie(session,col=rainbow(2), main="# of capture data frames by versatility")
pie(summary(factor(child)),col=rainbow(16), main="# of capture data frames per child")



poly<-subset(postures_fulls, versatility== "poly")
spe<-subset(postures_fulls, versatility== "spe")

mydata<- poly
#############################
quiz1<-subset(mydata, activity == "quiz1")
quiz2<-subset(mydata, activity == "quiz2")
dances<-subset(mydata, activity == "dance")
explanations<-subset(mydata, activity == "explain")
quiz_features <-rbind(quiz1,quiz2)

ggplot(dances, aes(x = JointP_SpineMid_X, y = JointP_SpineMid_Z, colour = style)) + geom_point() + facet_grid(~child)
ggplot(quiz_features, aes(x = JointP_Neck_X, y = JointP_Neck_Z, colour = style)) + geom_point() + facet_grid(~child)
ggplot(explanations, aes(x = com_x, y =com_z, colour = style)) + geom_point() + facet_grid(~child)




###############################




