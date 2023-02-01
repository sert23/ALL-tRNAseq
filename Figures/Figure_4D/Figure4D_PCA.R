##Libraries
library(factoextra)

library(heatmap3)
library(RColorBrewer)
library(colorRamps)
library(ggpubr)


setwd("C:/Users/Cris/Dropbox/TRABAJO/NL/Chantal/PCAs/")

##Read the files
df<-read.table("cellsALL.txt",header = T,sep = "\t" ,row.names=1)
annotation <- read.table("annotationCELLSall.txt",header=T,sep="\t",row.names=3)
annotation <- annotation[ order(row.names(annotation)),]

##PCA
tdf <- t(df)
tdf <- tdf[ order(row.names(tdf)), ]
res.pca <- prcomp(tdf, scale = TRUE)

fviz_pca_ind(res.pca, habillage=annotation$group, repel = TRUE, title = "",labelsize=5,
             pointsize=8,palette="futurama",invisible=c("quali"))+
  scale_shape_manual(values=c(20,20,20,20))+
  font("ylab", size = 18)+font("xlab", size=25)+
  font("x.text", size=18)+font("y.text", size=25)+
  font("legend.text",size=18)+font("legend.title",size=18)

