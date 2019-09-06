from matplotlib import pyplot as plt
import numpy as np

#自变量和应变量
x=np.random.randint(0,20,20)
y_1=range(10,30)
y_2=range(5,25)

_xticks_label=range(0,30)
_yticks_label=range(0,40)

#设置图片的大小
fig=plt.figure(figsize=(10,5),dpi=80)

#设置图片的标题
plt.title("sample img")

#设置轴的刻度
plt.xticks(_xticks_label[::2])
plt.yticks(_yticks_label[::3])

#设置网格
plt.grid(alpha=0.6)

#显示x,y(linestyle="--   ,-  , :  ,.  ,  .-   ")
plt.plot(x,y_1,label="first",color="red",linewidth=2,alpha=0.6)
plt.plot(x,y_2,label="second",color="green",linewidth=3,alpha=0.3)

#显示图例
#plt.legend(loc="upper left")
#打印图像
plt.show()

#保存图片
#plt.savefig("./test.png")
