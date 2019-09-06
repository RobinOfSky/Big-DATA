import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# matplotlib 中文 负号的支持
mpl.rcParams["font.family"] = "SimHei"

#直方图的创建
a=[ 64,  94,  61,  75,  94,  33, 116,   3, 107, 112,  70,  74, 110,
        44,  96,  21,   0,  59,  55,  78,  25,  19,  77, 100,  13,  31,
       102, 116,  24,  12,  46,  25,  82,   6,  76,  46,  71,  13,  35,
       105,  13,  53,  93, 116,  48,  64,  18,  92,  31,   4,  61, 118,
       110, 119,  86,  72,  66,  93,  90,   4, 115,  59,  35,  51, 117,
        43,  67,  50, 113,  74,  93, 118,  96,  50,  50,  32,  83,  12,
        68,   3,  88,  22,  82,  39,   3, 112,  74,  63,  49,  53,  28,
        42,  98,  58,  11,  67, 114,  42,  56, 103,  89,   1,  80,  35,
        21,  97, 101,  61,  11,  10,  120,  78,  21, 101, 114,   7,  85,
       101,  97,  67]

bin_width=10
print(max(a),min(a),max(a)-min(a))
num_bins=int((max(a)-min(a))//bin_width)

plt.hist(a,num_bins)

plt.xticks(list(range(min(a),max(a)))[::bin_width],rotation=45)
plt.grid(True,linestyle="-",alpha=0.5)


plt.show()