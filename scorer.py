import re
import config

class OffenseScorer(object):
    def __init__(self, input_dict):
        self.input_dict = input_dict
        self.score_dict = {}

    def _calculate_score(self, text):
        self.score = self._count_low_risk(text) + (self._count_high_risk(text) * 2)      
        return self.score

    def _count_low_risk(self,text):
        self.low_risk_count = len(re.findall(config.LOW_RISK_RE, text))
        return self.low_risk_count

    def _count_high_risk(self, text):
        self.high_risk_count = len(re.findall(config.HIGH_RISK_RE, text))
        return self.high_risk_count

    def get_score(self):
        for name, text in self.input_dict.items():
            score = self._calculate_score(text)
            self.score_dict[name] = score
        return self.score_dict