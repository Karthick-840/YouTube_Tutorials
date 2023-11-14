from icalendar import Calendar, Event
import pandas as pd
from datetime import datetime, timedelta



# Initialize the iCalendar
cal = Calendar()

for _,ROW in video_details.iterrows():
    
    # Define a start date and time
    start_date = pd.to_datetime(ROW['Start Date'] + ' ' + ROW['Start Time']) 
    
    playlist_data = create_video_data(ROW['Video Link'])
    if ROW['Title'] == 'hg':
        sort_by_runtime= True
    else:
        sort_by_runtime=False
        
    df = create_learning_group(playlist_data,int(ROW['Time to Spend']),sort_by_runtime)

    # Group the DataFrame by 'Category'
    df_dict = dict(iter(df.groupby('Group')))
    
    for group, dft in df_dict.items():
    # Calculate event duration from Run Time
        duration = timedelta(minutes=int(ROW['Time to Spend']))

        # Skip weekends (Saturday and Sunday)
        while start_date.weekday() >= 5:  # 5 and 6 correspond to Saturday and Sunday
            start_date += timedelta(days=1)

        # Create an event for each row
        event = Event()
        event.add('summary',ROW['Title']+ group)
        event.add('dtstart', start_date)
        event.add('dtend', start_date + duration)

        # Combine Video Link and Description in the description field
        event.add('description', dft)

        cal.add_component(event)

        # Increment start date for the next event
        start_date += timedelta(days=1)


return cal
