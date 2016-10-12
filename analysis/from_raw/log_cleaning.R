
all_childess = c('4','5S1','5S2','6S1','6S2','7S1','7S2','8S1','8S2','9S1','10S2','10S1','11S1',
                 '11S2','12S1','12S2','13S1','13S2','14S1','14S2','15S1','15S2','16S1','16S2')
for (e in all_childess){
  fname = paste0(paste0("/media/wafa/Johal1/DATA_ANALYSIS/STYLEBOT/SKELETONS/Enfant",e,sep=""),
                 "/skeleton/body_joints_labelized.timestamp",sep="")
  print(fname)
  body_joints_labelized <- read.csv(fname)
  t = table(as.factor(body_joints_labelized$id),body_joints_labelized$activity)
  print(t)
  t = data.frame(t)
  ids = subset(t, t$Freq!=0 & (t$Var2 == 'dance' | t$Var2 == 'quiz1' | t$Var2 == 'quiz2'))
  ids = unique(ids$Var1)
  print(ids)
  subdoy = subset(body_joints_labelized, is.element(body_joints_labelized$id, ids$Var1))
  ggplot(subdoy, aes(x=as.factor(subdoy$time), y=subdoy$JointP_SpineMid_X, colour=subdoy$activity,group=subdoy$id))+ geom_line() +
    scale_colour_discrete_list()+ theme_Publication()
  cat ("Press [enter] to continue")
  line <- readline()
  
}



