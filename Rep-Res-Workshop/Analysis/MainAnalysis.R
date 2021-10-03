###########################################################
###
### Avian Species Richness Data Analysis
### Perry Williams
### 09/12/2020
###
###########################################################

###
### Set the working directory
###

setwd("/Users/pwill/Desktop/GRAD778_04_2020/Data")

###
### Load the avian species richness data
###

Data.tmp=read.csv("birds.csv")

###
### Look at the number of species versus the data
###

plot(Data.tmp$area,Data.tmp$spp)

###
### Alaska looks like an outlier, with a lot of area,
### and average number of species. Remove it from the
### analysis
###

Data=Data.tmp
## Data=Data.tmp[-2,]

###
### Plot species versus area, with Alaska removed
###

plot(Data$area,Data$spp)

###
### Assign response variable, y, and predictor variables
### x1 (area), x2 (temp), and x3 (precip).
###

y=Data$spp
x1=Data$area
x2=Data$temp
x3=Data$precip

###
### Fit a multiple linear regression model with response
### variable 'spp' (number of species) and predictor
### variables 'area', 'temp', and 'precip'
###

linMod=lm(y~x1+x2+x3)

###
### Summarize the model fit
###

summary(linMod)

###
### Made a plot of the marginal relationships between the
### response variable and each predictor variable
###

pdf(here("Analysis/ResultsFigures/Figure1.pdf"))

par(mfrow=c(3,1),mar=c(4,4,2,2))
plot(x1,y,pch=16,col=2)
plot(x2,y,pch=16,col=3)
plot(x3,y,pch=16,col=4)

dev.off()
