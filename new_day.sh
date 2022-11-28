#!/bin/bash

if test ${#1} -eq 2
then
	touch input/in$1_real.txt
	touch input/in$1_test.txt
	cp -v code00.py code$1.py
	sed -i "s/##/$1/g" code$1.py
else
	touch input/in0$1_real.txt
	touch input/in0$1_test.txt
	cp -v code00.py code0$1.py
	sed -i "s/##/0$1/g" code0$1.py
fi
