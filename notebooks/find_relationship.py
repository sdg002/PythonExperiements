"""
Sample code to find relationships between two data series
Includes correlation analysis, regression, and visualization techniques
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import pearsonr, spearmanr, kendalltau
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

def generate_sample_data():
    """Generate sample data with different types of relationships"""
    np.random.seed(42)
    n = 100
    
    # Series with strong positive correlation
    x1 = np.random.normal(0, 1, n)
    y1 = 2 * x1 + np.random.normal(0, 0.5, n)
    
    # Series with negative correlation
    x2 = np.random.normal(0, 1, n)
    y2 = -1.5 * x2 + np.random.normal(0, 0.8, n)
    
    # Series with no correlation
    x3 = np.random.normal(0, 1, n)
    y3 = np.random.normal(0, 1, n)
    
    # Series with non-linear relationship
    x4 = np.linspace(-3, 3, n)
    y4 = x4**2 + np.random.normal(0, 1, n)
    
    return (x1, y1), (x2, y2), (x3, y3), (x4, y4)

def correlation_analysis(x, y, series_name="Series"):
    """Perform comprehensive correlation analysis"""
    print(f"\n=== Correlation Analysis for {series_name} ===")
    
    # Pearson correlation (linear relationship)
    pearson_corr, pearson_p = pearsonr(x, y)
    print(f"Pearson Correlation: {pearson_corr:.4f} (p-value: {pearson_p:.4f})")
    
    # Spearman correlation (monotonic relationship)
    spearman_corr, spearman_p = spearmanr(x, y)
    print(f"Spearman Correlation: {spearman_corr:.4f} (p-value: {spearman_p:.4f})")
    
    # Kendall's tau (rank-based correlation)
    kendall_corr, kendall_p = kendalltau(x, y)
    print(f"Kendall's Tau: {kendall_corr:.4f} (p-value: {kendall_p:.4f})")
    
    # Interpretation
    def interpret_correlation(corr):
        abs_corr = abs(corr)
        if abs_corr >= 0.8:
            return "Very Strong"
        elif abs_corr >= 0.6:
            return "Strong"
        elif abs_corr >= 0.4:
            return "Moderate"
        elif abs_corr >= 0.2:
            return "Weak"
        else:
            return "Very Weak/No"
    
    print(f"Relationship Strength: {interpret_correlation(pearson_corr)}")
    print(f"Direction: {'Positive' if pearson_corr > 0 else 'Negative' if pearson_corr < 0 else 'No clear direction'}")
    
    return {
        'pearson': (pearson_corr, pearson_p),
        'spearman': (spearman_corr, spearman_p),
        'kendall': (kendall_corr, kendall_p)
    }

def regression_analysis(x, y, series_name="Series"):
    """Perform linear regression analysis"""
    print(f"\n=== Regression Analysis for {series_name} ===")
    
    # Reshape for sklearn
    X = x.reshape(-1, 1)
    
    # Fit linear regression
    model = LinearRegression()
    model.fit(X, y)
    
    # Predictions
    y_pred = model.predict(X)
    
    # Metrics
    r2 = r2_score(y, y_pred)
    slope = model.coef_[0]
    intercept = model.intercept_
    
    print(f"Linear Equation: y = {slope:.4f}x + {intercept:.4f}")
    print(f"R-squared: {r2:.4f}")
    print(f"Explained Variance: {r2*100:.2f}%")
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r2': r2,
        'predictions': y_pred
    }

def advanced_relationship_tests(x, y, series_name="Series"):
    """Perform advanced statistical tests for relationships"""
    print(f"\n=== Advanced Tests for {series_name} ===")
    
    # Mutual Information (non-linear relationships)
    from sklearn.feature_selection import mutual_info_regression
    X = x.reshape(-1, 1)
    mi_score = mutual_info_regression(X, y)[0]
    print(f"Mutual Information Score: {mi_score:.4f}")
    
    # Distance Correlation (detects non-linear dependencies)
    try:
        from dcor import distance_correlation
        dcor_val = distance_correlation(x, y)
        print(f"Distance Correlation: {dcor_val:.4f}")
    except ImportError:
        print("Distance Correlation: (dcor package not installed)")
    
    # Maximal Information Coefficient (MIC)
    try:
        from minepy import MINE
        mine = MINE()
        mine.compute_score(x, y)
        mic_score = mine.mic()
        print(f"Maximal Information Coefficient (MIC): {mic_score:.4f}")
    except ImportError:
        print("MIC: (minepy package not installed)")

def visualize_relationship(x, y, series_name="Series", regression_results=None):
    """Create comprehensive visualization of the relationship"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(f'Relationship Analysis: {series_name}', fontsize=16)
    
    # Scatter plot with regression line
    axes[0, 0].scatter(x, y, alpha=0.6, color='blue')
    if regression_results:
        axes[0, 0].plot(x, regression_results['predictions'], color='red', linewidth=2)
        axes[0, 0].set_title(f'Scatter Plot with Regression Line\nR² = {regression_results["r2"]:.4f}')
    else:
        axes[0, 0].set_title('Scatter Plot')
    axes[0, 0].set_xlabel('X')
    axes[0, 0].set_ylabel('Y')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Residual plot (if regression performed)
    if regression_results:
        residuals = y - regression_results['predictions']
        axes[0, 1].scatter(regression_results['predictions'], residuals, alpha=0.6, color='green')
        axes[0, 1].axhline(y=0, color='red', linestyle='--')
        axes[0, 1].set_title('Residual Plot')
        axes[0, 1].set_xlabel('Predicted Values')
        axes[0, 1].set_ylabel('Residuals')
        axes[0, 1].grid(True, alpha=0.3)
    else:
        axes[0, 1].hist2d(x, y, bins=20)
        axes[0, 1].set_title('2D Histogram')
        axes[0, 1].set_xlabel('X')
        axes[0, 1].set_ylabel('Y')
    
    # Distribution plots
    axes[1, 0].hist(x, bins=20, alpha=0.7, color='blue', label='X')
    axes[1, 0].hist(y, bins=20, alpha=0.7, color='red', label='Y')
    axes[1, 0].set_title('Distribution Comparison')
    axes[1, 0].set_xlabel('Value')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Q-Q plot for normality check
    from scipy.stats import probplot
    probplot(x, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot (X vs Normal)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def comprehensive_analysis(x, y, series_name="Series"):
    """Perform comprehensive relationship analysis"""
    print(f"\n{'='*60}")
    print(f"COMPREHENSIVE RELATIONSHIP ANALYSIS: {series_name}")
    print(f"{'='*60}")
    
    # Basic statistics
    print(f"\n=== Basic Statistics ===")
    print(f"X - Mean: {np.mean(x):.4f}, Std: {np.std(x):.4f}, Range: [{np.min(x):.4f}, {np.max(x):.4f}]")
    print(f"Y - Mean: {np.mean(y):.4f}, Std: {np.std(y):.4f}, Range: [{np.min(y):.4f}, {np.max(y):.4f}]")
    
    # Correlation analysis
    corr_results = correlation_analysis(x, y, series_name)
    
    # Regression analysis
    reg_results = regression_analysis(x, y, series_name)
    
    # Advanced tests
    advanced_relationship_tests(x, y, series_name)
    
    # Visualization
    visualize_relationship(x, y, series_name, reg_results)
    
    return {
        'correlations': corr_results,
        'regression': reg_results
    }

def demo_with_sample_data():
    """Demonstrate relationship analysis with sample data"""
    print("Generating sample data with different relationship patterns...")
    
    # Generate sample data
    positive_corr, negative_corr, no_corr, nonlinear = generate_sample_data()
    
    # Analyze each relationship
    datasets = [
        (positive_corr, "Strong Positive Correlation"),
        (negative_corr, "Negative Correlation"),
        (no_corr, "No Correlation"),
        (nonlinear, "Non-linear Relationship")
    ]
    
    results = {}
    for (x, y), name in datasets:
        results[name] = comprehensive_analysis(x, y, name)
    
    return results

def analyze_custom_data(x_data, y_data, series_name="Custom Data"):
    """Analyze relationship between custom data series"""
    x = np.array(x_data)
    y = np.array(y_data)
    
    if len(x) != len(y):
        raise ValueError("Both series must have the same length")
    
    return comprehensive_analysis(x, y, series_name)

if __name__ == "__main__":
    print("Relationship Analysis Demo")
    print("=" * 50)
    
    # Run demo with sample data
    demo_results = demo_with_sample_data()
    
    # Example of analyzing custom data
    print("\n" + "="*60)
    print("CUSTOM DATA EXAMPLE")
    print("="*60)
    
    # Example custom data (temperature vs ice cream sales)
    temperature = [20, 25, 30, 35, 40, 22, 28, 33, 38, 24, 29, 34, 39, 21, 26, 31, 36, 23, 27, 32]
    ice_cream_sales = [50, 75, 100, 125, 150, 60, 90, 115, 140, 70, 95, 120, 145, 55, 80, 105, 130, 65, 85, 110]
    
    custom_results = analyze_custom_data(temperature, ice_cream_sales, "Temperature vs Ice Cream Sales")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)