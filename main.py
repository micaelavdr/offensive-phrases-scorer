#!/user/bin/python
import argparse
import os
from scorer import OffenseScorer
from utils import readDirFiles

def main(path):

	print('Analyzing risks for text files in directory %s' % path)

	file_dict = readDirFiles(path)
	osb = OffenseScorer(file_dict)

	results = ""
	for name, score in osb.get_score().items():
		results += "%s : %s \n" % (name, score)

	file = open("output.txt", "w")
	file.write(results)

	print('Done. Scores are: \n')
	print(results)
	print('Results saved to %s' % os.path.abspath("output.txt"))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Sort files by offense score")
	parser.add_argument('path',type=str, help='path to directory of files to be sorted')
	args = parser.parse_args()
	main(args.path)