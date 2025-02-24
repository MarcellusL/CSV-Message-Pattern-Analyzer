from src.message_analyzer import MessageAnalyzer
from src.chart_visualizer import ChartVisualizer

def main():
    '''
    Main function to run the message pattern analysis program.
    Features data loading, analysis, and chart visualization.
    '''

    file_path = "Fake Big Data.csv"
    analyzer = MessageAnalyzer(file_path)

    # Count messages received by each person
    # Results stored as dictionary: {name: message_count}
    results = analyzer.count_messages_received()

    print("\nPreviewing CSV data:")
    analyzer.analyze_csv()

    # Analyze detailed message patterns
    # Includes message counts by date and sender
    patterns = analyzer.analyze_message_patterns()

    # Create and save visualization charts
    # Generates time-series plots for each person
    chart_visualizer = ChartVisualizer()
    chart_visualizer.create_chart_visualization(patterns)

if __name__ == "__main__": 
    main()