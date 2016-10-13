

select_skeleton <- function(subdoy,e){
  #e4
  ids_e4 = c('72057594037928448','72057594037935776')
  
  #e7s2
  ids_e7s2=c('72057594037935424','72057594037937136')
  
  # e9s1
  ids_e9s1 =  c('72057594037932704','72057594037932176')
  
  # e10s2
  ids_e10s2 = c(' 72057594037938640', '72057594037943152')
  
  #e11s2
  ids_e11s2 = c('72057594037931328','72057594037932016')
  
  # e13s1
  ids_e13s1=c('72057594037929056','72057594037930080')
  
  #e14s1
  ids_e14s1=c('72057594037935584')
  
  #e16s1
  ids_e16s1 = c('72057594037929600','72057594037930272')
  
  
  if (e=='4') {
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e4));

  }
  else if (e=='7S2'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e7s2))
  }
  else if (e=='9S1'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e9s1))
  }
  else if (e=='10S2'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e10s2))
  }
  else if (e=='11S2'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e11s2))
  }
  else if (e=='13S1'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e13s1))
  }
  else if (e=='14S1'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e14s1))
  }
  else if (e=='16S1'){
    subdoy = subset(subdoy, is.element(subdoy$id,ids_e16s1))
  }
  return(subdoy)
} 


all_childess = c('4','5S1','5S2','6S1','6S2','7S1','7S2','8S1','8S2','9S1','10S2','10S1','11S1',
                 '11S2','12S1','12S2','13S1','13S2','14S1','14S2','15S1','15S2','16S1','16S2')
for (e in all_childess){
  fname = paste0(paste0("/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/Enfant",e,sep=""),
                 "/skeleton/body_joints_labelized.timestamp",sep="")
  print(fname)
  body_joints_labelized <- read.csv(fname)
  t = table(as.factor(body_joints_labelized$id),body_joints_labelized$activity)
  print(t)
  t = data.frame(t)
  ids = subset(t, t$Freq!=0 & (t$Var2 == 'dance' | t$Var2 == 'quiz1' | t$Var2 == 'quiz2'))
  ids = unique(ids$Var1)
  print(ids)
  subdoy = subset(body_joints_labelized, is.element(body_joints_labelized$id, ids))
  table(as.factor(subdoy$id),subdoy$activity)
  if(length(ids)!=1){
    subdoy = select_skeleton(subdoy,e)
    
    
    #p = ggplot(subdoy, aes(x=as.factor(subdoy$time), y=subdoy$JointP_SpineMid_X, colour=as.factor(subdoy$activity),
    #                 group=as.factor(subdoy$id)))+ geom_line() 
    #print(p)
  }
 
  foname = paste0(paste0("/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_e",e,sep=""),
                 ".csv",sep="")
  print(foname)  
  write.csv(subdoy,foname)
  
  
  cat ("Press [enter] to continue")
  line <- readline()
  
}


all_childess = c('5S1','5S2','6S1','6S2','7S1','7S2','8S1','8S2','9S1','10S2','10S1','11S1',
                 '11S2','12S1','12S2','13S1','13S2','14S1','14S2','15S1','15S2','16S1','16S2')

e='4'
foname = paste0(paste0("/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_e",e,sep=""),
                ".csv",sep="")
print(foname)  
posture= read.csv(foname)
attach(posture)
posture = posture[order(time),]
posture$time_rel = seq.int(nrow(posture))
for (e in all_childess){
  foname = paste0(paste0("/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_e",e,sep=""),
                  ".csv",sep="")
  print(foname)  
  posture_c = read.csv(foname)
  attach(posture_c)
  posture_c = posture_c[order(time),]
  posture_c$time_rel = seq.int(nrow(posture_c))
  posture = rbind(posture,posture_c)
  attach(posture)
  
}
foname = "/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_all.csv"
print(foname)  
posture = posture[order(time, child),]
write.csv(posture,foname)

head(posture$time_rel)

ske_all <- read.csv("/media/wafa/Johal/DATA_ANALYSIS/STYLEBOT/SKELETONS/csv_files/ske_all.csv")
colnames(ske_all)

ggplot(subdoy, aes(x=as.factor(subdoy$time), y=subdoy$JointP_SpineMid_X, colour=as.factor(subdoy$activity),group=as.factor(subdoy$id)))+ geom_line() 
