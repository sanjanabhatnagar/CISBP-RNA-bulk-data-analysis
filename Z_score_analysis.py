import pandas as pd
import os
import sys


r = pd.read_csv(sys.argv[1], sep = "\t")
Cis_el_file = open(sys.argv[2])
r2 = pd.DataFrame(r)

'''
Converting the content into a DataFrame explicitly.

For sequence scans, we performed a one-sided Z test for each motif on its sequence scores, and defined ‘strong motif matches’ as those with scores significantly higher than the mean (FDR <0.1, corrected for all motifs).
Ref : "A compendium of RNA-binding motifs for decoding gene regulation Debashish Ray, Hilal Kazan, […]Timothy R. Hughes"
'''
feat = r2.describe()

'''
Any value above the cutoff for a particular motif would make the corresponding 7mer a strong match. 
Whereas for every 7mer, the highest value across the row would mean the strongest match is with that particular motif amongst all other motifs(i.e. the other ones for which this 7mer passed the cutoff)

'''
Cutoffs = feat.loc['75%'] # The final cutoff list (containing cutoffs for each motif column).


'''
Searching Cis_El barcode and cis-elements within the Z-score DataFrame. Barcode and cis-element IDs are appeneded with the respective elements.

'''
Cis_El=[]
for a in Cis_el_file:
    Cis_El.append(a)


Cis_El_info = {}
Cis_El_info2 = {}
Motifs_allCis_El = []
for a in Cis_El:
    seven_mers_in_Cis_El = []
    Strong_Motifs_in_Cis_El = []
    strong_motifs_list = []
    All_Cis_El_Motifs = []
    Other_motif_matches = []
    for c in r2['7mer']:
        if c in a:
            z = (r2.loc[r2[r2['7mer']==c].index.values]).T
            l=1
            maxval = 0
            while (l < 245):
                if maxval < z.iloc[l].values:# Looking for the strongest motif match among all other motifs #For E-score analysis use this condition - ((z.iloc[l].values > 0.45) or (z.iloc[l].values == 0.45))
                    maxval = z.iloc[l].values
                    Sev_mer = pd.DataFrame(z.loc['7mer'].values) # Using pd.DataFrame as it removes the descriptors like Name:, dtype:. Don't know how it exactly works
                    Motifname_Index_Zscore = pd.DataFrame(z.iloc[l])
                    Motifname = r2.columns[l]
                    for_rbp_scrip = z.iloc[l]
                if Cutoffs[l-1] < z.iloc[l].values:  # Over here looking for other strong motif matches for a given sequence for which the sequence's Z-score crossed the cutoff
                    Other_motif_matches.append(pd.DataFrame(z.iloc[l]))
                l = l+1
            Strong_Motifs_in_Cis_El.append(Motifname_Index_Zscore)
            seven_mers_in_Cis_El.append(Sev_mer)
            All_Cis_El_Motifs.append(Motifname)
            Motifs_allCis_El.append(Motifname)
            strong_motifs_list.append(for_rbp_scrip)
    Extracted_info = pd.Series([Strong_Motifs_in_Cis_El, seven_mers_in_Cis_El, Other_motif_matches])
    Cis_El_info.update({a: Extracted_info})
    Cis_El_info2.update({a : All_Cis_El_Motifs})
    

'''
Put value equal to z for a general table and put Extracted_info for just the Extracted_infoest z-score and corresponding motif.
df.to_csv('Cis_ElCISBP_ZScores_Format2.csv')  Over format 2, I prefer format 3, but the code for format 3 has yet to be automated.
'''
df = pd.DataFrame.from_dict(Cis_El_info, orient="index")
df2 = pd.DataFrame.from_dict(Cis_El_info2, orient="index")
df.to_csv("Desktop/Zscr_Ana_CisEls.csv")

# Extracting the strongly matched motifs (for all Cis_El)


