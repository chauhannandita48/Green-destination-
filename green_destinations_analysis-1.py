# ============================================================
#   GREEN DESTINATIONS – HR ATTRITION ANALYSIS
#   Internship Project | Unified Mentor
# ============================================================

# ── STEP 1: Install dependencies (run once in terminal) ──────
# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Styling ──────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
COLORS = {"Yes": "#E74C3C", "No": "#2ECC71"}
plt.rcParams['figure.dpi'] = 120


# ============================================================
# STEP 2: LOAD DATA
# ============================================================
df = pd.read_csv('greendestination.csv')

print("=" * 55)
print("  GREEN DESTINATIONS – ATTRITION ANALYSIS")
print("=" * 55)
print(f"\nDataset Shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Columns       : {list(df.columns)}\n")


# ============================================================
# STEP 3: ATTRITION RATE  (Primary KPI)
# ============================================================
attrition_counts = df['Attrition'].value_counts()
total_employees  = len(df)
left_employees   = attrition_counts.get('Yes', 0)
attrition_rate   = (left_employees / total_employees) * 100

print("─" * 55)
print("  ATTRITION RATE")
print("─" * 55)
print(f"  Total Employees   : {total_employees}")
print(f"  Employees Left    : {left_employees}")
print(f"  Still Employed    : {attrition_counts.get('No', 0)}")
print(f"  Attrition Rate    : {attrition_rate:.2f}%")
print("─" * 55)


# ============================================================
# STEP 4: FACTOR ANALYSIS  (Age, Income, Years at Company)
# ============================================================
factors = {
    'Age'           : 'Age',
    'MonthlyIncome' : 'Monthly Income ($)',
    'YearsAtCompany': 'Years at Company'
}

print("\n  FACTOR COMPARISON (Left vs Stayed)\n")
print(f"  {'Factor':<22} {'Left (Yes)':>12} {'Stayed (No)':>12}")
print("  " + "-" * 48)
for col, label in factors.items():
    yes_mean = df[df['Attrition'] == 'Yes'][col].mean()
    no_mean  = df[df['Attrition'] == 'No'][col].mean()
    print(f"  {label:<22} {yes_mean:>12.1f} {no_mean:>12.1f}")
print()


# ============================================================
# STEP 5: VISUALISATIONS
# ============================================================

fig = plt.figure(figsize=(18, 20))
fig.suptitle('Green Destinations – HR Attrition Dashboard',
             fontsize=20, fontweight='bold', y=0.98, color='#2C3E50')


# ── Plot 1: Attrition Rate – Donut Chart ─────────────────────
ax1 = fig.add_subplot(3, 3, 1)
wedge_colors = [COLORS['Yes'], COLORS['No']]
wedges, texts, autotexts = ax1.pie(
    attrition_counts,
    labels=attrition_counts.index,
    autopct='%1.1f%%',
    colors=wedge_colors,
    startangle=90,
    wedgeprops=dict(width=0.55, edgecolor='white', linewidth=2),
    textprops={'fontsize': 11}
)
for at in autotexts:
    at.set_fontweight('bold')
    at.set_fontsize(12)
ax1.set_title('Attrition Rate', fontweight='bold', fontsize=13, pad=12)
ax1.text(0, 0, f'{attrition_rate:.1f}%\nAttrition',
         ha='center', va='center', fontsize=11, fontweight='bold', color='#E74C3C')


# ── Plot 2: Attrition Count – Bar Chart ──────────────────────
ax2 = fig.add_subplot(3, 3, 2)
bars = ax2.bar(attrition_counts.index,
               attrition_counts.values,
               color=[COLORS[k] for k in attrition_counts.index],
               edgecolor='white', linewidth=1.5, width=0.5)
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 10,
             str(int(bar.get_height())),
             ha='center', fontweight='bold', fontsize=12)
ax2.set_title('Attrition Count', fontweight='bold', fontsize=13)
ax2.set_xlabel('Attrition', fontsize=11)
ax2.set_ylabel('Number of Employees', fontsize=11)
ax2.set_ylim(0, attrition_counts.max() * 1.15)


# ── Plot 3: Age Distribution ──────────────────────────────────
ax3 = fig.add_subplot(3, 3, 3)
for val, color in COLORS.items():
    subset = df[df['Attrition'] == val]['Age']
    ax3.hist(subset, bins=15, alpha=0.7, color=color, edgecolor='white', linewidth=0.8, label=val)
ax3.set_title('Age Distribution by Attrition', fontweight='bold', fontsize=13)
ax3.set_xlabel('Age', fontsize=11)
ax3.set_ylabel('Count', fontsize=11)
patches = [mpatches.Patch(color=COLORS[k], label=k) for k in COLORS]
ax3.legend(handles=patches, title='Attrition')


# ── Plot 4: Age vs Attrition – Boxplot ───────────────────────
ax4 = fig.add_subplot(3, 3, 4)
df.boxplot(column='Age', by='Attrition', ax=ax4,
           patch_artist=True,
           boxprops=dict(facecolor='#AED6F1'),
           medianprops=dict(color='#E74C3C', linewidth=2))
ax4.set_title('Age vs Attrition', fontweight='bold', fontsize=13)
ax4.set_xlabel('Attrition', fontsize=11)
ax4.set_ylabel('Age', fontsize=11)
plt.sca(ax4)
plt.title('')


