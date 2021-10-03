# Reproducible Research Workshop

## Perry Williams

## October 2, 2021

## Project Description

The reproducible research workshop covers basic usage of R, RStudio, Latex, and knitr to develop a workflow for research documentation and reproduction. The reproducible research workshop was developed from the bookReproducible Research with R and RStudio, by Christopher Gandrud.

## Video Lectures

- [Introduction](https://youtu.be/5isfqu7dhmk)
- [Installation](https://youtu.be/qk4YiRPovNM)
- [LaTeX](https://youtu.be/Ec3jqBKuXyk)
- [knitR](https://youtu.be/LGOApODWJlE)
- [Conclusion](https://youtu.be/C1Xv3riRZno)

## Overview of files

### Rep-Res-Workshop

The parent directory for the workshop is a file called Rep-Res-Workshop. Within this file are three files, including Analysis, Data, and Presentation.

#### Analysis

The analysis file contains an R script file calledMainAnalysis.R that was used to analyze vian species richness in the United States. It also contains a sub-file called ResultsFigures, which includes .pdf output of figures from theMainAnalysis.Rfile.

#### Data

The data file contains the avian species richness data.csv file used in theMainAnalysis.R
script.

#### Presentation

The presentation file contains seven sub-files. Four files contain examples used during the workshop. Two files contain exercises used during the workshop. One file contains the documents requried to compile the workshop lecture pdf.

## Installing the Main Software for the Workshop

Before coming to the workshop you should install the main software. All of the software programs covered in the workshop are open source and can be easily downloaded for free. They are available for Windows, Mac, and Linux operating systems. They should run well on most modern computers.

You should install R before installing RStudio. You can download the programs from the following websites:

- [R](http://www.r-project.org/)
- [RStudio](http://www.rstudio.com/ide/download)

The dowload webpages for these programs habe comprehensive information on how to install them, so please refer to those pages for more information. After installingRamdRStudioyou will want to install a number of user-writen packages that are covered in this workshop. To install all of these user-written packages, run the following command in R:

```{r}
required.packages=c("formatR","here","knitr","Matrix")
lapply(required.packages,install.packages,character.only=TRUE)
lapply(required.packages,library,character.only=TRUE)
```

## Installing markup language

To create LATEXdocuments you need to install a TEXdistribution. They are available for Windows, Mac, and Linux systems. They can be found at: [http://www.latex-project.org/ftp.html](http://www.latex-project.org/ftp.html). Please refer to that site for more
installation information.

## Session Info

```{r}
toLatex(sessionInfo())
```

- R version 3.6.0 (2019-04-26),x86_64-apple-darwin15.6.
- Locale:
  en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-
- Running under:macOS Mojave 10.14.
- Matrix products: default
- BLAS:
  /Library/Frameworks/R.framework/Versions/3.6/Resources/lib/libRblas.0.dylib

- LAPACK: /Library/Frameworks/R.framework/Versions/3.6/Resources/lib/libRlapack.dylib

- Base packages: base, datasets, graphics, grDevices, methods, stats, utils
- Other packages: formatR 1.7, here 0.1, knitr 1.25, Matrix 1.2-
- Loaded via a namespace (and not attached): backports 1.1.4, compiler 3.6.0, evaluate 0.14, grid 3.6.0, highr 0.8, lattice 0.20-38, magrittr 1.5, rprojroot 1.3-2, stringi 1.4.3, stringr 1.4.0, tcltk 3.6.0, tools 3.6.0, xfun 0.
