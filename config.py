import os
import re
from utils import getRegex, readFile

low_risk_phrases = readFile("risk_files/low_risk_phrases.txt")
LOW_RISK_RE = getRegex(low_risk_phrases, "\n")

high_risk_phrases = readFile("risk_files/high_risk_phrases.txt")
HIGH_RISK_RE = getRegex(high_risk_phrases, "\n")