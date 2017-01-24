#!/usr/bin/python
# -*- coding: utf-8 -*-

num_a_mult = range(1, 11)

for multiplos_uno in num_a_mult:
	
	print "\n" + "Tabla del " + str(multiplos_uno)
	+ "\n" + "------------"

	for multiplos_dos in num_a_mult:
		print str(multiplos_uno) + " x " + str(multiplos_dos)
		+ " = " + str(multiplos_uno*multiplos_dos)
