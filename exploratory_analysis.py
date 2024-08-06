import pandas as pd
import matplotlib.pyplot as plt

# Paths to your data files
train_file = r'C:\MSCI_641\Project\train data\train.jsonl'
val_file = r'C:\MSCI_641\Project\val data\val.jsonl'
test_file = r'C:\MSCI_641\Project\test data\test.jsonl'
output_file = r'C:\MSCI_641\Project\data\roberta_task1.csv'

# Load data into DataFrames
train_data = pd.read_json(train_file, lines=True)
val_data = pd.read_json(val_file, lines=True)
test_data = pd.read_json(test_file, lines=True)

train_variables=train_data.columns
val_variables=val_data.columns
test_variables=test_data.columns

'''
print("Variables in Training Set")
for var_name in train_variables:
    print(var_name)
print()
    
print("Variables in Validation Set")
for var_name in val_variables:
    print(var_name)
print()
    
print("Variables in Test Set")
for var_name in test_variables:
    print(var_name)
'''
    
# Function to count words in a list of strings
def count_words(text_list):
    if isinstance(text_list, list):
        return sum(len(text.split()) for text in text_list)
    else:
        return 0  # Or handle accordingly if the format is unexpected

#Count Number fo Words in postText
train_data['postText_count'] = train_data['postText'].apply(count_words)
val_data['postText_count'] = val_data['postText'].apply(count_words)
test_data['postText_count'] = test_data['postText'].apply(count_words)

#Count Number fo Words in targetParagraphs
train_data['targetParagraphs_count'] = train_data['targetParagraphs'].apply(count_words)
val_data['targetParagraphs_count'] = val_data['targetParagraphs'].apply(count_words)
test_data['targetParagraphs_count'] = test_data['targetParagraphs'].apply(count_words)

#Count Number fo Words in targetTitle

# Convert each sample to a formatted list using list comprehension
train_lists = [[sample] for sample in train_data['targetTitle']]
train_data['targetTitle_list']=train_lists

val_lists = [[sample] for sample in val_data['targetTitle']]
val_data['targetTitle_list']=val_lists

test_lists = [[sample] for sample in test_data['targetTitle']]
test_data['targetTitle_list']=test_lists


train_data['targetTitle_count'] = train_data['targetTitle_list'].apply(count_words)
val_data['targetTitle_count'] = val_data['targetTitle_list'].apply(count_words)
test_data['targetTitle_count'] = test_data['targetTitle_list'].apply(count_words)

#Count Number for Words in spoiler (no spoiler column in test data)
train_data['spoiler_count'] = train_data['spoiler'].apply(count_words)
val_data['spoiler_count'] = val_data['spoiler'].apply(count_words)

#Save spoiler position Daat to Dataframe
train_spoiler_positions=train_data['spoilerPositions']
val_spoiler_positions=val_data['spoilerPositions']

