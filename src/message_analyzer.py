import pandas as pd

class MessageAnalyzer:
    '''
    This class is to analyze message patterns such a message count by person in a
    large csv dataset. This handles large files by using chunk processing. 
    '''

    def __init__(self, file_path):
        self.file_path = file_path
        self.chunk_size = 10000
        self.names = []
        self.get_names_input()

    def get_names_input(self):
        '''
        Prompts input to get name for analysis, will store name in self.names list
        '''

        print("Enter names to analyze (press Enter twice when done):")

        while True:
            name = input("Enter a name (or press enter to finish): ")
            if name == "":
                if self.names:
                    break
                else:
                    print("Error: No names were given. Please enter at least one name!")
                    continue
            self.names.append(name)

        print(f"Starting 'messages received by' search for: {', '.join(self.names)}\n")

    def analyze_csv(self, nrows = 10):
        '''
        Preview CSV file contents with customizable row count. 
        
        Prompts user to enter number of rows to view (max 100).
        Shows column names and data preview.

        Returns:
            tuple: (list of column names, number of rows read)
        '''

        user_input = input("Would you like to specify the number of rows to preview? (yes/Enter to skip): ").lower()

        if user_input == 'yes' or user_input == 'y':
            while True:
                try: 
                    nrows = input("Enter number of rows to preview (max 100): ")
                    if nrows.strip() == "":
                        print(f"Using default value: {nrows} rows")
                        break
                    nrows = int(nrows)
                    if nrows <= 0:
                        print("Please enter a positive number")
                        continue
                    if nrows > 100:
                        print("Maximum preview is 100 rows. Setting to 100.")
                        nrows = 100 
                    break
                except ValueError:
                    print("Please enter a valid number")
        else:
            nrows = 10
            print(f"Using default value: {nrows} rows")

        df = pd.read_csv(self.file_path, nrows=nrows)
        column_names = df.columns.tolist()

        print(f"\nColumns found: {column_names}")
        print(f"\nFirst {nrows} rows:")
        print(df)

        total_rows = len(df)
        print(f"\nRows read: {total_rows}")

        return column_names, total_rows
    
    def count_messages_received(self):
        '''
        Count total messages recevied by each person

        Processes files in chunk to handle large datasets.
        Shows progress

        Returns: 
            dict: A dictionary mapping names to message counts
        '''

        results = {} # Store results for each person

        for person_name in self.names:
            print(f"Analysis search for: {person_name}")
            messages_received = 0 
            chunk_count = 0 

            # Process file in chunks to handle larges files efficiently
            for chunk in pd.read_csv(self.file_path, chunksize=self.chunk_size):
                chunk_count += 1
                if chunk_count % 10 == 0:
                    print(f"Processing chunk {chunk_count} for {person_name}")
            
                # Filter messages where person is the receiver
                received = chunk[chunk['Receiver'] == person_name]
                messages_received += len(received)
        
            print(f"\nSearch completed for {person_name} (processed {chunk_count} chunks):")
            print(f"Messages received by {person_name}: {messages_received}")
            print("-" * 50)  # Separator line
            results[person_name] = messages_received
        return results

    def analyze_message_patterns(self):
        '''
        Analyze message patterns for each person inserted from self.names list

        Collects:
            - Total messages received
            - Messages by date
            - Messages by sender

        Returns: 
            dict: A dictionary containing pattern analysis for each person
        '''

        all_patterns = {} 

        print("Starting analyze message patterns\n")
        for person_name in self.names:
            messages = {
                'total_received': 0,
                'by_date': {},
                'by_sender': {},
                'most_active_hour': None
            }

            for chunk in pd.read_csv(self.file_path, chunksize=self.chunk_size, usecols=['Receiver', 'Sender', 'Date']):
                # Filter messages for current person
                received = chunk[chunk['Receiver'] == person_name]
                
                messages['by_date'].update(received['Date'].value_counts().to_dict())
                messages['by_sender'].update(received['Sender'].value_counts().to_dict())
                messages['total_received'] += len(received)
            all_patterns[person_name] = messages
        return all_patterns