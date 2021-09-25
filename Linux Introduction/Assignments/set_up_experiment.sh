#!/bin/bash
cd ~/
mkdir $1
cd $1
mkdir Code Data Figures Writeup
cd Data
mkdir processed raw

echo "$1 directory created in your home directory"