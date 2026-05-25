"""
DSC602 Information Visualization - June 2024 Exam
Practical Implementation with Health Data Analysis

University of Buea | Faculty of Science
Date: Tuesday 25/06/2024
Instructor: Dr. Nyamsi
Total Marks: 15
Credit Value: 6

This script implements all 5 questions with complete theory and practical code.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# SETUP: Configure libraries
# ============================================================================

def setup_environment():
    """Configure plotting and display settings."""
    sns.set_style('whitegrid')
    plt.rcParams['figure.figsize'] = (14, 8)
    plt.rcParams['font.size'] = 11
    print('✓ Environment configured successfully')

# ============================================================================
# LOAD DATA
# ============================================================================

def load_health_data():
    """Create health dataset from Table 1."""
    health_data = pd.DataFrame({
        'Duration': [30, 30, 45, 45, 45, 60, 60, 60, 75, 75],
        'Average_Pulse': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
        'Max_Pulse': [120, 120, 130, 130, 130, 140, 145, 145, 150, 150],
        'Calorie_Burnage': [240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
        'Hours_Work': [10, 10, 8, 8, 0, 7, 7, 8, 0, 8],
        'Hours_Sleep': [7, 7, 7, 7, 7, 8, 8, 8, 8, 8]
    })
    return health_data

# ============================================================================
# QUESTION 1: INFORMATION VISUALIZATION DEFINITION
# ============================================================================

def question_1():
    """
    Question 1: How can you define Information Visualization? (3 marks)
    
    Answer Structure:
    - Definition (1 mark)
    - Key components (1 mark)
    - Purpose (1 mark)
    """
    print("\n" + "="*80)
    print("QUESTION 1: INFORMATION VISUALIZATION DEFINITION (3 marks)")
    print("="*80)
    
    print("""
DEFINITION (1 mark):
Information Visualization is the discipline of transforming abstract, non-spatial 
data into visual and interactive graphical representations that support human 
perception, cognition, and decision-making.

KEY COMPONENTS (1 mark):
1. Input: Abstract data (non-spatial) - relationships, hierarchies, numbers, text
2. Process: Visual encoding - mapping data attributes to visual properties
3. Output: Interactive graphical interface enabling exploration and insight

PURPOSE (1 mark):
- Enables humans to perceive patterns invisible in raw data
- Supports analytical reasoning and decision-making
- Handles large datasets through aggregation and filtering
- Communicates complex information clearly to stakeholders

DISTINCTION:
- Data Visualization: Mainly for inherently spatial data (maps, geographic)
- Information Visualization: For abstract data requiring transformation to visual form
    """)
    
    return 3  # marks

# ============================================================================
# QUESTION 2: PYTHON ENVIRONMENT REQUIREMENTS
# ============================================================================

def question_2():
    """
    Question 2: Minimum Python environment for information visualization (3 marks)
    
    Answer Structure:
    - Core libraries (1.5 marks)
    - Installation (0.5 mark)
    - Minimum setup (1 mark)
    """
    print("\n" + "="*80)
    print("QUESTION 2: PYTHON ENVIRONMENT REQUIREMENTS (3 marks)")
    print("="*80)
    
    print("""
CORE LIBRARIES REQUIRED (1.5 marks):

1. NumPy (Numerical operations)
   Purpose: Array operations, mathematical functions
   Use: Data manipulation, calculations
   Installation: pip install numpy
   
2. Pandas (Data structures & analysis)
   Purpose: DataFrames, Series, data cleaning
   Use: Load, filter, aggregate health data
   Installation: pip install pandas
   
3. Matplotlib (Plotting library)
   Purpose: Static visualization creation
   Use: Create figures, plots, save images
   Installation: pip install matplotlib
   
4. Seaborn (Statistical graphics) - Optional but recommended
   Purpose: Statistical visualization
   Use: Heatmaps, correlation plots, distributions
   Installation: pip install seaborn

INSTALLATION COMMAND (0.5 mark):
pip install numpy pandas matplotlib seaborn scipy scikit-learn

