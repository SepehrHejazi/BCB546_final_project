# BCB546_final_project

## Description of DESeq Analysis: contains an R-markdown file "DESeqAnalysis.Rmd" with code used to re-create Figure 2, and analyze data and re-create supplementary table 2. The re-created heatmap includes "Heatmap_35_top_padj.png", which contains the top 35 DGEs in AGAT -/- compared to Wildtype with padj, and "DESeq_HeatMap_AGAT_control.png", which only includes genes that made it past FDR (13 total, which makes sense for miRs). Re-creation of supplementary table 2, or Significantly regulated miRNAs between wt and AGAT-/- mice, is found in "deficient_control_result". Contains original data "GSE184723_miRNA_read-counts.csv.gz". 

## Description Fig4_DESeq_Plots_Rmd
Contains R-markdown file with code for using DESeq to attempt to recreate the MI part of figure 4 comparing MI to WT at three different time points (Day 1, Week 1, and Week 8).
