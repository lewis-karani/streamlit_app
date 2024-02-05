pip install matplotlib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Generate dataset

df = pd.read_csv("hsp_data.csv")

# Streamlit app
st.title("This is my streamlit app")
st.header("This page describes analysis on the differential expression of Heat Shock Proteins in Plasmodium falciparum")

#Background
st.header("Study Background")
"""
Molecular chaperones are proteins that facilitate the folding of other proteins, thus enabling them to acquire the correct 3D structure necessary for their function and by doing so, they prevent and reverse stress-induced protein misfolding in the cell. The heat shock protein 90(HSP90) constitutes this family of chaperones. Heat shock proteins are essential for the survival of the most virulent malaria parasite, Plasmodium  falciparum and play a major role when the parasite encounters stress as it moves from the vector to human host, mediating malaria pathogenesis. The protozoan parasite P.falciparum adapts to its environment by translocating these HSP90  for its survival. Hsp90 is a chaperone protein that enables the parasite circumvent challenges such as febrile episodes and drug pressure in the host. Subsequently, PfHSP90 may constitute the hub that drives drug resistance in malaria parasites. By comparing the expression levels of HSP90 in untreated and treated samples, the study aimed to determine if there was a significant difference in expression levels and whether this difference could potentially be used as a marker of drug efficacy. This would provide important insights into the mechanisms of drug action against malaria and contribute to the development of new therapeutic strategies for the disease.
"""
# Display the dataset
st.header("HSP90_Metadata")
st.dataframe(df)

#Methodology
st.header("Methods")
"""
This was a cross sectional study that focused on Plasmodium falciparum positive blood samples collected from a stable malaria transmission zone in Kenya. Ribonucleic acid (RNA) was extracted from Whatman dried blood spots from archived clinical isolates for day 0 (before treatment) and day 2 (after treatment) and purified. Forty-five samples were randomly chosen.  Quantitative real time PCR was used to amplify the HSP90 gene mRNA in the samples using species-specific primers. Each sample was amplified in triplicate with a house keeping gene, Beta-actin included. Average Ct was calculated and the fold change between HSP90 expression at day 0 and day 2 computed using the 2^-(∆∆Ct) method. Statistical analysis was also done to determine the correlation between different parameters
"""
# Summary statistics
st.header("Descriptive_statistics")
st.write(df.describe())
 
 #Show expression change between day0 and day2
x_bar = df["subjid"]
y_bar = df["fold_change"]
plt.bar(x_bar, y_bar)
plt.xlabel("Samples")
plt.ylabel("HSP90 expression")
plt.title("Fold change in HSP90 expression btn day0 and day2")
plt.show()

#Results
st.header("Results")
"""
Of the forty-five blood samples included in the study, HSP90 gene expression was compared between day 0 and day 2 samples from the same patients. A fold difference of >1.6 was used as an indication of a twofold increase in the gene expression levels. Fifteen out of 45 (33%) samples showed at least a twofold increase in HSP90 expression levels. 8/15 (53.3%) had a twofold increase. 3/15 (20%) had a threefold increase, with single samples out of the 15 (6.7%) showing a 4-, 5-, 7-, and 9-fold increase. A fold difference of <0.6 was taken to define a downregulation in HSP90 expression. From the samples analyzed, 12 of the 45 (27%) showed a downregulation in HSP90 expression between the febrile and treated samples. The remaining population, n=18 (40%) showed the same expression levels between the febrile and treated sample population. 
"""
# Correlation matrix
st.header("Correlation Matrix")
numeric_df = df.select_dtypes(include=['float64', 'int64'])
st.write(numeric_df.corr())

# Plot of expression 

df = pd.DataFrame({
    'subject_id': df["subjid"],
    'expression_day0': df["expression_malaria"],
    'expression_day2': df["expression_treatment"]
})

# Plot the line graph using Matplotlib
plt.plot(df['subject_id'], df['expression_day0'], label='Day 0', color='blue')
plt.plot(df['subject_id'], df['expression_day2'], label='Day 2', color='green')

# Set labels and title
plt.xlabel('Subject ID')
plt.ylabel('Gene Expression')
plt.title('Gene Expression Changes from Day 0 to Day 2')

# Show legend
plt.legend()

# Show the plot
plt.show()













