##########################################################
## SCRIPT FOR Analysing MidTerm Grades                  ##
## By Farhang.Fp                                        ##
## Oct 1st 2020                                         ##
## Computational Thinking                               ##
##########################################################

### Define the working directory 
setwd('C:\\Users\\Farha\\Dropbox\\Farhang (1)\\Computational Thinking Material- ENGR1330\\5th Week')

### Read the full data
data <- read.csv('MidTermFull.csv')
data
IC <- data[,3]
TH <- data[,4]
T73 <- data[,5]
Tp <- data[,6]

#Summary
summary(IC)
summary(TH )
summary(T73 )


par(mfrow=c(2,2))
boxplot(IC,horizontal=TRUE,col="goldenrod1",main="In-Class Grades (out of 23)")
text(x=fivenum(IC), labels =fivenum(IC), y=1.25)

boxplot(TH,horizontal=TRUE,col="darkorange2",main="Take-home Grades (out of 50)")
text(x=fivenum(TH), labels =fivenum(TH), y=1.25)

boxplot(T73,horizontal=TRUE,col="darkred",main="Total Grades (out of 73)")
text(x=fivenum(T73), labels =fivenum(T73), y=1.25)

boxplot(Tp,horizontal=TRUE,col="deeppink3",main="Total Grades (percentage)")
text(x=fivenum(Tp), labels =fivenum(Tp), y=1.25)


















