=====
creating our own WC tool
======

User input and output
===========

ccwc - Tool created for getting byte count, number of lines, characters, words using our own tool

/usr/local/bin/ccwc -c sample3.txt 
Number of bytes in 'sample3.txt': 3541

======================
Utility will count the words, lines and characters if you dont provide any flag specifically
pnagar448@NJSML-1731830 CodingChallenges % /usr/local/bin/ccwc sample3.txt 
Number of bytes in 'sample3.txt': 3541
Number of lines in 'sample3.txt': 21
Number of words in 'sample3.txt': 546
Number of characters in 'sample3.txt': 3541
=========================

if you provide specific flag while running the utility it will work accordingly 
pnagar448@NJSML-1731830 CodingChallenges % /usr/local/bin/ccwc -c sample3.txt
Number of bytes in 'sample3.txt': 3541
pnagar448@NJSML-1731830 CodingChallenges % /usr/local/bin/ccwc -w sample3.txt
Number of words in 'sample3.txt': 546
pnagar448@NJSML-1731830 CodingChallenges % /usr/local/bin/ccwc -l sample3.txt
Number of lines in 'sample3.txt': 21
=====================================

verified the output with wc and stat tool in mac and the result is matching with ccwc utility 
=========
