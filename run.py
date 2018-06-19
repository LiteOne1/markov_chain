
from markov_python_master.cc_markov import MarkovChain

#initiate class

x = MarkovChain()

x.add_file('lyrics.txt')
words = x.add_string('thriller')

for i in x.generate_text():
    print i,








