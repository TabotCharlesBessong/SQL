"""
DSC602 Information Visualization - Exam Question 2 Solution
Complete Python Implementation for Data Visualization

Date: 2023
Question: 20 marks
Topic: Creating various data visualizations from a sales dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# SETUP AND CONFIGURATION
# ============================================================================

def setup_plotting():
    """Configure matplotlib for optimal visualization"""
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    print("✓ Plotting environment configured")


# ============================================================================
# PART 1: CREATE THE DATA FRAME
# ============================================================================

def create_sales_dataframe():
    """
    Create a pandas DataFrame from the exam provided table.
    
    Returns:
        DataFrame: Sales data with columns for names and sales by category
    """
    print("\n" + "="*70)
    print("PART 1: CREATING DATA FRAME")
    print("="*70)
    
    # Raw data from exam table
    data = {
        'Sales_Name': ['Henry', 'Peter', 'Nichoulas', 'Mary', 'Dan', 'Oussy', 'Maboukam'],
        'Land_sales': [12, 15, 25, 8, 5, 0, 10],
        'Clothe_sales': [2500, 1900, 1800, 5000, 2850, 8005, 5000],
        'Book_sales': [2300, 2000, 180, 5000, 20, 12, 15]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add total sales column
    df['Total_Sales'] = df['Land_sales'] + df['Clothe_sales'] + df['Book_sales']
    
    print("\nDataFrame created successfully!")
    print("\nData Preview:")
    print(df.to_string(index=False))
    
    print("\n\nDataFrame Information:")
    print(df.info())
    
    print("\n\nBasic Statistics:")
    print(df.describe())
    
    return df


# ============================================================================
# PART 2: BAR PLOT OF SALES VOLUME
# ============================================================================

def create_bar_plot(df, save_path=None):
    """
    Create a bar plot showing total sales volume for each sales representative.
    
    THEORETICAL EXPLANATION:
    A bar plot uses rectangular bars with heights proportional to values.
    Bar plots are effective for:
    - Comparing values across categories
    - Showing differences between groups
    - Displaying discrete, quantitative data
    - Easy value reading and direct comparison
    
    In this case: Each sales representative has a bar showing total sales.
    
    Args:
        df: DataFrame with sales data
        save_path: Optional path to save the figure
    """
    print("\n" + "="*70)
    print("PART 2: BAR PLOT OF SALES VOLUME")
    print("="*70)
    
    print("\nTheoretical Explanation:")
    print("- Bar plots compare quantitative values across categories")
    print("- Height of bar represents magnitude of value")
    print("- Easy to rank and compare values")
    print("- Effective for showing performance differences")
    
    plt.figure(figsize=(12, 6))
    
    # Create bars
    bars = plt.bar(df['Sales_Name'], df['Total_Sales'], 
                   color='steelblue', edgecolor='navy', alpha=0.7, width=0.6)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Styling
    plt.xlabel('Sales Representative', fontsize=12, fontweight='bold')
    plt.ylabel('Total Sales Volume', fontsize=12, fontweight='bold')
    plt.title('Total Sales Volume by Sales Representative', 
             fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Bar plot saved to: {save_path}")
    
    plt.show()
    
    # Print summary statistics
    print("\n\nBar Plot Analysis:")
    top_3 = df.nlargest(3, 'Total_Sales')[['Sales_Name', 'Total_Sales']]
    print("\nTop 3 Sales Representatives:")
    for idx, (_, row) in enumerate(top_3.iterrows(), 1):
        print(f"  {idx}. {row['Sales_Name']}: {row['Total_Sales']:,}")
    
    bottom_3 = df.nsmallest(3, 'Total_Sales')[['Sales_Name', 'Total_Sales']]
    print("\nBottom 3 Sales Representatives:")
    for idx, (_, row) in enumerate(bottom_3.iterrows(), 1):
        print(f"  {idx}. {row['Sales_Name']}: {row['Total_Sales']:,}")


# ============================================================================
# PART 3: PIE CHART OF ITEM SALES
# ============================================================================

def create_pie_chart(df, save_path=None):
    """
    Create a pie chart showing the proportion of sales by product category.
    
    THEORETICAL EXPLANATION:
    Pie charts display data as slices of a circle, where each slice represents
    a proportion of the whole. They are effective for:
    - Showing part-to-whole relationships
    - Displaying categorical data as percentages
    - Visualizing composition (how parts make up a total)
    - Quick understanding of relative proportions
    
    In this case: Each product category has a slice showing its proportion
    of total sales.
    
    Args:
        df: DataFrame with sales data
        save_path: Optional path to save the figure
    """
    print("\n" + "="*70)
    print("PART 3: PIE CHART OF ITEM SALES")
    print("="*70)
    
    print("\nTheoretical Explanation:")
    print("- Pie charts show part-to-whole relationships")
    print("- Each slice represents proportion of total")
    print("- Useful for showing composition")
    print("- Percentage labels add clarity")
    
    # Calculate totals by category
    category_totals = {
        'Land Sales': df['Land_sales'].sum(),
        'Clothing Sales': df['Clothe_sales'].sum(),
        'Book Sales': df['Book_sales'].sum()
    }
    
    plt.figure(figsize=(10, 8))
    
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    explode = (0.05, 0.05, 0.05)  # Slightly separate all slices
    
    wedges, texts, autotexts = plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True,
        textprops={'fontsize': 11, 'fontweight': 'bold'}
    )
    
    # Enhance appearance
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
    
    plt.title('Proportion of Sales by Product Category', 
             fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Pie chart saved to: {save_path}")
    
    plt.show()
    
    # Print analysis
    print("\n\nPie Chart Analysis:")
    print("\nTotal Sales by Product Category:")
    total_all = sum(category_totals.values())
    for category, total in category_totals.items():
        percentage = (total / total_all) * 100
        print(f"  {category}: {total:,} ({percentage:.1f}%)")


# ============================================================================
# PART 4: BOX PLOT OF ITEM SALES
# ============================================================================

def create_box_plot(df, save_path=None):
    """
    Create a box plot showing distribution of sales across product categories.
    
    THEORETICAL EXPLANATION:
    Box plots display data distribution using quartiles:
    - Box: Contains middle 50% of data (interquartile range, IQR)
    - Line in box: Represents median (50th percentile)
    - Whiskers: Extend to show range of data
    - Points: Outliers (data outside 1.5 × IQR)
    
    Box plots are excellent for:
    - Comparing distributions across categories
    - Identifying outliers and anomalies
    - Understanding data spread and skewness
    - Detecting inconsistencies in data
    
    Args:
        df: DataFrame with sales data
        save_path: Optional path to save the figure
    """
    print("\n" + "="*70)
    print("PART 4: BOX PLOT OF ITEM SALES")
    print("="*70)
    
    print("\nTheoretical Explanation:")
    print("- Box plots show distribution of data")
    print("- Box contains 50% of data (Q1 to Q3)")
    print("- Line in box shows median")
    print("- Whiskers show range")
    print("- Points show outliers")
    print("- Enables comparison of distributions")
    
    # Prepare data
    box_data = [
        df['Land_sales'],
        df['Clothe_sales'],
        df['Book_sales']
    ]
    
    plt.figure(figsize=(10, 6))
    
    bp = plt.boxplot(
        box_data,
        labels=['Land Sales', 'Clothing Sales', 'Book Sales'],
        patch_artist=True,
        notch=False,
        showmeans=True,
        meanprops=dict(marker='D', markerfacecolor='red', markersize=8)
    )
    
    # Customize colors
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Styling
    plt.ylabel('Sales Volume', fontsize=12, fontweight='bold')
    plt.title('Distribution of Sales by Product Category', 
             fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Box plot saved to: {save_path}")
    
    plt.show()
    
    # Print statistical summary
    print("\n\nBox Plot Analysis - Statistical Summary:\n")
    categories = ['Land_sales', 'Clothe_sales', 'Book_sales']
    category_names = ['Land Sales', 'Clothing Sales', 'Book Sales']
    
    for cat, cat_name in zip(categories, category_names):
        data = df[cat]
        print(f"\n{cat_name}:")
        print(f"  Minimum: {data.min()}")
        print(f"  Q1 (25th percentile): {data.quantile(0.25)}")
        print(f"  Median (Q2): {data.median()}")
        print(f"  Q3 (75th percentile): {data.quantile(0.75)}")
        print(f"  Maximum: {data.max()}")
        print(f"  Mean: {data.mean():.2f}")
        print(f"  Std Dev: {data.std():.2f}")
        print(f"  IQR (Q3-Q1): {data.quantile(0.75) - data.quantile(0.25)}")


# ============================================================================
# PART 5: AREA PLOT OF ITEM SALES
# ============================================================================

def create_area_plot(df, save_path=None):
    """
    Create area plots showing sales trends by category and representative.
    
    THEORETICAL EXPLANATION:
    Area plots are similar to line plots but with the area below lines filled.
    Area plots are effective for:
    - Showing trends over categories (especially when ordered)
    - Displaying cumulative totals or compositions
    - Emphasizing magnitude and change
    - Comparing multiple series that should be stacked
    
    Two types are created:
    1. Stacked area plot: Shows composition and total
    2. Non-stacked area plot: Shows individual trends
    
    Args:
        df: DataFrame with sales data
        save_path: Optional path to save figures
    """
    print("\n" + "="*70)
    print("PART 5: AREA PLOT OF ITEM SALES")
    print("="*70)
    
    print("\nTheoretical Explanation:")
    print("- Area plots show trends with emphasis on magnitude")
    print("- Area under line shows cumulative value")
    print("- Stacked areas show composition")
    print("- Non-stacked areas show individual trends")
    print("- Useful for multi-series comparison")
    
    # -------- STACKED AREA PLOT --------
    print("\n\nCreating Stacked Area Plot...")
    print("(Shows composition: how each category contributes to total)")
    
    plt.figure(figsize=(12, 6))
    
    x = np.arange(len(df['Sales_Name']))
    
    plt.stackplot(x,
                 df['Land_sales'],
                 df['Clothe_sales'],
                 df['Book_sales'],
                 labels=['Land Sales', 'Clothing Sales', 'Book Sales'],
                 colors=['#ff9999', '#66b3ff', '#99ff99'],
                 alpha=0.7)
    
    plt.xlabel('Sales Representative', fontsize=12, fontweight='bold')
    plt.ylabel('Sales Volume', fontsize=12, fontweight='bold')
    plt.title('Stacked Area Plot: Sales Distribution by Representative', 
             fontsize=14, fontweight='bold')
    plt.xticks(x, df['Sales_Name'], rotation=45, ha='right')
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(f"{save_path}_stacked.png", dpi=300, bbox_inches='tight')
        print(f"✓ Stacked area plot saved to: {save_path}_stacked.png")
    
    plt.show()
    
    # -------- NON-STACKED AREA PLOT --------
    print("\n\nCreating Non-Stacked Area Plot...")
    print("(Shows individual trends for each category)")
    
    plt.figure(figsize=(12, 6))
    
    # Plot each series
    plt.plot(df['Sales_Name'], df['Land_sales'], 
            marker='o', linewidth=2, label='Land Sales', color='#ff9999')
    plt.fill_between(range(len(df['Sales_Name'])), df['Land_sales'], 
                     alpha=0.3, color='#ff9999')
    
    plt.plot(df['Sales_Name'], df['Clothe_sales'], 
            marker='s', linewidth=2, label='Clothing Sales', color='#66b3ff')
    plt.fill_between(range(len(df['Sales_Name'])), df['Clothe_sales'], 
                     alpha=0.3, color='#66b3ff')
    
    plt.plot(df['Sales_Name'], df['Book_sales'], 
            marker='^', linewidth=2, label='Book Sales', color='#99ff99')
    plt.fill_between(range(len(df['Sales_Name'])), df['Book_sales'], 
                     alpha=0.3, color='#99ff99')
    
    plt.xlabel('Sales Representative', fontsize=12, fontweight='bold')
    plt.ylabel('Sales Volume', fontsize=12, fontweight='bold')
    plt.title('Area Plot: Sales Trends by Representative and Category', 
             fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(f"{save_path}_individual.png", dpi=300, bbox_inches='tight')
        print(f"✓ Individual area plot saved to: {save_path}_individual.png")
    
    plt.show()


# ============================================================================
# COMPREHENSIVE ANALYSIS AND SUMMARY
# ============================================================================

def print_comprehensive_analysis(df):
    """
    Print comprehensive analysis and insights from the data.
    
    Args:
        df: DataFrame with sales data
    """
    print("\n" + "="*70)
    print("COMPREHENSIVE DATA ANALYSIS SUMMARY")
    print("="*70)
    
    total_all = df['Total_Sales'].sum()
    
    print("\n1. TOP PERFORMERS (by Total Sales):")
    top_performers = df.nlargest(3, 'Total_Sales')[['Sales_Name', 'Total_Sales']]
    for idx, (_, row) in enumerate(top_performers.iterrows(), 1):
        percentage = (row['Total_Sales'] / total_all) * 100
        print(f"   {idx}. {row['Sales_Name']:12} | Total: {row['Total_Sales']:6,} ({percentage:5.1f}%)")
    
    print("\n2. PRODUCT CATEGORY INSIGHTS:")
    print(f"   - Land Sales Total:      {df['Land_sales'].sum():8,}")
    print(f"   - Clothing Sales Total:  {df['Clothe_sales'].sum():8,}")
    print(f"   - Book Sales Total:      {df['Book_sales'].sum():8,}")
    print(f"   - Grand Total:           {total_all:8,}")
    
    print("\n3. SALES PERFORMANCE VARIANCE:")
    max_idx = df['Total_Sales'].idxmax()
    min_idx = df['Total_Sales'].idxmin()
    print(f"   - Highest Sale:  {df.loc[max_idx, 'Total_Sales']:6,} (by {df.loc[max_idx, 'Sales_Name']})")
    print(f"   - Lowest Sale:   {df.loc[min_idx, 'Total_Sales']:6,} (by {df.loc[min_idx, 'Sales_Name']})")
    print(f"   - Average Sale:  {df['Total_Sales'].mean():6.2f}")
    print(f"   - Std Dev:       {df['Total_Sales'].std():6.2f}")
    
    print("\n4. PRODUCT DISTRIBUTION INSIGHTS:")
    land_pct = (df['Land_sales'].sum() / total_all) * 100
    clothe_pct = (df['Clothe_sales'].sum() / total_all) * 100
    book_pct = (df['Book_sales'].sum() / total_all) * 100
    print(f"   - Clothing dominates with {clothe_pct:.1f}% of total sales")
    print(f"   - Book sales represent   {book_pct:.1f}% of total sales")
    print(f"   - Land sales represent   {land_pct:.1f}% of total sales")
    
    print("\n5. INDIVIDUAL REPRESENTATIVE DETAILS:")
    display_df = df[['Sales_Name', 'Land_sales', 'Clothe_sales', 'Book_sales', 'Total_Sales']].copy()
    display_df = display_df.sort_values('Total_Sales', ascending=False)
    print(display_df.to_string(index=False))
    
    print("\n" + "="*70)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("\n" + "="*70)
    print("DSC602 INFORMATION VISUALIZATION - EXAM QUESTION 2")
    print("Complete Solution: Data Visualization with Python")
    print("="*70)
    
    # Setup
    setup_plotting()
    
    # Create data
    df = create_sales_dataframe()
    
    # Create visualizations
    create_bar_plot(df)
    create_pie_chart(df)
    create_box_plot(df)
    create_area_plot(df)
    
    # Print analysis
    print_comprehensive_analysis(df)
    
    print("\n✓ All visualizations and analysis complete!")
    print("\nFiles created:")
    print("  - Various PNG figures (if save paths specified)")
    print("  - This script demonstrates all required visualizations")


if __name__ == "__main__":
    main()
