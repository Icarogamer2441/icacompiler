import compiler
import sys

output_file_name = sys.argv[1] # the output name will be the argument 1 after the argument 0 (argument 0 will be the compiler.py after the python command)

compiler.start(outputname=output_file_name)

compiler.createstrvar("mseg", "hello ")
compiler.prtvar("mseg")
compiler.createstrvar("msgb", "world\\n")
compiler.strcpy("mseg", "msgb") # change the value of mseg to the value of msgb
compiler.prtvar("mseg") # print "world" and new line because of changing the value to msgb
compiler.msg("Whats your name? ")
compiler.strinp("name")
compiler.msg("Welcome ")
compiler.prtinp("name")
compiler.asciimsg("65")
compiler.asciimsg("10")

compiler.end()
