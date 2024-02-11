from typing import List, Tuple, Dict
import regex as re
import sys

Part = Dict[str, int]
Range = Tuple[int, int]
Rule = Tuple[str, bool, int, str]

class Workflow():
    def __init__(self, identifier:str, rules:List[Rule], default:str):
        self.identifier = identifier
        self.rules = rules
        self.default = default
        
    def apply(self, part:Part)->str:
        for rule in self.rules:
            category, greater, threshold, referral = rule
            if greater:
                if part[category] > threshold: return referral 
            else:
                if part[category] < threshold: return referral 
        return self.default
        
    def apply_range(self, valrange:Range)->Dict[str, Range]:
        referrals = {rule[3]:[] for rule in self.rules}
        referrals[self.default] = []
        
        for rule in self.rules:
            category, greater, threshold, referral = rule
            start, end = valrange[category]
            if greater:
                if end > threshold: 
                    valrange_new = valrange.copy()
                    valrange_new[category] = (max(start, threshold+1), end)
                    referrals[referral].append(valrange_new)
                    valrange[category] = (start, threshold)
            else:
                if start < threshold: 
                    valrange_new = valrange.copy()
                    valrange_new[category] = (start, min(end, threshold-1))
                    referrals[referral].append(valrange_new)
                    valrange[category] = (threshold, end)
        referrals[self.default].append(valrange)
        return referrals

def main():
    name = 'input'

    #Read input - trying out regular expressions
    pattern = re.compile('([a-z]*)\{((?:[xmas][><]\d+:[a-zA-Z]+,)+)([a-zA-Z]+)\}$')
    rule_pattern = re.compile('([xmas])([><])(\d+):([a-zA-Z]+),')

    part_pattern = re.compile('([xmas]=\d+)')

    with open("inputs/day19/{}.txt".format(name)) as file:
        workflows = {}
        for line in file:
            if len(line.strip()) == 0:
                break
            groups = pattern.match(line).groups()
            identifier = groups[0]
            rules = [(category, (greater == '>'), int(threshold), referral) for (category, greater, threshold, referral) in (match.groups() for match in rule_pattern.finditer(groups[1]))]
            default = groups[2]
            workflows[identifier] = Workflow(identifier, rules, default)
    
        parts = [{category:int(value) for (category, value) in (string.split('=') for string in part_pattern.findall(line))} for line in file]

    #Task 1
    accepted_rating = 0
    for part in parts:
        referral = 'in'
        while not referral in ['A', 'R']:
            referral = workflows[referral].apply(part)
        if referral == 'A': accepted_rating += sum(part.values())
    
    print("Sum of accepted ratings:", accepted_rating)
    
    #Task 2
    accepted_number = 0
    
    referrals = {'in':[{char:(1, 4000) for char in 'xmas'}]}
    while len(referrals) > 0:
        referrals_new = {referral:[] for referral in workflows}
        referrals_new['A'] = []
        referrals_new['R'] = []
        for referral in referrals:
            for valrange in referrals[referral]:
                for (referral, ranges) in workflows[referral].apply_range(valrange).items():
                    referrals_new[referral] += ranges
        for valrange in referrals_new.pop('A'):
            accepted_temp = 1
            for category in valrange:
                accepted_temp *= (valrange[category][1]-valrange[category][0]+1)
            accepted_number += accepted_temp
        referrals_new.pop('R')
        referrals = {referral:ranges for (referral, ranges) in referrals_new.items() if len(ranges)>0}
        
    print("Number of accepted values:", accepted_number)
        
if __name__ == "__main__":
    sys.exit(main())