#Written by S.Sepehr_Hejazi
#3_7_2023 


import pandas as pd

# insert the path to your fastq file (sequenced data) and you excel sheet with miRNA data bank sequences
fastq_file = "path/to/your/fastq/file.fastq"
excel_file = "path/to/your/excel/sheet.xlsx"

# Reading the fastq file, striping the white spaces with strip(), selecting just the sequence lines with enumerate()
with open(fastq_file, 'r') as f:
    seq = [line.strip() for i, line in enumerate(f) if i % 4 == 1]

# exctracting the column of Mature1_Seq in the databank
df = pd.read_excel(excel_file)
mirnas = df['Mature1_Seq'].tolist()

# counting the number of each miRNA repeats in the fastq lines starting the dictionary from count=0
counts = {mirna: 0 for mirna in mirnas}

# finding the sequences to the miRNAs and count them
for s in seq:
    for mirna in mirnas:
        if mirna in s:
            counts[mirna] += 1

# Save the counts of each reference sequence to a CSV file
with open('counts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['miRNA', 'Count'])
    for  mirna in mirnas():
        writer.writerow([mirna, count])