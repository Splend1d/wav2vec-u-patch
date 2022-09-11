# +
import matplotlib.pyplot as plt
libri960jsd4 = [0.005849,0.1697,0.07850,0.2635]
libri960jsd4_30000 = [0.08223,0.1332,0.1070,0.2213]
libri960jsd4_3000 = [0.2478,0.3525,0.3420,0.3647]
libri960per = [20.25,26.02,21.83,31.59]
libri960per_30000 = [23.46,22.65,22.40,34.05]
libri960per_3000 = [36.07,85.73,88.74,62.22]
plt.scatter(libri960jsd4 + libri960jsd4_30000+libri960jsd4_3000,libri960per + libri960per_30000+libri960per_3000, facecolors='none',color="blue")
libri9dot6jsd4 = [0.07201,0.2228,0.1375, 0.3003]
libri9dot6per = [22.51,29.03,24.65,105]
libri9dot6jsd4_3000 = [0.2478,0.3525,0.3420, 0.3647]
libri9dot6per_3000  = [33.03,78,-1,-1]
plt.scatter(libri9dot6jsd4+libri9dot6jsd4_3000,libri9dot6per+libri9dot6per_3000,color="blue",marker="+",s=100)
# accentjsd4 = [0.2475,0.2718,0.2229, 0.3406,0]
# accentper  = [86.37,-1,86.1114,-1,20.35]
# plt.scatter(accentjsd4,accentper,color= "orange",marker="*",s=100)
SB300jsd4 = [ 0.1357,
 0.2513,
0.1499,
0.3174,0]

SB300per  = [92.1030,94.1236,95.2556,89.97,35.8031]

SB300per_SB  = [44.3800,35.8031,43.3315,66.6672,32.3447]
plt.scatter(SB300jsd4,SB300per,color= "black",marker="D")
plt.scatter(SB300jsd4,SB300per_SB,color= "black",marker="d", facecolors='none')
#SBjsd4 = [0.2248,-1,-1, -1,0,0.08668]
#SBper  = [95.8623,-1,-1,-1,95.1334,93.4818]
#plt.scatter(SBjsd4,SBper,color= "black",marker="D")
TED500jsd4 = [ 0.08803,0.1825,0.08410, 0.2678,0]
TED500per  = [31.6240,35.2112,32.0563,41.87,28.1339]
TED500jsd4_3000 = [0.2927]
TED500per_3000 = [88.7887]

TED10jsd4 = [0.1909,0.2855,0.1928, -1,0,0.1014]
TED10per  = [36.0068,88.26,33.5211,85.92,29.13,32.4414]
TED10jsd4_3000 = [0.3128]
TED10per_3000 = [87.0413]
plt.scatter(TED500jsd4+TED500jsd4_3000,TED500per+TED500per_3000,color= "red",marker = "*", facecolors='none')
plt.scatter(TED10jsd4+TED10jsd4_3000,TED10per+TED10per_3000,color= "red",marker = "x")

plt.legend(['Libri960','Libri9.6',"SB300_w2v2","SB300_w2v2all","TED500","TED10"], loc ="upper left")
#plt.hlines(40,-0.01,0.4,color="black",linestyles="dashed")
plt.ylim((0,110))
plt.xlim(-0.01,0.4)
plt.xlabel("4gram JSD")
plt.ylabel("PER")
#plt.xscale('log')
plt.savefig("JSD-PERall.pdf",bbox_inches='tight')
plt.show()

# +
import matplotlib.pyplot as plt
libri960jsd4 = [0.005849,0.1697,0.07850,0.2635]
libri960jsd4_30000 = [0.08223,0.1332,0.1070,0.2213]
libri960jsd4_3000 = [0.2478,0.3525,0.3420,0.3647]

libri960jsd3_3000 = [0.07877,0.1488,0.1318,0.1791]
libri960jsd3_30000 = [0.01415,0.05945,0.03779,0.1116]
libri960jsd3 = [0.001422,0.1005,0.03652,0.1584]

libri960jsd2_3000 = [0.1791,0.03150,0.01958,0.05192]
libri960jsd2_30000 = [0.001726,0.01898,0.009890,0.03795]
libri960jsd2 = [0.0003695,0.04589,0.01178,0.06900]

libri960jsd1_3000 = [0.003134,0.003110,0.002154,0.008696]
libri960jsd1_30000 = [0.0005311,0.002503,0.001469,0.006461]
libri960jsd1 = [0.0001425,0.01359,0.002031,0.02089]

libri960per = [20.25,26.02,21.83,31.59]
libri960per_30000 = [23.46,22.56,22.40,34.05]
libri960per_3000 = [36.07,85.73,88.74,62.22]

plt.scatter(libri960jsd1 + libri960jsd1_30000+libri960jsd1_3000,libri960per + libri960per_30000+libri960per_3000, facecolors='none',color="black",marker = "*",s=100)
plt.scatter(libri960jsd2 + libri960jsd2_30000+libri960jsd2_3000,libri960per + libri960per_30000+libri960per_3000,color="orange",marker = "+",s=100)
plt.scatter(libri960jsd3 + libri960jsd3_30000+libri960jsd3_3000,libri960per + libri960per_30000+libri960per_3000, facecolors='none',color="red",marker = "D")
plt.scatter(libri960jsd4 + libri960jsd4_30000+libri960jsd4_3000,libri960per + libri960per_30000+libri960per_3000, facecolors='none',color="blue")

plt.legend(['1-gram','2-gram','3-gram','4-gram'])
#plt.annotate("LibriLM", (0.005849, 20.25),xytext=(-0.5, -5),textcoords="offset points",arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("wiki103", (0.1697, 26.02),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("NewsCrawl", (0.07850, 21.83),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("ImageCorpus", (0.2635, 31.59),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("LibriLM", (0.005849, 20.25),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("LibriLM", (0.005849, 20.25),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))
#plt.annotate("LibriLM", (0.005849, 20.25),xytext=(0.004, 10),arrowprops=dict(arrowstyle='-', color='black', linewidth=2))

#plt.hlines(40,-0.01,1,color="black",linestyles="dashed")
plt.ylim((0,110))
#plt.xlim(-0.01,0.4)
# plt.title("JSD-PER between LibriSpeech960 and text")
plt.xlabel("JSD")
plt.ylabel("PER")
plt.xscale('log')

plt.savefig("JSD-PER.pdf",bbox_inches='tight')
plt.show()
# -


