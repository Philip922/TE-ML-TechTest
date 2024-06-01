import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from src.utils.fuzzy_match import fuzzy_matching


input_name = 'KAREN'
found_names = ['national', 'Karen', 'S.']
matches = fuzzy_matching(input_name, found_names)
print(matches)

input_last_name = 'DE LA CRUZ'
found_last_names = ['DE LA CRUX', '##g', 'Booking', 'Karen Susana', 'avip']
matches = fuzzy_matching(input_last_name, found_last_names)
print(matches)

input_name = 'Andrew'
found_names = ['Andm', 'Scott', 'M.']
matches = fuzzy_matching(input_name, found_names)
print(matches)
