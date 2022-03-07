def wind_speed_categories(speed):
    if speed < 1:
        return "Calm"
    elif 1 >= speed < 3:
        return "Light Air"
    elif 3 >= speed < 7:
        return "Light Breeze"
    elif 7 >= speed < 12:
        return "Gentle Breeze"
    elif 12 >= speed < 18:
        return "Moderate Breeze"
    elif 18 >= speed < 24:
        return "Fresh Breeze"
    elif 24 >= speed < 31:
        return "Strong Breeze"
    elif 31 >= speed < 38:
        return "Near Gale"
    elif 38 >= speed < 46:
        return "Gale"
    elif 46 >= speed < 54:
        return "Strong Gale"
    elif 54 >= speed < 63:
        return "Whole Gale"
    elif 63 >= speed < 75:
        return "Storm Force"
    else:
        return "Hurricane"
