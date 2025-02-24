# CSV Message Pattern Analyzer

A Python tool for analyzing message patterns in large CSV datasets. This tool processes large files using chunk processing and provides chart visualizations of messaging patterns over time.

## Features
- Process large CSV files using chunk-based reading
- Interactive command-line interface for name input
- Analyze message patterns and frequencies
- Generate time-series visualizations
- Memory-efficient data processing

## Example Output
![Message Patterns Over Time](example_output/message_trends_Kyle.png)
*Example visualization showing message frequency over time*

## Installation
1. Clone the repository
```bash
git clone https://github.com/MarcellusL/CSV-Message-Pattern-Analyzer.git
```
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage
Run `python main.py` and follow the prompts to:
- Enter names to analyze
- View CSV preview
- Generate message statistics
- Create visualizations

## Technologies Used
- Python 3.10.11
- pandas for CSV processing
- matplotlib for visualization
- datetime for data handling and time-series analysis