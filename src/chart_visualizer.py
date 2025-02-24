import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

class ChartVisualizer:
        @staticmethod
        def create_chart_visualization(all_patterns):
            '''
            Create chart visualization of message patterns

            Paramenter:
                all_patterns (dict): Pattern data from analyze_message_patterns

            Saves plots as PNG files name 'message_trends_{person_name}.png'
            '''

            print("Creating chart visualization")
            for person_name, messages_data in all_patterns.items():
                # Convert dates from strings to datetime objects for plotting
                dates = [datetime.strptime(date, '%Y-%m-%d') for date in messages_data['by_date'].keys()]
                counts = list(messages_data['by_date'].values())

                plt.figure(figsize=(12, 6))
                plt.plot(dates, counts)

                # Format x-axis to show dates properly
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                plt.gcf().autofmt_xdate() # Rotate date labels for better readability

                # Add chart labels and grid
                plt.title('Messages Over Time')
                plt.xlabel('Date')
                plt.ylabel('Number of Messages')
                plt.grid(True) 

                # Save the chart 
                plt.savefig(f'message_trends_{person_name}.png')
                plt.close()
                print(f"Created visualization chart for {person_name}")