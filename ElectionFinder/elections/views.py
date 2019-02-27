from django.shortcuts import render
from .utils import create_dw_api
import requests
import json

from .forms import ElectionForm

# Create your views here.

def election_form(request):
    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data
            state = address['state'].strip().lower()
            place = address['city'].strip().replace(" ", "_").lower()

            r = requests.get(create_dw_api(state, place),headers={'Accept': 'application/json' })
            if r.status_code == 200:
                r_text = r.text
                r_jsonify = json.loads(r_text)

                if r_jsonify:
                    r_dict = r_jsonify[0]

                    context = {
                        'state': state,
                        'place': place,
                        'message': 'Whoo hooo! There is an election in ',
                        'date': 'Here is the date:',
                        'election_info': r_dict['date'][:10],
                    }
                else:
                    context = {
                    'sorry' : 'Sorry, no upcoming elections in your area',
                }

            else:
                context = {
                    'sorry' : 'Sorry, those are not valid places',
                }
            return render(request, 'elections/result.html', context)
    else:
        form = ElectionForm()

    return render(request, 'elections/index.html', {'form': form})

