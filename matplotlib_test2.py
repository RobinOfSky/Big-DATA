import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
# matplotlib 中文 负号的支持
mpl.rcParams["font.family"] = "SimHei"
mpl.rcParams["axes.unicode_minus"] = False

x=["机器学习","人工智能","深度学习","数据处理","数据开发","数据挖掘","数据分析"]
y=[53,69,41,78,57,26,23]

plt.plot(range(len(x),y)

plt.xticks(range(len(x),x,rotation=45)

plt.show()

