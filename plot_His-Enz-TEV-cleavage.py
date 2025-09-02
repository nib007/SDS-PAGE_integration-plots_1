import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import numpy as np

# --- 1. Data Loading and Preparation ---

# Paste the raw data into a string.
# I've taken the liberty of adding a "Protein" column name to the header
# based on the content in that column for easier filtering.
data = """Lane	Band No.	Band-Lane	Condition	pH	Salt	Urea	Protein	Protein Mol. Wt. (KDa)	Abs. Quant. (ug)	Rel. Quant.	Band %	Lane %
2	1	2-1	Not treated His-Enz	-	-	-		79.7	N/A	0.2	5.1	2.6
2	2	2-2	Not treated His-Enz	-	-	-	TEV protease	28.3	2.1	1.2	29.1	14.8
2	3	2-3	Not treated His-Enz	-	-	-		23.6	N/A	0.4	10.0	5.1
2	4	2-4	Not treated His-Enz	-	-	-	His-Enz	16.6	5.1	1.8	44.6	22.8
2	5	2-5	Not treated His-Enz	-	-	-	Enz	14.7	N/A	0.5	11.2	5.7
3	1	3-1	Test condition	6.0	0.1	0.0		79.7	N/A	0.2	3.8	2.2
3	2	3-2	Test condition	6.0	0.1	0.0	TEV protease	27.9	2.8	1.4	32.9	19.0
3	3	3-3	Test condition	6.0	0.1	0.0		23.3	N/A	0.4	9.8	5.7
3	4	3-4	Test condition	6.0	0.1	0.0	His-Enz	16.4	4.4	1.7	41.1	23.7
3	5	3-5	Test condition	6.0	0.1	0.0	Enz	14.6	N/A	0.5	12.4	7.2
4	1	4-1	Test condition	6.0	0.1	0.5		79.7	N/A	0.2	3.7	2.1
4	2	4-2	Test condition	6.0	0.1	0.5	TEV protease	28.0	3.0	1.4	34.1	19.1
4	3	4-3	Test condition	6.0	0.1	0.5		23.3	N/A	0.4	9.7	5.4
4	4	4-4	Test condition	6.0	0.1	0.5	His-Enz	16.5	4.8	1.8	43.4	24.3
4	5	4-5	Test condition	6.0	0.1	0.5	Enz	14.6	N/A	0.4	9.1	5.1
5	1	5-1	Test condition	6.0	0.1	1.0		80.1	N/A	0.1	3.5	2.0
5	2	5-2	Test condition	6.0	0.1	1.0	TEV protease	28.2	3.6	1.5	36.2	20.8
5	3	5-3	Test condition	6.0	0.1	1.0		23.5	N/A	0.4	9.7	5.6
5	4	5-4	Test condition	6.0	0.1	1.0	His-Enz	16.5	4.9	1.8	42.5	24.4
5	5	5-5	Test condition	6.0	0.1	1.0	Enz	14.7	N/A	0.3	8.2	4.7
6	1	6-1	Test condition	6.0	0.35	0.5		80.1	N/A	0.2	4.2	2.4
6	2	6-2	Test condition	6.0	0.35	0.5	TEV protease	28.6	3.2	1.4	35.0	19.7
6	3	6-3	Test condition	6.0	0.35	0.5		23.7	N/A	0.4	9.1	5.1
6	4	6-4	Test condition	6.0	0.35	0.5	His-Enz	16.8	4.6	1.7	42.0	23.6
6	5	6-5	Test condition	6.0	0.35	0.5	Enz	14.8	N/A	0.4	9.7	5.5
7	1	7-1	Molecular weight marker				Molecular weight marker	180.0	1.2	1.0	6.9	6.1
7	2	7-2	Molecular weight marker				Molecular weight marker	130.0	2.4	1.3	8.7	7.6
7	3	7-3	Molecular weight marker				Molecular weight marker	100.0	7.6	2.4	16.2	14.2
7	4	7-4	Molecular weight marker				Molecular weight marker	70.0	4.9	1.8	12.3	10.7
7	5	7-5	Molecular weight marker				Molecular weight marker	55.0	6.0	2.0	13.7	12.0
7	6	7-6	Molecular weight marker				Molecular weight marker	40.0	2.5	1.3	8.8	7.7
7	7	7-7	Molecular weight marker				Molecular weight marker	35.0	3.7	1.5	10.6	9.3
7	8	7-8	Molecular weight marker				Molecular weight marker	25.0	1.4	1.1	7.2	6.3
7	9	7-9	Molecular weight marker				Molecular weight marker	15.0	3.6	1.5	10.4	9.1
7	10	7-10	Molecular weight marker				Molecular weight marker	10.0	N/A	0.8	5.2	4.5
8	1	8-1	Test condition	6.8	0.05	0		81.3	N/A	0.2	4.4	2.3
8	2	8-2	Test condition	6.8	0.05	0	TEV protease	29.0	4.2	1.7	34.2	18.3
8	3	8-3	Test condition	6.8	0.05	0		24.0	N/A	0.5	10.8	5.8
8	4	8-4	Test condition	6.8	0.05	0	His-Enz	16.9	5.2	1.9	38.4	20.6
8	5	8-5	Test condition	6.8	0.05	0	Enz	15.0	N/A	0.6	12.2	6.5
9	1	9-1	Test condition	6.8	0.05	0.5		82.2	N/A	0.1	3.1	1.7
9	2	9-2	Test condition	6.8	0.05	0.5	TEV protease	29.0	3.9	1.6	34.4	19.0
9	3	9-3	Test condition	6.8	0.05	0.5		24.0	N/A	0.5	11.2	6.2
9	4	9-4	Test condition	6.8	0.05	0.5	His-Enz	16.9	5.2	1.9	40.6	22.4
9	5	9-5	Test condition	6.8	0.05	0.5	Enz	14.9	N/A	0.5	10.8	5.9
10	1	10-1	Test condition	6.8	0.1	1		81.9	N/A	0.2	4.5	2.5
10	2	10-2	Test condition	6.8	0.1	1	TEV protease	29.0	3.3	1.5	34.1	18.9
10	3	10-3	Test condition	6.8	0.1	1		24.0	N/A	0.5	10.6	5.9
10	4	10-4	Test condition	6.8	0.1	1	His-Enz	16.9	4.7	1.8	41.1	22.9
10	5	10-5	Test condition	6.8	0.1	1	Enz	15.0	N/A	0.4	9.7	5.4
11	1	11-1	Test condition	6.8	0.35	0.5		81.7	N/A	0.3	5.7	3.1
11	2	11-2	Test condition	6.8	0.35	0.5	TEV protease	29.2	3.7	1.5	33.1	18.1
11	3	11-3	Test condition	6.8	0.35	0.5		24.2	N/A	0.5	10.1	5.5
11	4	11-4	Test condition	6.8	0.35	0.5	His-Enz	17.0	5.3	1.9	40.1	21.9
11	5	11-5	Test condition	6.8	0.35	0.5	Enz	15.1	N/A	0.5	11.0	6.0
12	1	12-1	Molecular weight marker					180.0	3.2	1.4	7.5	6.8
12	2	12-2	Molecular weight marker				TEV protease	130.0	4.6	1.7	9.1	8.3
12	3	12-3	Molecular weight marker					100.0	11.4	3.2	16.7	15.1
12	4	12-4	Molecular weight marker				His-Enz	70.0	8.0	2.5	12.9	11.7
12	5	12-5	Molecular weight marker				Enz	55.0	8.0	2.7	14.0	12.7
12	6	12-6	Molecular weight marker				Molecular weight marker	40.0	4.6	1.7	9.0	8.2
12	7	12-7	Molecular weight marker				Molecular weight marker	35.0	5.6	1.9	10.2	9.2
12	8	12-8	Molecular weight marker				Molecular weight marker	25.0	3.0	1.4	7.3	6.6
12	9	12-9	Molecular weight marker				Molecular weight marker	15.0	5.5	1.9	10.0	9.1
12	10	12-10	Molecular weight marker				Molecular weight marker	10.0	N/A	0.6	3.3	3.0
13	1	13-1	Test condition	7.4	0.05	0		81.7	N/A	0.2	5.3	2.7
13	2	13-2	Test condition	7.4	0.05	0	TEV protease	29.1	1.7	1.1	38.7	19.9
13	3	13-3	Test condition	7.4	0.05	0		24.0	N/A	0.3	8.6	4.4
13	4	13-4	Test condition	7.4	0.05	0	His-Enz	17.0	1.6	1.1	38.0	19.5
13	5	13-5	Test condition	7.4	0.05	0	Enz	14.9	N/A	0.3	9.4	4.8
14	1	14-1	Test condition	7.4	0.05	0.5		83.4	N/A	0.2	4.7	2.7
14	2	14-2	Test condition	7.4	0.05	0.5	TEV protease	29.3	3.6	1.5	33.4	19.6
14	3	14-3	Test condition	7.4	0.05	0.5		24.2	N/A	0.4	9.4	5.5
14	4	14-4	Test condition	7.4	0.05	0.5	His-Enz	17.0	5.4	1.9	41.8	24.6
14	5	14-5	Test condition	7.4	0.05	0.5	Enz	15.0	N/A	0.5	10.8	6.3
15	1	15-1	Test condition	7.4	0.1	1		82.9	N/A	0.2	3.9	2.3
15	2	15-2	Test condition	7.4	0.1	1	TEV protease	29.0	4.0	1.6	34.3	20.3
15	3	15-3	Test condition	7.4	0.1	1		24.1	N/A	0.5	9.7	5.7
15	4	15-4	Test condition	7.4	0.1	1	His-Enz	17.0	5.9	2.0	42.5	25.1
15	5	15-5	Test condition	7.4	0.1	1	Enz	15.0	N/A	0.5	9.6	5.7
16	1	16-1	Test condition	7.4	0.35	0.5		81.8	N/A	0.3	5.5	2.9
16	2	16-2	Test condition	7.4	0.35	0.5	TEV protease	29.0	4.2	1.6	32.6	17.3
16	3	16-3	Test condition	7.4	0.35	0.5		24.1	N/A	0.5	9.2	4.9
16	4	16-4	Test condition	7.4	0.35	0.5	His-Enz	17.0	6.2	2.1	41.2	21.8
16	5	16-5	Test condition	7.4	0.35	0.5	Enz	15.0	N/A	0.6	11.4	6.0
17	1	17-1	Molecular weight marker					180.0	5.6	1.9	8.0	7.1
17	2	17-2	Molecular weight marker					130.0	6.7	2.2	9.0	8.0
17	3	17-3	Molecular weight marker					100.0	14.2	3.8	15.4	13.9
17	4	17-4	Molecular weight marker					70.0	10.7	3.0	12.5	11.2
17	5	17-5	Molecular weight marker					55.0	12.0	3.2	13.0	11.6
17	6	17-6	Molecular weight marker					40.0	6.6	2.2	8.9	7.9
17	7	17-7	Molecular weight marker					35.0	7.8	2.4	9.9	8.9
17	8	17-8	Molecular weight marker					25.0	4.8	1.8	7.3	6.6
17	9	17-9	Molecular weight marker					15.0	9.8	2.8	11.6	10.4
17	10	17-10	Molecular weight marker					10.0	1.5	1.1	4.4	3.9
18	1	18-1	Test condition	8	0.05	0		82.7	N/A	0.2	4.4	2.5
18	2	18-2	Test condition	8	0.05	0	TEV protease	29.1	2.6	1.3	38.2	21.5
18	3	18-3	Test condition	8	0.05	0		24.1	N/A	0.4	10.7	6.0
18	4	18-4	Test condition	8	0.05	0	His-Enz	17.0	2.4	1.3	37.3	21.0
18	5	18-5	Test condition	8	0.05	0	Enz	15.0	N/A	0.3	9.4	5.3
19	1	19-1	Test condition	8	0.05	0.5		85.0	N/A	0.2	4.6	2.6
19	2	19-2	Test condition	8	0.05	0.5	TEV protease	29.3	2.9	1.4	33.0	18.5
19	3	19-3	Test condition	8	0.05	0.5		24.2	N/A	0.4	9.4	5.3
19	4	19-4	Test condition	8	0.05	0.5	His-Enz	17.0	5.0	1.8	43.5	24.5
19	5	19-5	Test condition	8	0.05	0.5	Enz	15.0	N/A	0.4	9.6	5.4
20	1	20-1	Test condition	8	0.1	1		87.4	N/A	0.1	3.8	2.1
20	2	20-2	Test condition	8	0.1	1	TEV protease	29.8	2.3	1.2	33.8	19.3
20	3	20-3	Test condition	8	0.1	1		24.5	N/A	0.3	8.7	4.9
20	4	20-4	Test condition	8	0.1	1	His-Enz	17.3	4.3	1.7	45.4	25.9
20	5	20-5	Test condition	8	0.1	1	Enz	15.2	N/A	0.3	8.4	4.8
21	1	21-1	Test condition	8	0.35	0.5		89.9	N/A	0.3	4.9	2.9
21	2	21-2	Test condition	8	0.35	0.5	TEV protease	30.4	4.6	1.7	29.9	17.3
21	3	21-3	Test condition	8	0.35	0.5		25.0	N/A	0.6	10.2	5.9
21	4	21-4	Test condition	8	0.35	0.5	His-Enz	17.6	8.1	2.5	42.8	24.8
21	5	21-5	Test condition	8	0.35	0.5	Enz	15.5	N/A	0.7	12.1	7.1
22	1	22-1	Not treated His-Enz	-	-	-		93.7	N/A	0.1	3.7	2.1
22	2	22-2	Not treated His-Enz	-	-	-	TEV protease	31.5	1.2	1.0	29.5	16.2
22	3	22-3	Not treated His-Enz	-	-	-		25.8	N/A	0.3	8.2	4.5
22	4	22-4	Not treated His-Enz	-	-	-	His-Enz	18.0	4.4	1.7	49.7	27.2
22	5	22-5	Not treated His-Enz	-	-	-	Enz	15.9	N/A	0.3	8.8	4.8
"""

