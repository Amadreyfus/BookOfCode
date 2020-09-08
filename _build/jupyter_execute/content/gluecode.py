(glue_code)=
# GlueCode

from myst_nb import glue

c0 = []
t_insert = %timeit -o -n3000 -r100 c0.insert(0, 'a')

glue('t_insert', t_insert)

c1 = []
t_append = %timeit -o -n3000 -r100 c1.append('a')

glue('t_append', t_append)

#Verify that both lists are the same
assert all([a == b for a, b in zip(c0, c1)]), "Answers differed?"

# Report the ratio of execution times
print(f"\n==> (insert time) / (append time) for 300,000 ops: ~ {t_insert.average/t_append.average}x")

glue('t_ratio', (t_insert.average/t_append.average))

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot') # Displays graph in the style of R's ggplot

x = np.linspace(0,10)
y = np.sin(x)
fig = plt.plot(x,y)

glue('basic_sin', fig, display=False)

