###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
from ignore import pd; import pandas as pd                                        #
###############################################################

# Let's say I have a dictionary that maps guitar types
# to their colors
guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

# Create a new Series object, passing in the guitars_dict dictionary as the data source.
# Assign the resulting Series to a "guitars" variable.
guitars = pd.Series(guitars_dict)

# Access the value for the index position of 0 within the "guitars" Series.
# Assign the value to a "fender_color" variable.
guitars[0]
fender_color = guitars[0]
# Access the value for the index label of "Gibson Les Paul" in the "guitars" Series.
# Assign the value to a "gibson_color" variable.
guitars['Gibson Les Paul']
gibson_color = guitars['Gibson Les Paul']
# Access the value for the index label of "ESP Eclipse" in the "guitars" Series.
# Assign the value to a "esp_color" variable.
guitars['ESP Eclipse']
esp_color = guitars['ESP Eclipse']