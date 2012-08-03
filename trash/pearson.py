from math import sqrt

def pearson(pin1_number, pin2_number):
    """Produces a metric of similarity between movies, 1.0 means the movies are
    essentially identical, -1.0 means they are complete opposites on the
    scale.
    
    @pin1_number -- A dictionary of pin occurences, of the format {"user_id": number, "user_id2": number}
    @pin2_number -- A dictionary of pin occurences, of the format {"user_id": number, "user_id2": number}

    @returns -- float"""
    common_pinners = []

    for pin in pin1_number:
        if pin in pin2_number:
            common_pinners.append(pin)
    
    if len(common_pinners) == 0:
        return 0

    pin1_sum = sum(pin1_number[pinner] for pinner in common_pinners)
    pin2_sum = sum(pin2_number[pinner] for pinner in common_pinners)

    pin1_sum_square  = sum([pow(pin1_number[pinner], 2) for pinner in common_pinners])
    pin2_sum_square  = sum([pow(pin2_number[pinner], 2) for pinner in common_pinners])

    product_sum = sum([pin1_number[pinner] * pin2_number[pinner] for pinner in common_pinners])

    # Calculate the pearson score, r
    num_pinners = len(common_pinners)
    num = product_sum - ((pin1_sum * pin2_sum)/num_pinners)
    den = sqrt((pin1_sum_square - pow(pin1_sum, 2) / num_pinners) * (pin2_sum_square - pow(pin2_sum, 2)/num_pinners))

    if den == 0:
        return 0

    return num/den


if __name__ == "__main__":

    pins = {
        "janew" : {"tumblr": 154, "wanelo": 100, "onekingslane": 80},
        "michellelsun" : {"polyvore": 7, "bettycrocker": 8, "onekingslane":6}
        "caitlin_cawley" : {"hometalk":43, "blogspot": 23}
    }
        # how to call it in mongoDB

    # movies = { 
    #     "Wall-E": { "Ebert": 5.0, "Siskel": 4.0, "LeBron": 5.0, "Moses": 3.7, "Shaq": 4.5, "Bartholomew": 4.8 },
    #     "The Hangover": { "Ebert": 4.5, "Siskel": 4.2, "LeBron": 4.8, "Moses": 3.5, "Shaq": 4.6, "Bartholomew": 4.7 },
    #     "The Notebook": { "Ebert": 1.0, "Siskel": 4.5, "LeBron": 3.2, "Moses": 5.7, "Shaq": 0.5, "Bartholomew": 1.2 } }

    print pearson_similarity(pins["janew"], pins["michellelsun"])
    print pearson_similarity(pins["michellelsun"], pins["caitlin_cawley"])
    print pearson_similarity(pins["Wall-E"], pins["The Hangover"])