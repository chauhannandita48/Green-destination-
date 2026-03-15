# ============================================================
#   TABLEAU DASHBOARD GUIDE – GREEN DESTINATIONS
#   Step-by-Step Instructions
# ============================================================


# ──────────────────────────────────────────────────────────────
# CALCULATED FIELDS  (create these first in Tableau)
# ──────────────────────────────────────────────────────────────

# 1. Attrition Rate (%)
#    Name: "Attrition Rate"
#    Formula:
SUM(IF [Attrition] = "Yes" THEN 1 ELSE 0 END) / COUNT([Employee Number])

# 2. Attrition Flag (numeric)
#    Name: "Attrition Flag"
#    Formula:
IF [Attrition] = "Yes" THEN 1 ELSE 0 END

# 3. Age Group (bins)
#    Name: "Age Group"
#    Formula:
IF [Age] < 25 THEN "Under 25"
ELSEIF [Age] < 35 THEN "25-34"
ELSEIF [Age] < 45 THEN "35-44"
ELSEIF [Age] < 55 THEN "45-54"
ELSE "55+"
END

# 4. Income Band
#    Name: "Income Band"
#    Formula:
IF [Monthly Income] < 3000 THEN "Low (<3k)"
ELSEIF [Monthly Income] < 7000 THEN "Mid (3k-7k)"
ELSE "High (>7k)"
END

# 5. Tenure Group
#    Name: "Tenure Group"
#    Formula:
IF [Years At Company] <= 2 THEN "0-2 Years"
ELSEIF [Years At Company] <= 5 THEN "3-5 Years"
ELSEIF [Years At Company] <= 10 THEN "6-10 Years"
ELSE "10+ Years"
END


# ──────────────────────────────────────────────────────────────
# SHEETS TO CREATE
# ──────────────────────────────────────────────────────────────

# SHEET 1 – KPI: Attrition Rate
# ─────────────────────────────
# • Drag [Attrition Rate] to the Text shelf (Marks card → Text)
# • Change Mark type to "Text"
# • Format: Percentage, 2 decimal places
# • Add a reference label: "of employees left"
# • Title: "Attrition Rate"
# • Color the number RED (#E74C3C)


# SHEET 2 – KPI: Total Employees Left
# ─────────────────────────────────────
# • Drag COUNT([Employee Number]) → Text
# • Filter: Attrition = "Yes"
# • Title: "Employees Left"


# SHEET 3 – Attrition by Department (Bar Chart)
# ──────────────────────────────────────────────
# Rows:    Department
# Columns: [Attrition Rate]   (the calculated field)
# Color:   Attrition (Yes=Red, No=Green)
# Mark type: Bar
# Sort: Descending by Attrition Rate
# Label: Show mark labels
# Title: "Attrition Rate by Department"


# SHEET 4 – Attrition by Age Group (Bar Chart)
# ─────────────────────────────────────────────
# Rows:    Age Group
# Columns: [Attrition Rate]
# Color:   Red gradient (higher rate = darker red)
# Mark type: Bar
# Title: "Attrition by Age Group"
# Sort Age Group: Under 25, 25-34, 35-44, 45-54, 55+


# SHEET 5 – Attrition by Monthly Income (Bar Chart)
# ──────────────────────────────────────────────────
# Rows:    Income Band
# Columns: [Attrition Rate]
# Color:   Attrition Rate (sequential color)
# Mark type: Bar
# Title: "Attrition by Income Band"


# SHEET 6 – Attrition by Years at Company (Line Chart)
# ──────────────────────────────────────────────────────
# Columns: Years At Company
# Rows:    [Attrition Rate]
# Mark type: Line + Circle
# Color:   #E74C3C
# Title: "Attrition Trend by Tenure"
# Tip: Limit X-axis to 0–20 years for cleaner view


# SHEET 7 – Attrition by Gender (Side-by-side Bar)
# ──────────────────────────────────────────────────
# Rows:    Gender
# Columns: [Attrition Rate]
# Color:   Attrition
# Mark type: Bar
# Title: "Attrition by Gender"


# SHEET 8 – Attrition by OverTime (Bar Chart)
# ─────────────────────────────────────────────
# Rows:    Over Time
# Columns: [Attrition Rate]
# Color:   Attrition Rate (diverging Red-Green)
# Title: "Impact of Overtime on Attrition"


# SHEET 9 – Attrition by Job Role (Heatmap)
# ──────────────────────────────────────────
# Rows:    Job Role
# Columns: Department
# Color:   [Attrition Rate]   (Red = high)
# Mark type: Square
# Label:   [Attrition Rate] formatted as %
# Title: "Attrition Heatmap by Role & Department"


# ──────────────────────────────────────────────────────────────
# DASHBOARD LAYOUT GUIDE
# ──────────────────────────────────────────────────────────────
#
# Dashboard Size: 1200 x 850 px  (Fixed)
#
# ┌─────────────────────────────────────────────────────────┐
# │  🟢 GREEN DESTINATIONS – HR ATTRITION DASHBOARD        │
# ├──────────────┬──────────────┬───────────────────────────┤
# │  KPI:        │  KPI:        │  KPI:                     │
# │  Attrition   │  Employees   │  Total Employees          │
# │  Rate 16.1%  │  Left: 237   │  1470                     │
# ├──────────────┴──────────────┴───────────────────────────┤
# │  Attrition by Department   │  Attrition by Age Group   │
# │  (Bar Chart)               │  (Bar Chart)              │
# ├────────────────────────────┼───────────────────────────┤
# │  Attrition by Income Band  │  Attrition Trend: Tenure  │
# │  (Bar Chart)               │  (Line Chart)             │
# ├────────────────────────────┼───────────────────────────┤
# │  By Gender  │  By Overtime │  Heatmap: Role & Dept     │
# └─────────────┴──────────────┴───────────────────────────┘
#
# FILTERS TO ADD (drag to Dashboard as Quick Filters):
#   • Department
#   • Gender
#   • Age Group
#   • OverTime


# ──────────────────────────────────────────────────────────────
# COLOR SCHEME
# ──────────────────────────────────────────────────────────────
# Attrition = "Yes"  →  #E74C3C  (Red)
# Attrition = "No"   →  #2ECC71  (Green)
# Background         →  #F8F9FA  (Light grey)
# Title bar          →  #2C3E50  (Dark navy)
# Accent             →  #3498DB  (Blue for KPI boxes)


# ──────────────────────────────────────────────────────────────
# QUICK STEPS TO CONNECT DATA IN TABLEAU
# ──────────────────────────────────────────────────────────────
# 1. Open Tableau Desktop / Tableau Public
# 2. Connect → Text File → select "greendestination.csv"
# 3. Check preview – 1470 rows, 35 columns
# 4. Go to Sheet 1
# 5. Create all Calculated Fields first (Analysis → Create Calculated Field)
# 6. Build each sheet one by one (listed above)
# 7. New Dashboard → drag sheets in
# 8. Add Filters, Titles, and Color formatting
# 9. Save as .twbx (Packaged Workbook) to submit
