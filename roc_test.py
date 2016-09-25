import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve

actual = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
          0, 0, 1, 1, 0, 0, 1, 1, 0, 0]

classifier_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

classifier_b =  [1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

classifier_c = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0,
                1, 1, 1, 0, 0, 1, 1, 1, 0, 0]

classifier_d = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0,
                1, 1, 0, 0, 0, 1, 1, 0, 0, 0]

classifier_e = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
               
# This is the ROC curve
fpr, tpr, theshold  = roc_curve(actual, classifier_a)
fprb, tprb, thesholdb  = roc_curve(actual, classifier_b)
fprc, tprc, thresholdc = roc_curve(actual, classifier_c)
fprd, tprd, thresholdd = roc_curve(actual, classifier_d)
fpre, tpre, thresholde = roc_curve(actual, classifier_e)

line1, = plt.plot([0, 1], label="Line 1", linestyle='--')
plt.plot(fpr, tpr)
plt.plot(fprb, tprb)
plt.plot(fprc, tprc)
plt.plot(fprd, tprd)
plt.plot(fpre, tpre)
plt.show()
