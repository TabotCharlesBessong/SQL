"""
DSC602 Information Visualization - June 2025 Exam
Question 3: Data Visualization Graphics and Characteristics
Practical Implementation of 6 Graph Types

University of Buea | Faculty of Science
Date: Saturday 28/06/2025
Instructor: Dr. Nyamsi
Question 3 Marks: 25 (4 marks per graph + 1 bonus)

This script implements all 6 graph types with theoretical explanations
and practical business examples.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configure plotting
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.size'] = 10

# ============================================================================
# GRAPH 1: LINE GRAPH
# ============================================================================

def graph_1_line_graph():
    """
    LINE GRAPH - Temporal Trends
    
    Definition: Connects data points with lines, showing values on y-axis 
    against time/sequence on x-axis.
    
    Best Use Contexts:
    1. Temporal Trends: Stock prices, website traffic, health metrics
    2. Multiple Series Comparison: Revenue vs. Expenses, different products
    
    Why Useful:
    - Pattern recognition (trends instantly visible)
    - Seasonality detection
    - Anomaly visibility
    - Prediction capability
    - Multiple series comparison
    - Intuitive for general audiences
    """
    
    print("\n" + "="*80)
    print("GRAPH 1: LINE GRAPH - Stock Price Trends")
    print("="*80)
    print(__doc__)
    
    # Create sample data
    dates = pd.date_range('2025-01-01', periods=100, freq='D')
    apple = 150 + np.cumsum(np.random.randn(100) * 2)
    google = 140 + np.cumsum(np.random.randn(100) * 1.5)
    microsoft = 160 + np.cumsum(np.random.randn(100) * 2.5)
    
    stock_data = pd.DataFrame({
        'Date': dates,
        'Apple': apple,
        'Google': google,
        'Microsoft': microsoft
    })
    
    # Create plot
    fig, ax = plt.subplots(figsize=(14, 7))
    
    ax.plot(stock_data['Date'], stock_data['Apple'], label='Apple', 
            linewidth=2, color='#A2AAAD', marker='o', markersize=3)
    ax.plot(stock_data['Date'], stock_data['Google'], label='Google',
            linewidth=2, color='#4285F4', marker='s', markersize=3)
    ax.plot(stock_data['Date'], stock_data['Microsoft'], label='Microsoft',
            linewidth=2, color='#00A4EF', marker='^', markersize=3)
    
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax.set_title('Stock Price Trends - LINE GRAPH (4 marks)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3)
    
    import matplotlib.dates as mdates
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    print(f"\nData Summary: {len(stock_data)} days of trading data")
    print(f"Context: TEMPORAL TRENDS - Instantly see performance comparison")

# ============================================================================
# GRAPH 2: BAR CHART
# ============================================================================

def graph_2_bar_chart():
    """
    BAR CHART - Category Comparison
    
    Definition: Displays categorical data as rectangular bars with 
    heights proportional to values.
    
    Best Use Contexts:
    1. Categorical Comparison: Sales by region, market share
    2. Part-to-Whole (Stacked): Revenue breakdown by division
    
    Why Useful:
    - Precise magnitude comparison
    - Simplicity
    - Multiple categories
    - Composition analysis (stacked)
    - Value labels possible
    """
    
    print("\n" + "="*80)
    print("GRAPH 2: BAR CHART - Sales by Region")
    print("="*80)
    print(__doc__)
    
    # Data
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East']
    sales = [450000, 380000, 520000, 250000, 180000]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F7B731', '#5F27CD']
    
    fig, ax = plt.subplots(figsize=(14, 7))
    bars = ax.bar(regions, sales, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Add labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'${height:,.0f}',
               ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax.set_ylabel('Sales ($)', fontsize=12, fontweight='bold')
    ax.set_title('Sales Revenue by Region - BAR CHART (4 marks)', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(sales) * 1.15)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    print(f"\nContext: CATEGORICAL COMPARISON")
    print(f"Highest: {regions[np.argmax(sales)]} (${max(sales):,.0f})")
    print(f"Lowest: {regions[np.argmin(sales)]} (${min(sales):,.0f})")

# ============================================================================
# GRAPH 3: HISTOGRAM
# ============================================================================

def graph_3_histogram():
    """
    HISTOGRAM - Distribution Analysis
    
    Definition: Shows distribution of continuous data using adjacent bins,
    where height represents frequency.
    
    Best Use Contexts:
    1. Distribution Analysis: Age, income, test scores
    2. Outlier Detection: Quality control, anomalies
    
    Why Useful:
    - Distribution shape visible
    - Central tendency
    - Spread/variability
    - Outlier identification
    - Data quality insights
    """
    
    print("\n" + "="*80)
    print("GRAPH 3: HISTOGRAM - Customer Age Distribution")
    print("="*80)
    print(__doc__)
    
    # Generate data
    np.random.seed(42)
    ages = np.random.normal(loc=45, scale=15, size=1000)
    ages = np.clip(ages, 18, 85)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Left: Standard histogram
    n, bins, patches = axes[0].hist(ages, bins=25, color='#4ECDC4', 
                                    edgecolor='black', alpha=0.7)
    
    for i, patch in enumerate(patches):
        if bins[i] < 25 or bins[i] > 75:
            patch.set_facecolor('#FF6B6B')
    
    axes[0].axvline(np.mean(ages), color='red', linestyle='--', linewidth=2,
                    label=f'Mean: {np.mean(ages):.1f}')
    axes[0].axvline(np.median(ages), color='green', linestyle='--', linewidth=2,
                    label=f'Median: {np.median(ages):.1f}')
    axes[0].set_xlabel('Age (years)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Frequency', fontsize=12, fontweight='bold')
    axes[0].set_title('Age Distribution - HISTOGRAM (4 marks)', fontsize=14, fontweight='bold')
    axes[0].legend(fontsize=11)
    axes[0].grid(True, alpha=0.3, axis='y')
    
    # Right: Cumulative
    axes[1].hist(ages, bins=25, cumulative=True, color='#45B7D1',
                edgecolor='black', alpha=0.7)
    axes[1].set_xlabel('Age (years)', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Cumulative Frequency', fontsize=12, fontweight='bold')
    axes[1].set_title('Cumulative Distribution', fontsize=14, fontweight='bold')
    axes[1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nContext: DISTRIBUTION ANALYSIS")
    print(f"Mean: {np.mean(ages):.2f}, Median: {np.median(ages):.2f}")
    print(f"Std Dev: {np.std(ages):.2f}, Range: {np.min(ages):.0f}-{np.max(ages):.0f}")

# ============================================================================
# GRAPH 4: FLOW CHART
# ============================================================================

def graph_4_flow_chart():
    """
    FLOW CHART - Process Documentation
    
    Definition: Diagram showing processes, decision points, and data flow
    using connected boxes, diamonds, and arrows.
    
    Best Use Contexts:
    1. Process Documentation: Workflows, procedures
    2. Decision Trees: Medical diagnosis, troubleshooting
    
    Why Useful:
    - Sequential steps clear
    - Branching logic visible
    - Non-technical understanding
    - Bottleneck identification
    - Training tool
    """
    
    print("\n" + "="*80)
    print("GRAPH 4: FLOW CHART - Customer Service Process")
    print("="*80)
    print(__doc__)
    
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    def add_box(x, y, width, height, text, color='lightblue'):
        box = FancyBboxPatch((x-width/2, y-height/2), width, height,
                            boxstyle="round,pad=0.1",
                            edgecolor='black', facecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', 
               fontsize=10, fontweight='bold', wrap=True)
    
    def add_arrow(x1, y1, x2, y2, label=''):
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                              arrowstyle='->', mutation_scale=20,
                              linewidth=2, color='black')
        ax.add_patch(arrow)
        if label:
            ax.text((x1+x2)/2+0.3, (y1+y2)/2, label,
                   fontsize=9, fontweight='bold', color='red')
    
    # Build flow
    add_box(5, 11, 2, 0.8, 'START', 'lightgreen')\n    add_arrow(5, 10.6, 5, 10)\n    add_box(5, 9.5, 2.5, 0.8, 'Receive\\nCall', 'lightblue')\n    add_arrow(5, 9.1, 5, 8.5)\n    add_box(5, 8, 2, 1, 'Issue?', 'lightyellow')\n    \n    add_arrow(4, 7.5, 2, 7, 'Billing')\n    add_arrow(5, 7.5, 5, 7, 'Tech')\n    add_arrow(6, 7.5, 8, 7, 'Product')\n    \n    add_box(2, 6.5, 1.8, 0.7, 'Check\\nAccount', 'lightcyan')\n    add_box(5, 6.5, 2, 0.7, 'Run\\nDiagnostics', 'lightyellow')\n    add_box(8, 6.5, 1.8, 0.7, 'Check\\nInventory', 'lightpink')\n    \n    add_arrow(2, 6.15, 2, 5.6)\n    add_arrow(5, 6.15, 5, 5.6)\n    add_arrow(8, 6.15, 8, 5.6)\n    \n    add_box(2, 5.2, 2, 0.8, 'Resolve', 'lightcyan')\n    add_box(5, 5.2, 2, 0.8, 'Fix', 'lightyellow')\n    add_box(8, 5.2, 2, 0.8, 'Process\\nOrder', 'lightpink')\n    \n    add_arrow(2, 4.8, 5, 4)\n    add_arrow(8, 4.8, 5, 4)\n    \n    add_box(5, 2.7, 2.5, 0.8, 'Document', 'lightcyan')\n    add_arrow(5, 2.3, 5, 1.7)\n    add_box(5, 1.2, 2, 0.8, 'END', 'lightcoral')\n    \n    ax.set_title('Process Flow - FLOW CHART (4 marks)', fontsize=14, fontweight='bold', pad=20)\n    ax.text(5, -0.5, 'Three branches handle different issue types, then converge',\n           ha='center', fontsize=10, style='italic')\n    \n    plt.tight_layout()\n    plt.show()
    
    print(f"\\nContext: PROCESS DOCUMENTATION\")\n    print(f\"Shows sequential steps with decision points and branching logic\")\n\n# ============================================================================\n# GRAPH 5: BOX PLOT\n# ============================================================================\n\ndef graph_5_box_plot():\n    \"\"\"\n    BOX PLOT - Statistical Summary\n    \n    Definition: Box-and-whisker plot displays five-number summary:\n    min, Q1, median, Q3, max.\n    \n    Best Use Contexts:\n    1. Group Comparison: Salary by department, test scores by school\n    2. Outlier Detection: Unusual measurements, anomalies\n    \n    Why Useful:\n    - Compact representation\n    - Multi-group comparison\n    - Statistical summary\n    - Outlier visibility\n    - Skewness detection\n    \"\"\"\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"GRAPH 5: BOX PLOT - Salary Distribution by Department\")\n    print(\"=\"*80)\n    print(__doc__)\n    \n    # Generate data\n    np.random.seed(42)\n    it = np.random.normal(loc=75000, scale=15000, size=50)\n    hr = np.random.normal(loc=55000, scale=10000, size=50)\n    sales = np.random.normal(loc=60000, scale=20000, size=50)\n    marketing = np.random.normal(loc=58000, scale=12000, size=50)\n    \n    # Add outliers\n    it = np.append(it, [120000, 15000])\n    sales = np.append(sales, [150000])\n    \n    salary_data = [it, hr, sales, marketing]\n    departments = ['IT', 'HR', 'Sales', 'Marketing']\n    \n    fig, ax = plt.subplots(figsize=(12, 7))\n    \n    bp = ax.boxplot(salary_data, labels=departments, patch_artist=True,\n                   showmeans=True,\n                   meanprops=dict(marker='D', markerfacecolor='red', markersize=8),\n                   medianprops=dict(color='darkblue', linewidth=2))\n    \n    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F7B731']\n    for patch, color in zip(bp['boxes'], colors):\n        patch.set_facecolor(color)\n        patch.set_alpha(0.7)\n    \n    ax.set_ylabel('Annual Salary ($)', fontsize=12, fontweight='bold')\n    ax.set_xlabel('Department', fontsize=12, fontweight='bold')\n    ax.set_title('Salary Distribution by Department - BOX PLOT (4 marks)',\n                fontsize=14, fontweight='bold')\n    ax.yaxis.grid(True, alpha=0.3)\n    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))\n    \n    plt.tight_layout()\n    plt.show()\n    \n    print(f\"\\nContext: DISTRIBUTION COMPARISON & OUTLIER DETECTION\")\n    for i, dept in enumerate(departments):\n        print(f\"{dept}: Median ${np.median(salary_data[i]):,.0f}\")\n\n# ============================================================================\n# GRAPH 6: BUBBLE MAP\n# ============================================================================\n\ndef graph_6_bubble_map():\n    \"\"\"\n    BUBBLE MAP - Geographic Analysis\n    \n    Definition: Geographic visualization with bubbles where size represents\n    magnitude and color represents category.\n    \n    Best Use Contexts:\n    1. Geographic Distribution: Sales by city, population density\n    2. Multi-Dimensional: Sales (size) by location + category (color)\n    \n    Why Useful:\n    - Geographic context\n    - Multiple dimensions\n    - Pattern discovery\n    - Intuitive\n    - Business value\n    \"\"\"\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"GRAPH 6: BUBBLE MAP - Sales by Store Location\")\n    print(\"=\"*80)\n    print(__doc__)\n    \n    stores = pd.DataFrame({\n        'Store': ['Downtown', 'Mall North', 'Mall South', 'Airport',\n                 'Harbor', 'Garden', 'Tech Park', 'University'],\n        'Longitude': [2, 1, 3, 4, 2, 1, 3, 2.5],\n        'Latitude': [3, 1, 1, 3, 4, 2, 2, 0.5],\n        'Sales': [150000, 85000, 92000, 180000, 110000, 65000, 140000, 72000],\n        'Category': ['Premium', 'Standard', 'Standard', 'Premium',\n                    'Standard', 'Budget', 'Premium', 'Budget']\n    })\n    \n    fig, ax = plt.subplots(figsize=(14, 8))\n    \n    color_map = {'Premium': '#FF6B6B', 'Standard': '#4ECDC4', 'Budget': '#95E1D3'}\n    colors = [color_map[cat] for cat in stores['Category']]\n    sizes = (stores['Sales'] / 1000) * 50\n    \n    scatter = ax.scatter(stores['Longitude'], stores['Latitude'], s=sizes,\n                        c=colors, alpha=0.6, edgecolors='black', linewidth=2)\n    \n    for idx, row in stores.iterrows():\n        ax.annotate(f\"{row['Store']}\\n${row['Sales']/1000:.0f}K\",\n                   xy=(row['Longitude'], row['Latitude']),\n                   xytext=(5, 5), textcoords='offset points',\n                   fontsize=9, fontweight='bold',\n                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))\n    \n    ax.set_xlabel('Longitude', fontsize=12, fontweight='bold')\n    ax.set_ylabel('Latitude', fontsize=12, fontweight='bold')\n    ax.set_title('Store Sales by Location - BUBBLE MAP (4 marks)',\n                fontsize=14, fontweight='bold')\n    \n    from matplotlib.patches import Patch\n    legend_elements = [Patch(facecolor=color_map['Premium'], edgecolor='black', label='Premium'),\n                      Patch(facecolor=color_map['Standard'], edgecolor='black', label='Standard'),\n                      Patch(facecolor=color_map['Budget'], edgecolor='black', label='Budget')]\n    ax.legend(handles=legend_elements, fontsize=11, loc='upper left')\n    \n    ax.text(0.5, 4.5, 'Bubble size = Sales volume', fontsize=10, style='italic')\n    ax.grid(True, alpha=0.3)\n    ax.set_xlim(-0.5, 5)\n    ax.set_ylim(-1, 5)\n    \n    plt.tight_layout()\n    plt.show()\n    \n    print(f\"\\nContext: GEOGRAPHIC MULTI-DIMENSIONAL ANALYSIS\")\n    print(stores.sort_values('Sales', ascending=False))\n\n# ============================================================================\n# MAIN EXECUTION\n# ============================================================================\n\ndef main():\n    \"\"\"\n    Execute all 6 graph implementations.\n    \"\"\"\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"DSC602 INFORMATION VISUALIZATION - JUNE 2025 EXAM\")\n    print(\"QUESTION 3: DATA VISUALIZATION GRAPHICS AND CHARACTERISTICS\")\n    print(\"=\"*80)\n    print(\"\\nPurpose: Identify which graph type is suitable for which context\")\n    print(\"Total Marks: 25 (4 marks per graph + 1 bonus)\")\n    print(\"\\n\" + \"=\"*80)\n    \n    # Execute all graphs\n    graph_1_line_graph()\n    graph_2_bar_chart()\n    graph_3_histogram()\n    graph_4_flow_chart()\n    graph_5_box_plot()\n    graph_6_bubble_map()\n    \n    # Summary\n    print(\"\\n\" + \"=\"*80)\n    print(\"SUMMARY: 6 GRAPH TYPES IMPLEMENTED\")\n    print(\"=\"*80)\n    \n    summary = pd.DataFrame({\n        'Graph': ['Line', 'Bar', 'Histogram', 'Flow', 'Box', 'Bubble'],\n        'Primary Use': ['Trends', 'Comparison', 'Distribution', 'Process', 'Statistical', 'Geographic'],\n        'Best For': [\n            'Stock prices, traffic',\n            'Sales by region',\n            'Age distribution',\n            'Workflows',\n            'Salary comparison',\n            'Location analysis'\n        ],\n        'Marks': [4, 4, 4, 4, 4, 4]\n    })\n    \n    print(\"\\n\" + summary.to_string(index=False))\n    print(\"\\nBonus marks: 1\")\n    print(\"Total: 25 marks\")\n    print(\"\\n\" + \"=\"*80)\n\nif __name__ == \"__main__\":\n    main()\n