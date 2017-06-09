'''
Draw a Venn diagram for two sets
'''
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
def draw_venn(sets):
 venn2(subsets=sets)
 plt.show()
Playing with Sets and Probability 141
if __name__ == '__main__':
 s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
 s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
 draw_venn([s1, s2])

 StudentID,Football,Others
1,1,0
2,1,1
3,0,1
--snip--

def read_csv(filename):
 football = []
 others = []
 with open(filename) as f:
 reader = csv.reader(f)
 next(reader)
 for row in reader:
 if row[1] == '1':
 football.append(row[0])
 if row[2] == '1':
 others.append(row[0])
 return football, others
