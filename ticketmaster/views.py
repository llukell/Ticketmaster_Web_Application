from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from .models import FavoriteEvents
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import FavoriteEvents


def index(request):
    context = {'events': []}  # Initialize events dictionary with an empty list

    if request.method == 'POST':
        genre = request.POST['category']
        hood = request.POST['location']
        events_returned = find_events(genre, hood)

        if events_returned is None:
            messages.error(request, 'The server encountered an issue while fetching data. Please try again later.')
        else:
            try:
                event_amount = events_returned['page']['totalElements']
                events = events_returned['_embedded']['events']
                event_lists = []
                for event in events:
                    event_number = event['id']
                    event_name = event['name']
                    thumbnail = event['images'][7]['url']
                    venue_name = event['_embedded']['venues'][0]['name']
                    venue_city = event['_embedded']['venues'][0]['city']['name']
                    venue_state = event['_embedded']['venues'][0]['state']['name']
                    venue_address = event['_embedded']['venues'][0]['address']['line1']
                    iso_date = event['dates']['start']['localDate']
                    local_time = event['dates']['start'].get('localTime', '')
                    close_up = event['url']

                    to_date = datetime.fromisoformat(
                        iso_date)  # not sure if I want to keep like this, but this is the time conversion

                    date = to_date.strftime("%B %d, %Y")
                    if local_time != '':
                        time_obj = datetime.strptime(local_time, "%H:%M:%S")
                        time = time_obj.strftime("%I:%M %p")

                    event_details = {
                        'is_favorite': FavoriteEvents.objects.filter(entry_model_id=event['id']).exists(),
                        'event_total': event_amount,
                        'event_id': event_number,
                        'event_name': event_name,
                        'thumbnail': thumbnail,
                        'venue_name': venue_name,
                        'venue_city': venue_city,
                        'venue_state': venue_state,
                        'venue_address': venue_address,
                        'date': date,
                        'time': time,
                        'close_up': close_up,
                    }

                    event_lists.append(event_details)  # append to events_list

                context = {
                    'events': event_lists,
                    'total_events': event_amount  # add event_amount separate
                }

            except KeyError:
                messages.error(request, "No matching search results. Check spelling and try again")
                print("api key contains an error")

    return render(request, 'ticketmaster.html', context)


def find_events(genre, hood):  # had to add the results into the url, was having trouble other way
    try:
        key = 'uPAY0ZLvbyr3E6B2IYlLOphfnT10KClv'

        api_url = ('https://app.ticketmaster.com/discovery/v2/events.json?keyword=' + genre + '&city=' + hood +
                   '&sort=date,asc&apikey=' + key)

        api_results = requests.get(api_url)

        results = api_results.json()

        return results

    except requests.exceptions.RequestException as e:
        print(f"Request failed:{e}")

        return None


@require_POST
def create_favorite(request):  # Create Favorite from AJAX POST

    event_id = request.POST.get('event_id')
    event_name = request.POST.get('event_name')
    thumbnail = request.POST.get('thumbnail')
    venue_name = request.POST.get('venue_name')
    venue_city = request.POST.get('venue_city')
    venue_state = request.POST.get('venue_state')
    venue_address = request.POST.get('venue_address')
    date = request.POST.get('date')
    time = request.POST.get('time')
    close_up = request.POST.get('close_up')

    already_favorite = FavoriteEvents.objects.filter(entry_model_id=event_id).first()
    if already_favorite:
        print('already favorite')

    else:
        FavoriteEvents.objects.create(

            entry_model_id=event_id,
            event=event_name,
            venue=venue_name,
            venueCity=venue_city,
            venueState=venue_state,
            venueAddress=venue_address,
            date=date,
            time=time,
            thumbnailURL=thumbnail,
            link=close_up,
            is_favorited=True
        )

        return JsonResponse({'status': 'success', 'message': 'Favorite created'})


def view_favorites(request):  # Read Favorites elements from model to display on favorites.html

    favorites = FavoriteEvents.objects.all()
    favorites_amount = FavoriteEvents.objects.all().count()
    context = {'favorites': favorites,
               'favorites_amount':favorites_amount}
    return render(request, 'favorites.html', context)


def update_favorite_attending(request):  # Update if user is going or not, boolean true/false
    if request.method == 'POST':

        attending_event_id = request.POST.get('event_id')
        print(attending_event_id)
        selected = FavoriteEvents.objects.filter(entry_model_id=attending_event_id).first()

        if selected:
            selected.is_going = not selected.is_going
            selected.save()
            return JsonResponse({'status': 'success', 'message': 'Favorite attending'})


def delete_favorite(request):  # delete favorite: get element id, delete (user can un-delete, if page is not refreshed)
    if request.method == 'POST':
        favorite_id = request.POST.get('event_id')
        favorite = FavoriteEvents.objects.filter(entry_model_id=favorite_id).first()

        if favorite:
            favorite.delete()
            return JsonResponse({'status': 'success', 'message': 'Favorite deleted'})