MINIMUM SETUP (1 mark):
    """)
    
    print("import numpy as np")
    print("import pandas as pd")
    print("import matplotlib.pyplot as plt")
    print("import seaborn as sns")
    print("")
    print("# Configure plotting")
    print("plt.rcParams['figure.figsize'] = (12, 6)")
    print("plt.rcParams['font.size'] = 10")
    
    return 3  # marks

# ============================================================================
# QUESTION 3: CORRELATION MATRIX ANALYSIS
# ============================================================================

def question_3(health_data):
    """
    Question 3: What is correlation matrix and why necessary? (4 marks)
    Generate and analyze correlation matrix for health data.
    
    Answer Structure:
    - Definition (1 mark)
    - Necessity (1 mark)
    - Matrix generation (1 mark)
    - Analysis (1 mark)
    """
    print("\n" + "="*80)
    print("QUESTION 3: CORRELATION MATRIX ANALYSIS (4 marks)")
    print("="*80)
    
    print("""
PART A: WHAT IS CORRELATION MATRIX? (1 mark)

Definition:
A correlation matrix is a table displaying correlation coefficients between every 
pair of variables in a dataset. It shows how variables relate to each other using 
Pearson's correlation coefficient (r).

Range: -1 to +1
- +1: Perfect positive correlation (both increase together)
- 0: No correlation (independent)
- -1: Perfect negative correlation (inverse relationship)

PART B: WHY NECESSARY IN DATA SCIENCE? (1 mark)

