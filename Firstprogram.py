import pandas as pd
import io 
data = pd.read_csv(io.BytesIO(uploaded['Uploads_Business-employment-data_Business-employment-data-March-2023-quarter_Download-data_business-employment-data-march-2023-quarter-regional-council-revisions (1).csv'])) 

print(data)

print("Head")
data.head()

print("Tail")
data.tail()
