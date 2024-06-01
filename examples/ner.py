import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from src.ner_distilbert.nel_distilbert import extract_name_and_last_name


example_text = '''
Adele D. Villanueva
1698 Pointe Lane
Hollywood, FL 33023

Mother's maiden name
Oneal
SSN
264-16-XXXX
Geo coordinates
26.03843, -80.305673
PHONE
954-967-1963
Country code
1
BIRTHDAY
November 15, 1975
Age
48 years old
Tropical zodiac
Scorpio
ONLINE
Email Address
AdeleDVillanueva@armyspy.com
Website
chadandjackie.com
Browser user agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
'''
result = extract_name_and_last_name(example_text)
print(result)