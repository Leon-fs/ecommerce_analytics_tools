def perform_statistical_analysis(data):
    """
    Perform statistical analysis on the given dataset.
    
    Parameters:
    data (DataFrame): The input data for analysis.
    
    Returns:
    dict: A dictionary containing statistical insights.
    """
    insights = {
        'mean': data.mean(),
        'median': data.median(),
        'std_dev': data.std(),
        'correlation': data.corr()
    }
    return insights

def generate_insights(data):
    """
    Generate insights from the dataset.
    
    Parameters:
    data (DataFrame): The input data for generating insights.
    
    Returns:
    str: A summary of insights.
    """
    insights = perform_statistical_analysis(data)
    summary = f"Mean:\n{insights['mean']}\n\nMedian:\n{insights['median']}\n\nStandard Deviation:\n{insights['std_dev']}\n\nCorrelation:\n{insights['correlation']}"
    return summary

def main():
    """
    Main function to execute the analysis.
    """
    import pandas as pd
    
    # Load your data here
    # data = pd.read_csv('path_to_your_data.csv')
    
    # For demonstration, let's create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    
    insights = generate_insights(data)
    print(insights)

if __name__ == "__main__":
    main()