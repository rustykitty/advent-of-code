import sys
import re

towels, designs = sys.stdin.read().rstrip().split('\n\n')

towels, designs = towels.split(', '), designs.split('\n')

pattern = re.compile(rf'({"|".join(towels)})+')

print(sum(True for design in designs if pattern.fullmatch(design)))