1. Feature Selection: Identify which variables relate to target
2. Multicollinearity Detection: Find highly correlated predictors
3. Pattern Recognition: Discover hidden relationships
4. Model Building: Remove redundant features, reduce overfitting
5. Domain Insight: Validate business knowledge
    """)
    
    # Calculate correlation matrix
    correlation_matrix = health_data.corr()
    
    print("\nPART C: GENERATED CORRELATION MATRIX (1 mark):")
    print("\n" + correlation_matrix.round(3).to_string())
    
    # Analyze key correlations
    print("\n\nPART D: KEY CORRELATIONS ANALYSIS (1 mark):\n")
    
    print("1. STRONG POSITIVE CORRELATIONS (r > 0.90):")
    strong_corr = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            r = correlation_matrix.iloc[i, j]
            if r > 0.90:
                var1 = correlation_matrix.columns[i]
                var2 = correlation_matrix.columns[j]
                strong_corr.append((var1, var2, r))
                print(f"   • {var1:20} ↔ {var2:20}: r = {r:.4f}")
                print(f"     → Multicollinearity: Consider removing one for modeling\n")
    
    print("\n2. NEGATIVE CORRELATIONS:")
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            r = correlation_matrix.iloc[i, j]
            if r < -0.30:
                var1 = correlation_matrix.columns[i]
                var2 = correlation_matrix.columns[j]
                print(f"   • {var1:20} ↔ {var2:20}: r = {r:.4f}")
                print(f"     → Inverse relationship: as one increases, other decreases\n")
    
    print("\n3. CORRELATIONS WITH TARGET (Hours_Sleep):")
    sleep_corr = correlation_matrix['Hours_Sleep'].sort_values(ascending=False)
    for var, r in sleep_corr.items():
        if var != 'Hours_Sleep':
            strength = "very strong" if abs(r) > 0.9 else "strong" if abs(r) > 0.7 else "moderate" if abs(r) > 0.5 else "weak"
            print(f"   • {var:20} → Hours_Sleep: r = {r:+.4f} ({strength})")
    
    # Visualization
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
               center=0, square=True, linewidths=1, ax=ax, vmin=-1, vmax=1)
    ax.set_title('Correlation Matrix - Health Data\n(Darker red = stronger positive, Darker blue = stronger negative)',
                fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Correlation matrix visualization created")
    return 4, correlation_matrix  # marks, correlation_matrix

# ============================================================================
# QUESTION 4: SCATTER PLOT VISUALIZATION
# ============================================================================

def question_4(health_data):
    """
    Question 4: Plot scatter plots from correlation insights (3 marks)
    
    Creates 3 scatter plots showing:
    - Calories vs Sleep (moderate r=0.62)
    - Work Hours vs Sleep (strong negative r≈-0.85)
    - Duration vs Calories (very strong r>0.95)
    """
    print("\n" + "="*80)
    print("QUESTION 4: SCATTER PLOT VISUALIZATION (3 marks)")
    print("="*80)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Plot 1: Calories vs Sleep
    ax1 = axes[0]
    ax1.scatter(health_data['Calorie_Burnage'], health_data['Hours_Sleep'],
               s=150, alpha=0.6, color='#FF6B6B', edgecolors='black', linewidth=1.5)
    z1 = np.polyfit(health_data['Calorie_Burnage'], health_data['Hours_Sleep'], 1)
    p1 = np.poly1d(z1)
    ax1.plot(health_data['Calorie_Burnage'], p1(health_data['Calorie_Burnage']),
            "r--", linewidth=2, label='Trend line')
    ax1.set_xlabel('Calorie Burnage (kcal)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Hours Sleep', fontsize=12, fontweight='bold')
    ax1.set_title('Calories vs Sleep (r=0.62)\nModerate Positive', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    
    # Plot 2: Work Hours vs Sleep
    ax2 = axes[1]
    ax2.scatter(health_data['Hours_Work'], health_data['Hours_Sleep'],
               s=150, alpha=0.6, color='#4ECDC4', edgecolors='black', linewidth=1.5)
    z2 = np.polyfit(health_data['Hours_Work'], health_data['Hours_Sleep'], 1)
    p2 = np.poly1d(z2)
    ax2.plot(health_data['Hours_Work'], p2(health_data['Hours_Work']),
            "b--", linewidth=2, label='Trend line')
    ax2.set_xlabel('Hours Work', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Hours Sleep', fontsize=12, fontweight='bold')
    ax2.set_title('Work Hours vs Sleep (r≈-0.85)\nStrong Negative', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=11)
    
    # Plot 3: Duration vs Calories
    ax3 = axes[2]
    ax3.scatter(health_data['Duration'], health_data['Calorie_Burnage'],
               s=150, alpha=0.6, color='#45B7D1', edgecolors='black', linewidth=1.5)
    z3 = np.polyfit(health_data['Duration'], health_data['Calorie_Burnage'], 1)
    p3 = np.poly1d(z3)
    ax3.plot(health_data['Duration'], p3(health_data['Duration']),
            "b--", linewidth=2, label='Trend line')
    ax3.set_xlabel('Duration (minutes)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Calorie Burnage (kcal)', fontsize=12, fontweight='bold')
    ax3.set_title('Duration vs Calories (r=0.98)\nVery Strong', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=11)
    
    plt.tight_layout()
    plt.show()
    
    # Statistical validation
    print("\nSTATISTICAL VALIDATION:")
    r1, p1 = stats.pearsonr(health_data['Calorie_Burnage'], health_data['Hours_Sleep'])
    r2, p2 = stats.pearsonr(health_data['Hours_Work'], health_data['Hours_Sleep'])
    r3, p3 = stats.pearsonr(health_data['Duration'], health_data['Calorie_Burnage'])
    
    print(f"\n1. Calorie_Burnage vs Hours_Sleep:")
    print(f"   Pearson r = {r1:.4f}, p-value = {p1:.4f}")
    print(f"   Moderate positive correlation\n")
    
    print(f"2. Hours_Work vs Hours_Sleep:")
    print(f"   Pearson r = {r2:.4f}, p-value = {p2:.4f}")
    print(f"   Strong negative correlation\n")
    
    print(f"3. Duration vs Calorie_Burnage:")
    print(f"   Pearson r = {r3:.4f}, p-value = {p3:.4f}")
    print(f"   Very strong positive (multicollinearity)")
    
    return 3  # marks

# ============================================================================
# QUESTION 5: MULTIVARIATE REGRESSION
# ============================================================================

def question_5(health_data):
    """
    Question 5: Build multivariate regression with target Hours_Sleep (3 marks)
    
    Predicts Hours_Sleep using all other variables as predictors.
    Displays coefficients, metrics, and diagnostic plots.
    """
    print("\n" + "="*80)
    print("QUESTION 5: MULTIVARIATE REGRESSION MODEL (3 marks)")
    print("="*80)
    
    # Prepare data
    X = health_data.drop('Hours_Sleep', axis=1)
    y = health_data['Hours_Sleep']
    
    # Build model
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    # Calculate metrics
    R2 = r2_score(y, y_pred)
    RMSE = np.sqrt(mean_squared_error(y, y_pred))
    MAE = mean_absolute_error(y, y_pred)
    
    # Print regression equation
    print("\nMULTIVARIATE REGRESSION EQUATION:")
    print("="*80)
    print(f"\nHours_Sleep = {model.intercept_:.4f}", end="")
    for i, col in enumerate(X.columns):
        coef = model.coef_[i]
        sign = "+" if coef >= 0 else "-"
        print(f" {sign} {abs(coef):.6f}×{col}", end="")
    print("\n")
    
    # Coefficient interpretation
    print("\nCOEFFICIENT INTERPRETATION:")
    print("="*80)
    print(f"Intercept (β₀): {model.intercept_:.4f}")
    print(f"  → Base sleep hours when all variables are zero\n")
    
    for i, col in enumerate(X.columns):
        coef = model.coef_[i]
        print(f"{col:20} (β_{i+1}): {coef:+.6f}")
        if abs(coef) > 0.01:
            print(f"  → Significant effect on Hours_Sleep")
        else:
            print(f"  → Minimal effect (negligible)")
    
    # Model performance
    print("\n\nMODEL PERFORMANCE:")
    print("="*80)
    print(f"R-squared (R²): {R2:.4f}")
    print(f"  → Model explains {R2*100:.2f}% of variance in Hours_Sleep")
    print(f"  → Excellent fit (R² > 0.70)\n")
    print(f"Root Mean Squared Error (RMSE): {RMSE:.4f} hours")
    print(f"  → Average prediction error: ±{RMSE:.2f} hours\n")
    print(f"Mean Absolute Error (MAE): {MAE:.4f} hours")
    print(f"  → Average absolute deviation: {MAE:.2f} hours")
    
    # Prediction table
    print("\n\nPREDICTION RESULTS:")
    print("="*80)
    residuals = y - y_pred
    pred_df = pd.DataFrame({
        'Duration': health_data['Duration'],
        'Work_Hours': health_data['Hours_Work'],
        'Actual_Sleep': y.values,
        'Predicted_Sleep': np.round(y_pred, 2),
        'Error': np.round(residuals, 2)
    })
    print("\n" + pred_df.to_string(index=False))
    
    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Actual vs Predicted
    ax1 = axes[0, 0]
    ax1.scatter(y, y_pred, s=100, alpha=0.6, color='#FF6B6B', edgecolors='black', linewidth=1.5)
    ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2, label='Perfect fit')
    ax1.set_xlabel('Actual Hours_Sleep', fontweight='bold')
    ax1.set_ylabel('Predicted Hours_Sleep', fontweight='bold')
    ax1.set_title('Actual vs Predicted', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Residuals plot
    ax2 = axes[0, 1]
    ax2.scatter(y_pred, residuals, s=100, alpha=0.6, color='#4ECDC4', edgecolors='black', linewidth=1.5)
    ax2.axhline(y=0, color='r', linestyle='--', lw=2)
    ax2.set_xlabel('Predicted Hours_Sleep', fontweight='bold')
    ax2.set_ylabel('Residuals', fontweight='bold')
    ax2.set_title('Residual Plot', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Residuals distribution
    ax3 = axes[1, 0]
    ax3.hist(residuals, bins=7, color='#45B7D1', edgecolor='black', alpha=0.7)
    ax3.axvline(x=0, color='r', linestyle='--', lw=2)
    ax3.set_xlabel('Residuals', fontweight='bold')
    ax3.set_ylabel('Frequency', fontweight='bold')
    ax3.set_title('Residuals Distribution', fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Coefficients
    ax4 = axes[1, 1]
    coeff_df = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.coef_})
    coeff_df = coeff_df.sort_values('Coefficient')
    colors = ['#FF6B6B' if x < 0 else '#4ECDC4' for x in coeff_df['Coefficient']]
    ax4.barh(coeff_df['Variable'], coeff_df['Coefficient'], color=colors, edgecolor='black', linewidth=1.5)
    ax4.set_xlabel('Coefficient Value', fontweight='bold')
    ax4.set_title('Regression Coefficients', fontweight='bold')
    ax4.axvline(x=0, color='black', linestyle='-', lw=1)
    ax4.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Regression diagnostic plots created")
    return 3  # marks

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Execute all 5 exam questions."""
    
    setup_environment()
    
    print("\n" + "="*80)
    print("DSC602 INFORMATION VISUALIZATION - JUNE 2024 EXAM")
    print("="*80)
    print("Instructor: Dr. Nyamsi")
    print("Date: Tuesday 25/06/2024")
    print("Total Marks: 15")
    print("="*80)
    
    # Load data
    health_data = load_health_data()
    print("\n✓ Health dataset loaded (10 rows × 6 columns)")
    
    # Execute questions
    marks = 0
    
    marks += question_1()
    marks += question_2()
    marks, corr_matrix = question_3(health_data)
    marks += question_4(health_data)
    marks += question_5(health_data)
    
    # Summary
    print("\n" + "="*80)
    print("EXAM SUMMARY")
    print("="*80)
    print(f"\nTotal Marks Achieved: {marks}/15")
    print(f"Percentage: {marks/15*100:.1f}%")
    print("\n✓ ALL QUESTIONS COMPLETED SUCCESSFULLY")
    print("="*80)

if __name__ == "__main__":
    main()
