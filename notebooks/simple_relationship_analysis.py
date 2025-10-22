"""
Simple example to find relationships between two data series
Focus on essential methods using common libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def quick_relationship_check(x, y, plot=True, title="Some title"):
    """
    Quick function to check relationship between two series
    
    Parameters:
    x, y: array-like, the two series to analyze
    plot: bool, whether to create a scatter plot
    
    Returns:
    dict with correlation metrics and interpretation
    """
    
    # Convert to numpy arrays
    x = np.array(x)
    y = np.array(y)
    
    # Calculate correlations
    pearson_corr, pearson_p = pearsonr(x, y)
    spearman_corr, spearman_p = spearmanr(x, y)
    
    # Linear regression
    X = x.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    
    # Interpretation
    def interpret_strength(corr):
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
            return "Very Weak"
    
    # Results
    results = {
        'pearson_correlation': pearson_corr,
        'pearson_p_value': pearson_p,
        'spearman_correlation': spearman_corr,
        'spearman_p_value': spearman_p,
        'r_squared': r2,
        'relationship_strength': interpret_strength(pearson_corr),
        'direction': 'Positive' if pearson_corr > 0 else 'Negative' if pearson_corr < 0 else 'None',
        'linear_equation': f"y = {model.coef_[0]:.3f}x + {model.intercept_:.3f}"
    }
    
    # Print summary
    print("Relationship Analysis Summary:")
    print("-" * 30)
    print(f"Pearson Correlation: {pearson_corr:.3f} (p={pearson_p:.3f})")
    print(f"Spearman Correlation: {spearman_corr:.3f} (p={spearman_p:.3f})")
    print(f"R-squared: {r2:.3f}")
    print(f"Relationship: {results['relationship_strength']} {results['direction']}")
    print(f"Linear Model: {results['linear_equation']}")
    
    # Significance interpretation
    alpha = 0.05
    if pearson_p < alpha:
        print(f"✓ Relationship is statistically significant (p < {alpha})")
    else:
        print(f"✗ Relationship is not statistically significant (p >= {alpha})")
    
    # Create plot if requested
    if plot:
        plt.figure(figsize=(10, 6))
        
        # Scatter plot
        plt.subplot(1, 2, 1)
        plt.scatter(x, y, alpha=0.6, color='blue')
        plt.plot(x, y_pred, color='red', linewidth=2, label=f'Linear fit (R²={r2:.3f})')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Scatter Plot\nCorrelation: {pearson_corr:.3f}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Residuals plot
        plt.subplot(1, 2, 2)
        residuals = y - y_pred
        plt.scatter(y_pred, residuals, alpha=0.6, color='green')
        plt.axhline(y=0, color='red', linestyle='--')
        plt.xlabel('Predicted Y')
        plt.ylabel('Residuals')
        plt.title('Residuals Plot')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Add text at the bottom of the figure
        bottom_text = f"Analysis: {results['relationship_strength']} {results['direction']} relationship (p={pearson_p:.3f})"
        plt.figtext(0.5, 0.02, bottom_text, ha='center', va='bottom', fontsize=10, 
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray', alpha=0.7))
        
        # Add title if provided
        if title != "Some title":
            plt.suptitle(title, fontsize=14, y=0.95)
        
        plt.show()
    
    return results

# Example usage with different types of relationships
if __name__ == "__main__":
    
    # Example 1: Strong positive correlation
    print("Example 1: Strong Positive Correlation")
    print("=" * 50)
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [2.1, 4.2, 5.8, 8.1, 10.2, 12.1, 13.9, 16.1, 18.2, 20.1]
    results1 = quick_relationship_check(x1, y1,title="Strong Positive Correlation Example")
    
    print("\n" + "=" * 50)
    
    # Example 2: Negative correlation
    print("Example 2: Negative Correlation")
    print("=" * 50)
    x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
    results2 = quick_relationship_check(x2, y2,title="Negative Correlation Example")
    
    print("\n" + "=" * 50)
    
    # Example 3: No correlation (random data)
    print("Example 3: No Correlation")
    print("=" * 50)
    np.random.seed(42)
    x3 = np.random.randn(50)
    y3 = np.random.randn(50)
    results3 = quick_relationship_check(x3, y3, title="No Correlation Example")
    
    print("\n" + "=" * 50)
    
    # Example 4: Real-world example - Height vs Weight
    print("Example 4: Height vs Weight")
    print("=" * 50)
    # Sample data (height in inches, weight in pounds)
    height = [60, 62, 64, 66, 68, 70, 72, 74, 76, 65, 67, 69, 71, 73, 61, 63, 75]
    weight = [120, 130, 140, 150, 160, 170, 180, 190, 200, 145, 155, 165, 175, 185, 125, 135, 195]
    results4 = quick_relationship_check(height, weight, title="Height vs Weight Analysis" )
    
    print("\n" + "=" * 50)
    print("Analysis Complete!")