# Use StringIO to read the string data into a pandas DataFrame
# The data is tab-separated, so we use sep='\t'
df = pd.read_csv(io.StringIO(data), sep='\t', skipinitialspace=True)

# --- Data Cleaning and Filtering ---

# We only care about the cleaved product, which is 'Enz'.
# Let's filter the DataFrame to only include rows where the 'Protein' is 'Enz'.
# We also want to exclude the control lanes ('Not treated His-Enz').
df_cleaved = df[(df['Protein'].str.strip() == 'Enz') & (df['Condition'] == 'Test condition')].copy()

# Convert relevant columns to numeric types. 'coerce' will turn non-numeric values into NaN.
for col in ['pH', 'Salt', 'Urea', 'Lane %']:
    df_cleaved[col] = pd.to_numeric(df_cleaved[col], errors='coerce')

# Drop any rows that might have missing values after conversion
df_cleaved.dropna(subset=['pH', 'Salt', 'Urea', 'Lane %'], inplace=True)


# --- 2. Plotting ---

# Set a general style for the plots
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100

# --- Plot 1: 4D Bubble Chart (pH vs. Salt vs. Urea vs. Cleavage %) ---
print("Generating Plot 1: 4D Bubble Chart...")
fig1, ax1 = plt.subplots(figsize=(12, 8))
scatter = ax1.scatter(
    x='pH',
    y='Salt',
    s=df_cleaved['Urea'] * 200 + 50,  # Scale Urea for better visibility (add constant to see 0M)
    c='Lane %',
    data=df_cleaved,
    cmap='viridis', # A color map where yellow is high, purple is low
    alpha=0.7,
    edgecolors='k',
    linewidth=0.5
)
# Add a colorbar for the 'Lane %'
cbar = fig1.colorbar(scatter)
cbar.set_label('Cleavage Efficiency (Lane %)', rotation=270, labelpad=20)
# Create a legend for marker size (Urea concentration)
for urea_val in sorted(df_cleaved['Urea'].unique()):
    ax1.scatter([], [], s=urea_val * 200 + 50, c='gray', alpha=0.7, label=f'{urea_val} M')
