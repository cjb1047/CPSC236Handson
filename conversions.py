def ftm(feet):
    meters = feet * 0.3048
    meters = round(meters, 2)
    return meters

def mtf(meters):
    feet = meters / 0.3048
    feet = round(feet, 2)
    return feet