'''
start_paragraphs = []
end_paragraphs = []
start_characters = []
end_characters = []

# Iterate through each sample's spoiler positions
for sample_idx, positions in enumerate(train_spoiler_positions, start=1):
    for spoiler_idx, pos in enumerate(positions, start=1):
        # Extract information from each spoiler position
        start_para = pos[0][0]  # Start paragraph
        start_char = pos[0][1]  # Start character
        end_para = pos[1][0]    # End paragraph
        end_char = pos[1][1]    # End character
        
        # Append to respective lists
        start_paragraphs.append(start_para)
        start_characters.append(start_char)
        end_paragraphs.append(end_para)
        end_characters.append(end_char)

# Create a DataFrame to store the extracted information
train_data = pd.DataFrame({
    'sp_start_paragraph': start_paragraphs,
    'sp_end_paragraph': end_paragraphs,
    'sp_start_character': start_characters,
    'sp_end_character': end_characters
    })

start_paragraphs = []
end_paragraphs = []
start_characters = []
end_characters = []

# Iterate through each sample's spoiler positions
for sample_idx, positions in enumerate(val_spoiler_positions, start=1):
    for spoiler_idx, pos in enumerate(positions, start=1):
        # Extract information from each spoiler position
        start_para = pos[0][0]  # Start paragraph
        start_char = pos[0][1]  # Start character
        end_para = pos[1][0]    # End paragraph
        end_char = pos[1][1]    # End character
        
        # Append to respective lists
        start_paragraphs.append(start_para)
        start_characters.append(start_char)
        end_paragraphs.append(end_para)
        end_characters.append(end_char)

# Create a DataFrame to store the extracted information
val_data = pd.DataFrame({
    'sp_start_paragraph': start_paragraphs,
    'sp_end_paragraph': end_paragraphs,
    'sp_start_character': start_characters,
    'sp_end_character': end_characters
    })
'''
'''
start_paragraphs = []
end_paragraphs = []
start_characters = []
end_characters = []

for idx, (tag, spoiler_positions) in enumerate(zip(train_data['tag'], train_data['spoilerPositions']), start=1):
    if tag == 'multi':
        for spoilers in train_data['spoilerPositions']:
            num_spoilers = len(spoilers)
        for i in range(num_spoilers):
            start_para = spoilers[i][0][0]
            start_char = spoilers[i][0][1]
            end_para = spoilers[i][1][0]
            end_char = spoilers[i][1][1]

            start_paragraphs.append(start_para)
            end_paragraphs.append(end_para)
            start_characters.append(start_char)
            end_characters.append(end_char)

        # Determine the number of spoilers
        num_spoilers = len(start_paragraphs)  # This will be the maximum number of spoilers among all samples

        # Initialize the DataFrame with empty values
        spoiler_df = pd.DataFrame()

        # Append columns for each spoiler
        for i in range(num_spoilers):
            col_prefix = f'Spoiler {i+1}'
            train_data[f'{col_prefix} Start Paragraph'] = start_paragraphs[i::num_spoilers]
            train_data[f'{col_prefix} End Paragraph'] = end_paragraphs[i::num_spoilers]
            train_data[f'{col_prefix} Start Character'] = start_characters[i::num_spoilers]
            train_data[f'{col_prefix} End Character'] = end_characters[i::num_spoilers]

    else:
        for spoiler_idx, pos in enumerate(train_data['spoilerPositions'], start=1):
            # Extract information from each spoiler position
            start_para = pos[0][0]  # Start paragraph
            start_char = pos[0][1]  # Start character
            end_para = pos[1][0]    # End paragraph
            end_char = pos[1][1]    # End character
            
            # Append to respective lists
            start_paragraphs.append(start_para)
            start_characters.append(start_char)
            end_paragraphs.append(end_para)
            end_characters.append(end_char)

    # Create a DataFrame to store the extracted information
    train_data = pd.DataFrame({
        'sp_start_paragraph': start_paragraphs,
        'sp_end_paragraph': end_paragraphs,
        'sp_start_character': start_characters,
        'sp_end_character': end_characters
        })
'''

columns_to_save= ['tags', 'postText_count', 'targetParagraphs_count', 'targetTitle_count', 'spoiler_count', 'spoilerPositions']
output_file = r'C:\MSCI_641\Project\data\train_size_metrics.csv'
train_data[columns_to_save].to_csv(output_file, index=False)

columns_to_save=['id', 'tags', 'postText_count', 'targetParagraphs_count', 'targetTitle_count', 'spoiler_count','spoilerPositions']
output_file = r'C:\MSCI_641\Project\data\val_size_metrics.csv'
val_data[columns_to_save].to_csv(output_file, index=False)

columns_to_save=['id','postText_count', 'targetParagraphs_count', 'targetTitle_count']
output_file = r'C:\MSCI_641\Project\data\test_size_metrics.csv'
test_data[columns_to_save].to_csv(output_file, index=False)

'''
# Plot Count of Words in postText as a Function of Tag

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True, tight_layout=True)
colors = {'phrase': 'blue', 'passage': 'green', 'multi': 'red'}

# Iterate through each tag and plot histograms
for i, tag in enumerate(['phrase', 'passage', 'multi']):
    tag_data = val_data[val_data['tags'] == tag]['postText_count']
    axs[i].hist(tag_data, bins=10, color=colors[tag], alpha=0.7)
    axs[i].set_title(f'Histogram for {tag.capitalize()}')
    axs[i].set_xlabel('postText_count')
    axs[i].set_xlim(0, 50)
    axs[i].set_ylim(0, 50)

# Show the plot
plt.show()
'''