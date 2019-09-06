import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# matplotlib 中文 负号的支持
mpl.rcParams["font.family"] = "SimHei"

#多个条形图的组合


plt.figure(figsize=(20,8),dpi=60)

a=["猩球崛起3","蜘蛛侠","战狼2","复仇者联盟4"]
b_14=[2358,399,2358,362]
b_15=[12357,156,2045,168]
b_16=[15748,312,4497,319]

#设置a在x轴上显示的相对位置
bar_width = 0.3
x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+2*bar_width for i in x_14]

plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

#设置a现实的额位置
plt.xticks(x_15,a)

#添加图例
plt.legend()

plt.show()