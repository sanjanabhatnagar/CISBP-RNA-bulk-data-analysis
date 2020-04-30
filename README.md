# CISBP-RNA-bulk-data-analysis

Alternative splicing is a tightly regulated process which forms a crucial layer of gene expression regulation and exerts its effects in a tissue-specific way. The cis-elements are sequence determinants of alternative splicing which are recognized by trans-factors that affect spliceosome recruitment and thus, result in diverse splicing patterns. 

We had a list of potential enhancers (cis-elements that enhance the inclusion of an alternate exon) and silencers (cis-elements that suppress the inclusion of an alternate exon). In order to find the motifs present in these elements and the corresponding RNA binding proteins these bind to, we chose the CISBP-RNA Database: Catalog of Inferred Sequence Binding Preferences of RNA binding proteins. 

The Bulk downloads section on http://cisbp-rna.ccbr.utoronto.ca was accessed and entire catalogue of inferred sequence binding preferences of RNA binding proteins for all species was downloaded.

The folder contains Z-scores, E-scores, Motif logos etc.

Z-score file was used to find the strongest motif matches for our elements (pilot experiment). 

The file contains Z-scores for each motif across 16,832 7mer sequences. There were total 245 motifs and corresponding information. 

Data analysis results in following in csv files for each activator and repressors category-

•	CISBP_HighestZScores_Motifs-2 – This file only contains the Z-scores which were highest across all the motifs for a given sequence (Column = 0).  Column 0 contains the strongly matched motifs i.e. the exact same motif is present within the element. 

Whereas, column 2 consists of those motifs which bear some sequence resemblance with the sequence of element but aren’t exact matches. The column consists of good-enough matches and not exact matches considering the individual motif cut-offs (scores above means i.e. in the 75th quartile).

According to the literature –“A compendium of RNA-binding motifs for decoding gene regulation Debashish Ray, Hilal Kazan, […]Timothy R. Hughes” -for each motif the strongest 7mer matches were found using the corresponding Z-score (FDR<0.1, corrected for all motifs. If the scores were significantly higher than the mean, the 7mer was considered to be a strong match for the given motif.

•	E-scores had a well-defined cut-off in the paper (0.45). E-scores file was also analysed for both repressors and activators, separately. Results can be found in EScores_RepressorsCISBPMotifs.csv and EScores_ActivatorsCISBPMotifs.csv. 

As expected, same motifs came up in the E-score file analysis with a few exceptions. Two new motifs which weren’t reported in Z-score analysis i.e. M186_0.6 for ID 68 cis-element (repressor) and M050_0.6 for ID 37 barcode (repressor) were found as well. These motifs have considerable similarity with the motifs reported after Z-score analysis for both elements. The logos seem to be quite similar. They even bind similar RBPs in the case of element 37B but for element 68E, RBPs are different but belong to same family.

•	Considering the motif matches, corresponding RBPs were found from RBP_all_information file. Files Rep_RBP_Motifs.csv and Act_RBP_Motifs.csv consist of elements, motifs which were strong matches and the corresponding RBP names and the species which they belong to.


•	Ranked_Elements_Zscores.csv file consists the ranks of the elements (in terms of motif matches) based on the Z-scores. There were total 16,832 sequences. 
•	Rank_distributions.jpeg contains box and whisker plot of the ranks of significant activators and repressors and the ranks of all insignificant elements (both which were rejected after and before the Holme-Bonferroni corrections.)



Following text is from README.txt from the CISBP bulk downloads folder-


Escores/Zscores.txt - these text files are matrices providing the E- and
Z-scores from each RNAcompete assay, for all 16,382 possible 7-mers.  E-scores
range from -0.5 to +0.5; 7-mers with E-scores >= 0.45 are considered "strongly
bound" by the associated RBP.  Z-scores can have arbitrary ranges, with higher
scored indicating stronger binding.  See Ray et al. Nature 2013 for additional
details.


Important link - http://hugheslab.ccbr.utoronto.ca/supplementary-data/RNAcompete_eukarya/ 
