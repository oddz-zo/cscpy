import json
import requests
import pandas as pd

response = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&_fields=id,school.name,latest.student.size&api_key=EK7WRPhfY1HtxVtT6ZK2NNpqR1sAZcIhRe33GSKP")
data = response.json()
student_size = pd.DataFrame(data['results'])