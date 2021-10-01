import pandas as pd
import numpy as np
import scipy.stats as stat

lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

sig_threshold = 0.05

# lifespan of vein pack subscribers
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']

# avergae lifespan of vein pack subscribers
avg_vein_pack_lifespans = np.mean(vein_pack_lifespans)
print('Average Vein Pack subscribers lifespan:')
print(round(avg_vein_pack_lifespans,1))

# to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 73 years
tstat, pval = stat.ttest_1samp(vein_pack_lifespans, 73)
print('P-value of one sample t-test:')
print(pval)
result = ('Vein Pack subscribers avergae lifespan is significantly longer than 73 years' if pval < sig_threshold else 'There is NO significant difference between the average lifespan of Vein Pack subscribers and 73 years')
print(result)

# lifespan of artery pack subscribers
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
# avergae lifespan of artery pack subscribers
avg_artery_pack_lifespans = np.mean(artery_pack_lifespans)
print('Average Artery Pack subscribers lifespan:')
print(round(avg_artery_pack_lifespans,1))

# to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack
tstat, pval = stat.ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print('P-value of two sample t-test:')
print(pval)
result = ('There is a significant difference in the avergae lifespan of Vein and Artery Packs' if pval < sig_threshold else 'There is NO significant difference between the average lifespan of Vein and Artery Packs')
print(result)

# to find if there is an association between the pack that a subscriber gets (Vein vs. Artery) and their iron level
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)
chi2, pval, dof, expected = stat.chi2_contingency(Xtab)
print(pval)
result = ('There is a significant association between type of pack (Vein vs. Artery)  someone subscribes to and thier level of iron' if pval < sig_threshold else 'There is NO association between the type of pack (Vein vs. Artery) someone subscribes to and their iron level')
print(result)
