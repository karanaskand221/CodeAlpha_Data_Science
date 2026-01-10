import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fix matplotlib for codespace
plt.style.use('default')
sns.set_palette("husl")

print("🚀 OIBSIP Task 2 Starting...")

# 1. LOAD DATA
print("\n📁 Loading Unemployment-in-India.csv...")
df = pd.read_csv('CodeAlphaUnemploymentAnalysis/Unemployment-in-India.csv')

# --- FIX: STRIP WHITESPACE FROM COLUMN NAMES ---
df.columns = df.columns.str.strip()
# -----------------------------------------------

print(f"Cleaned columns: {df.columns.tolist()}")
print(f"Number of columns: {len(df.columns)}")
print(f"✅ Loaded {df.shape[0]} rows, {df.shape[1]} columns")

# 2. CLEAN DATA
print("\n🧹 Cleaning data...")

# We map the long column names to the short names used in your logic
# This ensures df['Unemp_Rate'] and df['Employed'] work correctly
column_mapping = {
    'Estimated Unemployment Rate (%)': 'Unemp_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Participation_Rate'
}
df.rename(columns=column_mapping, inplace=True)

# Convert Date and handle numeric conversion
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Unemp_Rate'] = pd.to_numeric(df['Unemp_Rate'], errors='coerce')
df['Employed'] = pd.to_numeric(df['Employed'], errors='coerce')

# Drop empty rows (important for this dataset as it contains blank separator rows)
df.dropna(inplace=True)

print(f"✅ Clean data: {df.shape[0]} rows")

# 3. COVID ANALYSIS
print("\n🦠 COVID-19 Impact Analysis...")
pre_covid = df[df['Date'].dt.year == 2019]['Unemp_Rate'].mean()
covid_peak = df[df['Date'].dt.year == 2020]['Unemp_Rate'].mean()
surge = ((covid_peak / pre_covid) - 1) * 100

print(f"📊 Pre-COVID (2019): {pre_covid:.2f}%")
print(f"📊 COVID Peak (2020): {covid_peak:.2f}%") 
print(f"🔥 SURGE: +{surge:.1f}%")

# 4. TOP STATES
print("\n🏆 Top 5 Worst Hit States:")
top_states = df.groupby('Region')['Unemp_Rate'].mean().sort_values(ascending=False).head()
print(top_states.round(2))

# 5. PLOTS
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Unemployment by State
top_states.plot(kind='bar', ax=axes[0,0], color='red', alpha=0.7)
axes[0,0].set_title('Top 5 States by Unemployment Rate')
axes[0,0].tick_params(axis='x', rotation=45)

# Plot 2: Time Trend
# We use .to_timestamp() because matplotlib handles timestamps better than Period objects
monthly_avg = df.groupby(df['Date'].dt.to_period('M'))['Unemp_Rate'].mean()
monthly_avg.index = monthly_avg.index.to_timestamp()
axes[0,1].plot(monthly_avg.index, monthly_avg.values, marker='o', linewidth=3)
axes[0,1].set_title('Monthly Unemployment Trend')
axes[0,1].tick_params(axis='x', rotation=45)

# Plot 3: Rural vs Urban
area_avg = df.groupby('Area')['Unemp_Rate'].mean()
area_avg.plot(kind='bar', ax=axes[1,0], color=['green', 'orange'])
axes[1,0].set_title('Rural vs Urban Unemployment')

# Plot 4: COVID Surge
categories = ['Pre-COVID (2019)', 'COVID Peak (2020)']
values = [pre_covid, covid_peak]
axes[1,1].bar(categories, values, color=['blue', 'red'], alpha=0.7)
axes[1,1].set_title('COVID-19 Impact')
for i, v in enumerate(values):
    axes[1,1].text(i, v + 0.5, f'{v:.1f}%', ha='center')

plt.tight_layout()
plt.savefig('unemployment_analysis.png', dpi=300, bbox_inches='tight')
print("\n✅ PLOTS GENERATED: unemployment_analysis.png")

# 6. POLICY INSIGHTS
print("\n" + "="*60)
print("🎯 POLICY RECOMMENDATIONS")
print("="*60)
print("1. 🚨 IMMEDIATE: MSME relief in high unemployment regions")
print("2. 📚 SKILLS: Rural youth training programs") 
print("3. 💼 JOBS: Urban employment guarantee scheme")
print("4. 📈 MONITOR: Monthly labour force surveys")
print("\n✅ ANALYSIS COMPLETE!")
print("="*60)