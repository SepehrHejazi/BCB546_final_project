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
DESeq analysis was done following the DESeq vignette (http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html#heatmap-of-the-count-matrix). After FDR correction was applied, there were only 13 significantly regulated genes. Heatmap was made with top 35 p-adjusted genes. A heatmap that only includes 13 significant is provided. 
limma analysis was done following the limma vignette by Law et al., 2015 "RNA-seq analysis is easy as 1-2-3 with limma, Glimma and edgeR" (http://bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html). Ater differential expression analysis using empirical Bayes statistics, there were only 12 significantly regulated genes as shown by the heatmap provided. 
