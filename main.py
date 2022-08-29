import os
import seaborn as sns
import array
import numpy as np
import math
import pandas as pd
import subprocess
import shutil
from threshoulding import *



# Replace csv formal and input file from the list.


element_extraction_only()
nodes_2_extraction()

# just replace per_75 with the value printed below to get 75 percent of the  thing
low = 50

# percent
threshoulding(low)

# print(threshoulding(10)*10)
