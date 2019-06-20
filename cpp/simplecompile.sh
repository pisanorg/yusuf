#!/bin/bash

# simplecompile,sh: compile all cpp files as myprogram.exe and run some checks

# if you get the following error:
# -bash: ./simplecompile.sh: /bin/bash^M: bad interpreter: No such file or directory
# It means that the line-endings got changed between unix and Windows systems, to fix use:
# $ dos2unix simplecompile.sh

# make this file executable
# $ chmod 700 simplecompile.sh
# redirect the output and stderr from this file to output.txt
# $ ./simplecompile.sh > output.txt 2>&1


date

echo "*** Compiling"
g++ -std=c++11 -Wall -Wextra -Wno-sign-compare *.cpp -g -o myprogram.exe

echo "*** cpplint"
cpplint *.cpp

echo "*** cppcheck"
# cppcheck in CSS Linux Lab only knows about c++11
cppcheck --enable=all --force --inconclusive --language=c++ --std=c++11 --suppress=missingIncludeSystem *.cpp


echo "*** clang-tidy"
# perform all possible checks
# The "--" at the end is important. If cmake has created compile_commands.json file, it can be omitted
clang-tidy -checks="*" *.cpp --

echo "*** running"
./myprogram.exe

echo "*** running with valgrind"
valgrind ./myprogram.exe

echo "*** cleaning up"
rm myprogram.exe

date
