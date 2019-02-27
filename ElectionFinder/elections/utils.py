
def create_dw_api(state, city):

    base = 'https://api.turbovote.org/elections/upcoming?district-divisions='
    state_param = 'ocd-division/country:us/state:' + state + ','
    city_param = 'ocd-division/country:us/state:' + state + '/place:' + city
    full_api = base + state_param + city_param

    return(full_api)