ax1.legend(scatterpoints=1, frameon=True, title='Urea Conc.', loc='upper right')

ax1.set_xlabel("pH")
ax1.set_ylabel("Salt Concentration (M NaCl)")
ax1.set_title("Cleavage Efficiency as a Function of pH, Salt, and Urea", pad=20)
plt.tight_layout()
plt.show()


# --- Plot 2: Scatter Plots for Individual Factors ---
print("Generating Plot 2: Individual Factor Scatter Plots...")
fig2, (ax2, ax3, ax4) = plt.subplots(1, 3, figsize=(20, 6))
# Plot 2a: Efficiency vs. pH
sns.scatterplot(data=df_cleaved, x='pH', y='Lane %', hue='Salt', size='Urea', ax=ax2, palette='plasma', ec='k')
ax2.set_title('Efficiency vs. pH')
# Plot 2b: Efficiency vs. Salt
sns.scatterplot(data=df_cleaved, x='Salt', y='Lane %', hue='pH', size='Urea', ax=ax3, palette='cividis', ec='k')
ax3.set_title('Efficiency vs. Salt')
# Plot 2c: Efficiency vs. Urea
sns.scatterplot(data=df_cleaved, x='Urea', y='Lane %', hue='pH', size='Salt', ax=ax4, palette='inferno', ec='k')
ax4.set_title('Efficiency vs. Urea')
fig2.suptitle('Cleavage Efficiency vs. Individual Conditions', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
plt.show()


# --- Plot 3: Box Plots to Show Distribution ---
print("Generating Plot 3: Box Plots...")
fig3, (ax5, ax6) = plt.subplots(1, 2, figsize=(14, 6))
# Plot 3a: Box plot for pH
sns.boxplot(data=df_cleaved, x='pH', y='Lane %', ax=ax5)
sns.stripplot(data=df_cleaved, x='pH', y='Lane %', ax=ax5, color='0.25')
ax5.set_title('Cleavage Efficiency Distribution by pH')
# Plot 3b: Box plot for Salt
sns.boxplot(data=df_cleaved, x='Salt', y='Lane %', ax=ax6)
sns.stripplot(data=df_cleaved, x='Salt', y='Lane %', ax=ax6, color='0.25')
ax6.set_title('Cleavage Efficiency Distribution by Salt Conc.')
fig3.suptitle('Distribution of Cleavage Efficiency', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# --- Plot 4: Heatmap of pH vs. Salt ---
print("Generating Plot 4: Heatmap...")
# We can create a pivot table. Since Urea is another variable, we will average the
# efficiency for conditions with the same pH and Salt but different Urea.
heatmap_data = df_cleaved.pivot_table(values='Lane %', index='pH', columns='Salt', aggfunc=np.mean)

fig4, ax7 = plt.subplots(figsize=(10, 7))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=.5, ax=ax7)
ax7.set_title('Average Cleavage Efficiency (%) by pH and Salt Concentration')
plt.show()

print("\nAll plots generated.")

# ...existing code...

# --- Data Export ---
output_file = "cleaved_data_export.csv"
df_cleaved.to_csv(output_file, index=False)

print(f"Data exported to {output_file}")

# --- Export Plots --- Update the folder for where images are saved
exported_images_folder = r"C:\Users\Documents"
import os
if not os.path.exists(exported_images_folder):
    os.makedirs(exported_images_folder)

save_plots = input("Do you want to save the plot images as .jpg files? (y/n): ").strip().lower()
if save_plots == 'y':
    fig1.savefig(os.path.join(exported_images_folder, "Figure_1.jpg"), format='jpg')
    fig2.savefig(os.path.join(exported_images_folder, "Figure_2.jpg"), format='jpg')
    fig3.savefig(os.path.join(exported_images_folder, "Figure_3.jpg"), format='jpg')
    fig4.savefig(os.path.join(exported_images_folder, "Figure_4.jpg"), format='jpg')
    print(f"Plots saved in folder: {exported_images_folder}")