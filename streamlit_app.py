import streamlit as st
import pandas as pd
import plotly.express as px


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
fig = px.bar(x=x_bar, y=y_bar, labels={"x": "Samples", "y": "Expression change"}, title="HSP90 fold change btn day0 and day2")
fig.write_html("plot1.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot1.html")
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

# Melt the DataFrame to convert it to long format
df_melted = pd.melt(df, id_vars=["subject_id"], var_name="day", value_name="expression")

# Plot the line graph using Plotly Express
fig = px.line(df_melted, x="subject_id", y="expression", color="day",
              color_discrete_map={"expression_day0": "blue", "expression_day2": "green"},
              labels={"expression": "HSP90 Expression", "subject_id": "Subject ID"},
              title="HSP90 Expression Change between Day 0 and Day 2")
fig.write_html("plot.html")

# Automatically open a browser of your plot                 
import webbrowser
webbrowser.open("plot.html")


# Research insights
st.header("Research Insights")
st.write("""
Correlation of the HSP90 expression at day 0 with admission temperature gave a correlation value of -0.0984 which shows a weak negative correlation with no statistical significance p =  0.0717 while correlation with parasitemia at admission gave a value of -0.0633 at a p value of 0.00000135 showing statistical significance (p < 0.05). This shows that parasitemia, not temperature, value may be a confident predictor for the expression of HSP90 at the febrile stage. Correlating the fold change in HSP90 expression with parasitemia at day 0 gave a correlation value of 0.1596 at a p value of 0.2951 while correlation with parasitemia after treatment(day 2) gave a coefficient of -0.0733 at a p value of 0.6324. This highlights a weak negative correlation with no statistical significance. Correlated with temperature at sampling(day 0), the fold change in HSP90 expression gave a coefficient of 0.1908 at a p value of 0.2092 showing a weak positive correlation that is not statistically significant. The change in HSP90 expression was correlated with temperature at time of sampling. Correlation of non-febrile patients gave a weak negative correlation coefficient of r = -0.1619 at a p value of 0.2880 showing no statistical significance. Correlation for febrile patients with low grade fever showed a weak positive correlation r = 0.0739 with a high p value 0.6297 indicating no statistical significance in the correlation. There was a weak positive correlation (r = 0.1751) between change in HSP90 expression and high-grade fever patients but the correlation was not statistically significant (p = 0.2500). The fold difference correlation variable showed no significant correlation with age categories. There was a very weak negative correlation between subject’s under-five years and fold difference (r = -0.0657), but the correlation was not statistically significant (p value = 0.6682). There was also a very weak positive correlation between over five years and fold difference (r = 0.0286), but the correlation was equally not statistically significant (p-value = 0.8520). Overall, the data suggests that HSP90 expression is not an ideal biomarker for antimalarial efficacy.
""")

# Streamlit app run command
if __name__ == '__main__':
    st.run()