# ── Plot 5: Monthly Income vs Attrition – Boxplot ────────────
ax5 = fig.add_subplot(3, 3, 5)
df.boxplot(column='MonthlyIncome', by='Attrition', ax=ax5,
           patch_artist=True,
           boxprops=dict(facecolor='#A9DFBF'),
           medianprops=dict(color='#E74C3C', linewidth=2))
ax5.set_title('Monthly Income vs Attrition', fontweight='bold', fontsize=13)
ax5.set_xlabel('Attrition', fontsize=11)
ax5.set_ylabel('Monthly Income ($)', fontsize=11)
plt.sca(ax5)
plt.title('')


# ── Plot 6: Years at Company vs Attrition – Boxplot ──────────
ax6 = fig.add_subplot(3, 3, 6)
df.boxplot(column='YearsAtCompany', by='Attrition', ax=ax6,
           patch_artist=True,
           boxprops=dict(facecolor='#F9E79F'),
           medianprops=dict(color='#E74C3C', linewidth=2))
ax6.set_title('Years at Company vs Attrition', fontweight='bold', fontsize=13)
ax6.set_xlabel('Attrition', fontsize=11)
ax6.set_ylabel('Years at Company', fontsize=11)
plt.sca(ax6)
plt.title('')


# ── Plot 7: Attrition by Department ──────────────────────────
ax7 = fig.add_subplot(3, 3, 7)
dept_attr = df.groupby(['Department', 'Attrition']).size().unstack(fill_value=0)
dept_attr_pct = dept_attr.div(dept_attr.sum(axis=1), axis=0) * 100
dept_attr_pct.plot(kind='bar', ax=ax7,
                   color=[COLORS['No'], COLORS['Yes']],
                   edgecolor='white', linewidth=0.8)
ax7.set_title('Attrition Rate by Department', fontweight='bold', fontsize=13)
ax7.set_xlabel('Department', fontsize=11)
ax7.set_ylabel('Percentage (%)', fontsize=11)
ax7.legend(title='Attrition', labels=['No', 'Yes'])
ax7.tick_params(axis='x', rotation=15)


# ── Plot 8: Attrition by Gender ───────────────────────────────
ax8 = fig.add_subplot(3, 3, 8)
gender_attr = df.groupby(['Gender', 'Attrition']).size().unstack(fill_value=0)
gender_attr_pct = gender_attr.div(gender_attr.sum(axis=1), axis=0) * 100
gender_attr_pct.plot(kind='bar', ax=ax8,
                     color=[COLORS['No'], COLORS['Yes']],
                     edgecolor='white', linewidth=0.8)
ax8.set_title('Attrition Rate by Gender', fontweight='bold', fontsize=13)
ax8.set_xlabel('Gender', fontsize=11)
ax8.set_ylabel('Percentage (%)', fontsize=11)
ax8.legend(title='Attrition', labels=['No', 'Yes'])
ax8.tick_params(axis='x', rotation=0)


# ── Plot 9: Attrition by Overtime ────────────────────────────
ax9 = fig.add_subplot(3, 3, 9)
ot_attr = df.groupby(['OverTime', 'Attrition']).size().unstack(fill_value=0)
ot_attr_pct = ot_attr.div(ot_attr.sum(axis=1), axis=0) * 100
ot_attr_pct.plot(kind='bar', ax=ax9,
                 color=[COLORS['No'], COLORS['Yes']],
                 edgecolor='white', linewidth=0.8)
ax9.set_title('Attrition Rate by Overtime', fontweight='bold', fontsize=13)
ax9.set_xlabel('OverTime', fontsize=11)
ax9.set_ylabel('Percentage (%)', fontsize=11)
ax9.legend(title='Attrition', labels=['No', 'Yes'])
ax9.tick_params(axis='x', rotation=0)


plt.suptitle('')  # Remove auto-generated suptitle from boxplots
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('green_destinations_dashboard.png', bbox_inches='tight', dpi=150)
plt.show()
print("\n✅ Dashboard saved as 'green_destinations_dashboard.png'")


# ============================================================
# STEP 6: SUMMARY INSIGHTS
# ============================================================
print("\n" + "=" * 55)
print("  KEY FINDINGS SUMMARY")
print("=" * 55)

age_yes = df[df['Attrition'] == 'Yes']['Age'].mean()
age_no  = df[df['Attrition'] == 'No']['Age'].mean()
inc_yes = df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean()
inc_no  = df[df['Attrition'] == 'No']['MonthlyIncome'].mean()
yrs_yes = df[df['Attrition'] == 'Yes']['YearsAtCompany'].mean()
yrs_no  = df[df['Attrition'] == 'No']['YearsAtCompany'].mean()

print(f"""
  1. ATTRITION RATE
     → {attrition_rate:.2f}% of employees have left the company.

  2. AGE
     → Employees who left are younger on average
       (Left: {age_yes:.1f} yrs  |  Stayed: {age_no:.1f} yrs)
     → Younger employees are more likely to leave.

  3. MONTHLY INCOME
     → Employees who left earned less on average
       (Left: ${inc_yes:,.0f}  |  Stayed: ${inc_no:,.0f})
     → Lower income is a strong predictor of attrition.

  4. YEARS AT COMPANY
     → Employees who left had fewer years at the company
       (Left: {yrs_yes:.1f} yrs  |  Stayed: {yrs_no:.1f} yrs)
     → Early-tenure employees are at higher attrition risk.
""")
print("=" * 55)
print("  Analysis Complete!")
print("=" * 55)
