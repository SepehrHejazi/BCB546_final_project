# Introduction to original paper: 
## Reference: 
Jensen, M., Müller, C., Hübner, N. et al. Expression of cardiovascular-related microRNAs is altered in L-arginine:glycine amidinotransferase deficient mice. Sci Rep 12, 5108 (2022). https://doi.org/10.1038/s41598-022-08846-1
## background:
Authors are interested in the AGAT enzyme (L-arginine:glycine amidinotransferase), and its metabolites, creatine and homoarginine. They have been affiliated with myocardial infarction, heart failure, and ischemic stroke. 
## The aim: 
Expand the understanding of underlying molecular mechanisms of AGAT and its metabolites in cardiovascular disease. 
##The goals: 
1. Study AGAT-dependent regulation of miRNAs and association to cardiovascular disease

2. Determine whether AGAT-dependent changes in miRNA expression are related to either creatine or hArg

3. Study miRNA-mRNA interactions in AGAT-deficient mouse model to identify regulatory mechanisms within the cardiac AGAT metabolism

#  Technical details of your replication of analyses: 
## Figure # 2: 
Original figure number two is displaying significantly regulated miRNAs between wildtype and AGAT -/- mice. We attempted to replicate these results using both limma and DESeq2. 

DESeq analysis was done following the DESeq vignette (http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html#heatmap-of-the-count-matrix). After FDR correction was applied, there were only 13 significantly regulated genes. Heatmap was made with top 35 p-adjusted genes. A heatmap that only includes 13 significant genes is provided. Heatmap.2 was used instead of pheatmap due to compatibility issues - this resulted in a "chubby" heatmap with the heat scale on the top left instead of the top right, and horizontal instead of vertical. 

limma analysis was done following the limma vignette by Law et al., 2015 "RNA-seq analysis is easy as 1-2-3 with limma, Glimma and edgeR" (http://bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html). Ater differential expression analysis using empirical Bayes statistics, there were only 12 significantly regulated genes as shown by the heatmap provided. 

## Figure # 4: 
The original figure contained 4 bar graphs showing differential expression of 8 miRNAs. Three of the graphs compared widltype mice vs mice with induced myocardial infartcion at three different time points (1 day, 1 week, and 8 weeks). The 4th graph compared wildtype mice vs heart failure mice, I did not attemp to recreate this fouth graph.

Count data was abtained from the GEO Profiles database (GEO accession GSE114695). DESeq analysis was done following the DESeq vignette (http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html#heatmap-of-the-count-matrix). I was unablle to replicate the contrasts that the auhors did in order to correclty compare the conditions and times points.

Bar graohs to show differenctial expression were made using GGplot2. & out of the 8 candidate miRNAs showed some differencial expression which is what the authors saw also.

## Processing of raw data: 
