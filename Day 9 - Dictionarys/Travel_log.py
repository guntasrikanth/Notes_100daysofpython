travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,visits,cities):
    travel_log.append(
    {
        "country": country,
        "visits": visits,
        "cities": cities
    }
)
    

"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
