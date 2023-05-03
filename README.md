# BCB546_final_project

## Raw Data Analysis
The raw data was first edited using UNIX and the following command for further analysis in R:
$  sed 's/@/>/g' SRR16039738.fasta > r1.fatsa
(The r1.fasta was uploaded to OneDrive and linked in R. The raw SRR16039738.fasta file was not uploaded due to size limitations.)

## Description of DESeq Analysis: 
Contains an R-markdown file "DESeqAnalysis.Rmd" with code used to re-create Figure 2, and analyze data and re-create supplementary table 2. The re-created heatmap includes "Heatmap_35_top_padj.png", which contains the top 35 DGEs in AGAT -/- compared to Wildtype with padj, and "DESeq_HeatMap_AGAT_control.png", which only includes genes that made it past FDR (13 total, which makes sense for miRs). Re-creation of supplementary table 2, or Significantly regulated miRNAs between wt and AGAT-/- mice, is found in "deficient_control_result". Contains original data "GSE184723_miRNA_read-counts.csv.gz". 

## Description Fig4_Analysis
Contains R-markdown file "Fig4_DESeq_Plots.Rmd" with code for using DESeq to attempt to recreate the MI part of figure 4 comparing MI to WT at three different time points (Day 1, Week 1, and Week 8). Also the .csv files from analysis and the original data files used "GSE114695_Gene_FC_P-val_FPKM.txt.gz" and "GSE114695_miR_FC_P-val_RPM.txt.gz".
