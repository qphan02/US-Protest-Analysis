import pandas as pd
import numpy as np
import ollama
import os

def get_protest_message_llama(text):
    prompt = f"""
    What is one central idea or message of the protest in the follow text. 
    The answer should be one keyword only, like "Abortion", "Climate Change", "Gun Regulations", "Pro-choice", "Police Brutality", "Pro-Trump", "Coronavirus Mandates", "Anti-War", "Workes' Rights", "Higher Wages", "LGBTQ+", "Women's Right", "Racial Justice", "Anti-Mask", "Budget Cut", etc.
    
    Text:
    {text}
    """
    # extract the protest message from the response
    count = 0
    while True:
        protest_message = ollama.generate(model="llama2", prompt=prompt)["response"]
        protest_message = protest_message.rsplit("\n",-1)[-1]
        protest_message = protest_message.rsplit(":",-1)[-1]
        protest_message = protest_message.strip()
        protest_message = protest_message.strip("*")
        protest_message = protest_message.strip('"')
        protest_message = protest_message.strip()
        
        # sometime the model returns "Protest" as the protest message, which is not helpful
        # so we will try again a few times
        if protest_message != "Protest" or count > 5:
            break
        count += 1
    print(protest_message)
    return protest_message

df = pd.read_csv('North_America-United_States.csv')
df.set_index('data_id', inplace=True)

# extract the notes from the first comma to the last period
notes = df['notes'].str.extract(r',([^.]*)\.')[0]

# check if protest_messages folder exists
# create one if it does not
if not os.path.exists('./protest_messages'):
    os.makedirs('./protest_messages')

# define the number of chunks
num_chunks = 100

# split the DataFrame into chunks
chunks = np.array_split(notes, num_chunks)

# if the process is interrupted, set the skip variable to the index of the last chunk processed
skip = 0

for i, chunk in enumerate(chunks):
    if i < skip:
        continue
    
    # apply the function to the chunk
    chunk['protest_message'] = chunk.apply(get_protest_message_llama)
    
    # save the chunk to a unique file
    chunk["protest_message"].to_csv(f'./protest_messages/North_America-United_States_protest_{i}.csv')