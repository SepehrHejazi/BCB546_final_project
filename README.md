# BCB546_final_project

## Raw Data Analysis
The raw data was first edited using UNIX and the following command for further analysis in R:

```
$sed 's/@/>/g' SRR16039738.fasta > r1.fatsa 
```

The excel file created from the codes in the Raw Data Anlysis R markdown is uploaded in DeSeq folder. (The r1.fasta was uploaded to OneDrive and linked in R. The raw SRR16039738.fasta file was not uploaded due to size limitations.)

## mapping with reference miRNA
Due to the short length of miRNA sequences and the potential for even a single nucleotide difference to alter the miRNA's name and function, I chose to write my own mapping Python code using the 'find' function. While this approach may result in lower speed and could introduce false negative results, it ensures that there are no false positives. Alternatively, one could use free mapping libraries like Bowtie2 to perform the mapping. The code and a description of it can be found in the Python code (mappingV2.py) .

## Description of DESeq Analysis: 
Contains an R-markdown file "DESeqAnalysis.Rmd" with code used to re-create Figure 2, and analyze data and re-create supplementary table 2. The re-created heatmap includes "Heatmap_35_top_padj.png", which contains the top 35 DGEs in AGAT -/- compared to Wildtype with padj, and "DESeq_HeatMap_AGAT_control.png", which only includes genes that made it past FDR (13 total, which makes sense for miRs). Re-creation of supplementary table 2, or Significantly regulated miRNAs between wt and AGAT-/- mice, is found in "deficient_control_result". Contains original data "GSE184723_miRNA_read-counts.csv.gz". 

## Description of limma Analysis:
Contains an R-markdown file "limmaAnalysis_Final.Rmd" with code used to re-create Figure 2, and analyze data. The re-created heatmap includes "heatmap_DGE_WTvKO.png", which consists of the the top 12 DGEs in AGAT knockout mice compared to wildtype with Benjamini-Hochberg adjusted p-values less than or equal to 0.05. Other plots includes: (1) density plots of logCPM for pre-filtered ("pre-filtered_density plot.png") and filtered ("filtered_density plot.png") data, (2) boxplots of normalized ("Normalized_Count-Data.png") and un-normalized ("Un-normalized_Count-Data.png") count data in logCPM and (3) voom mean-variance trend compared to the empirical Bayes mean-variance trend ("Mean-variance trend.png"). Contains original data "GSE184723_miRNA_read-counts.csv.gz" and table of differential expression analysis for 226 miRNAs using limma and empirical Bayes method ("miRNA_limma_eBayes.csv").

## Description Fig4_Analysis
Contains R-markdown file "Fig4_DESeq_Plots.Rmd" with code for using DESeq to attempt to recreate the MI part of figure 4 comparing MI to WT at three different time points (Day 1, Week 1, and Week 8). Also the .csv files from analysis and the original data files used "GSE114695_Gene_FC_P-val_FPKM.txt.gz" and "GSE114695_miR_FC_P-val_RPM.txt.gz".

## Description of Jensen_et_al-2022.md file
This .md file introduces the original paper, explains the technical details of our replication of the analyses and summarizes our replication of the original results.
