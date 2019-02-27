from django.shortcuts import render
from .utils import create_dw_api
import requests

from .forms import ElectionForm

# Create your views here.

def election_form(request):
    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data
            state = address['state'].strip().lower()
            place = address['city'].strip().replace(" ", "_").lower()

            r = requests.get(create_dw_api(state, place))
            s = r.status_code

            context = {
                'state': state,
                'place': place,
                's': s,
            }
            return render(request, 'elections/result.html', context)
    else:
        form = ElectionForm()

    return render(request, 'elections/index.html', {'form': form})

