# GeekHub-Python

Home work №8/1 'Parser'
The script 'parser.py' created for getting data from site 'http://quotes.toscrape.com'.

Functional program: 
	- receipt of quotations: all;
	- receipt of records of authors: all, by identifier;
	- receipt of records of tags: all;
	- record the received data in a file: txt, csv, json, xls.
	
Default settings (without parameters command prompt): receipt of quotations, record the received data in a txt file.

usage: parser.py [-h] [-g {quotes,authors,tags,.}] [-f {txt,csv,json,xls,.}]
                 [-a N [N ...]]

Select parser settings

optional arguments:
  -h, --help					show this help message and exit
  -g {quotes,authors,tags,.}	to select a parsing group
  -f {txt,csv,json,xls,.}		to select a format record file
  -a N [N ...]					to select a identifier of authors
  
Some examples: 
	python parser.py -a 1 3 14
	python parser.py -g authors -f json
	python parser.py -f csv
	python parser.py -g tags
	python parser.py