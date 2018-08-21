
##Usage:

In terminal enter app directory `cd scorer`

Run script using `run python main.py <directory>` using directory of input files.
In this case `run python main.py input_files`

Output file will be saved to current directory as output.txt

#Risk Files

A regular expression is built from texts under risk_files directory.
Currently delimited using `\n`, but can be configured using `getRegex(low_risk_phrases, "<delimiter>")`

#Scorer Class

Basic usage:

`osb = OffenseScorer(file_dict)` where file_dict is a dictionary of {filename: text}

`osb.get_score()` returns dictionary of {filename: score}

