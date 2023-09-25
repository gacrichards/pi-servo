def map_value(value, in_min, in_max, out_min, out_max):
    # Calculate the proportion of the input value in the input range
    proportion = (value - in_min) / (in_max - in_min)
    
    # Map the proportion to the output range
    mapped_value = out_min + (proportion * (out_max - out_min))
    
    return mapped_value