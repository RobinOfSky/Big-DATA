import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# matplotlib 中文 负号的支持
mpl.rcParams["font.family"] = "SimHei"
mpl.rcParams["axes.unicode_minus"] = False


#条形图的制作

x=["机器学习","人工智能","深度学习","数据处理","数据开发","数据挖掘","数据分析"]
y=[53,69,41,78,57,26,23]

plt.figure(figsize=(10,5),dpi=80)

plt.bar(range(len(x)),y,width=0.5,color="green")

#将x轴的刻度与x的值相匹配，并设置旋转的角度
plt.xticks(range(len(x)),x,rotation=45)

plt.title("学习某些技术的人数")
plt.xlabel("技术")
plt.ylabel("人数")

plt.grid(alpha=0.4)

plt.show()
