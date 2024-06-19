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
compiler.push(10)
compiler.push(20)
compiler.printstack()
compiler.printstack()
compiler.push(10)
compiler.push(20)
compiler.sumstk()
compiler.printstack()
compiler.push(30)
compiler.push(5)
compiler.substk()
compiler.printstack()
compiler.push(50)
compiler.push(100)
compiler.pop()
compiler.printstack()
compiler.createintvar("myint", 10)
compiler.prtintvar("myint")

compiler.createstrvar("msg", "Ive been printed from scratch!', 10, '")
compiler.newlabel()
compiler.mov("rax", "1")
compiler.mov("rdi", "1")
compiler.mov("rsi", "msg")
compiler.mov("rdx", "size_of_msg")
compiler.syscall()
compiler.createintvar("myint2", 20)
compiler.msg("myint + myint2:\\n")
compiler.sumvar("myint", "myint2")
compiler.prtintvar("myint")
compiler.msg("myint - myint2:\\n")
compiler.subvar("myint", "myint2")
compiler.prtintvar("myint")

# you can print negative numbers in printstack and in printintvar

compiler.end()
