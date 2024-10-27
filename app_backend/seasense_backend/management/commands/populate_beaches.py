# seasense_backend/management/commands/populate_beaches.py

from django.core.management.base import BaseCommand
from seasense_backend.models import Region, State

class Command(BaseCommand):
    help = 'Safely populate states with beaches in regions without duplicating entries'

    def handle(self, *args, **options):
        # Complete data structure for regions, states, and beaches
        data = {
            'West Coast': {
                'Gujarat': [
                    'Dumas Beach', 'Suvali Beach', 'Umbharat Beach', 'Dandi Beach', 'Dabhari beach',
                    'Diu Beach', 'Tithal Beach', 'Mandavi Beach', 'Khambhat Beach'
                ],
                'Maharashtra': [
                    'Aksa Beach', 'Alibaug Beach', 'Gorai Beach', 'Juhu beach', 'Manori Beach', 'Marvé Beach',
                    'Versova Beach', 'Agardanda Beach', 'Diveagar Beach', 'Ganpatipule Beach', 'Guhagar Beach',
                    'Kelwa Beach', 'Tarkarli Beach', 'Shivaji Park Beach', 'Anjarle Beach', 'Dapoli Beach',
                    'Dahanu Beach', 'Srivardhan beach', 'Kihim Beach', 'Mandwa Beach', 'Velneshwar Beach',
                    'Vengurla Beach', 'Bassein Beach', 'Bhandarpule Beach', 'Nagaon Beach', 'Revdanda Beach',
                    'Rewas Beach', 'Kashid Beach', 'Karde (Murud) Beach', 'Harihareshwar Beach', 'Bagmandla Beach',
                    'Kelshi Beach', 'Harnai Beach', 'Bordi Beach', 'Ratnagiri Beach', 'Awas Beach', 'Sasawne Beach',
                    'Malvan Beach'
                ],
                'Goa': [
                    'Agonda Beach', 'Arambol Beach', 'Benaulim Beach', 'Cavelossim Beach', 'Chapora Beach',
                    'Mandrem Beach', 'Palolem Beach', 'Varca Beach', 'Baga Beach', 'Candolim Beach',
                    'Calangute Beach', 'Colva Beach', 'Miramar Beach', 'Morjim Beach', 'Bambolim Beach',
                    'Cabo de rama Beach', 'Anjuna Beach', 'Utorda Beach', 'Majorda Beach', 'Betalbatim Beach',
                    'Sernabatim Beach', 'Cavelossim Beach', 'Mobor Beach', 'Betul Beach', 'Querim Beach',
                    'Kalacha Beach', 'Mandrem Beach', 'Ashvem Beach', 'Vagator Beach', 'Ozran Beach', 'Sinquerim Beach'
                ],
                'Karnataka': [
                    'Karwar Beach', 'Kudle beach', 'Panambur Beach', 'NITK Beach', 'Sasihithlu Beach',
                    'Maravanthe Beach', 'Tannirubhavi Beach', 'Malpe Beach', 'Murudeshwara Beach', 'Apsarakonda Beach',
                    'Om Beach', 'Kaup Beach', 'Kodi Beach', 'Someshwar Beach', 'St Mary\'s Island Beach',
                    'Mukka Beach', 'Ullal beach'
                ],
                'Kerala': [
                    'Cherai Beach', 'Fort Kochi beach', 'Kollam Beach', 'Marari beach', 'Muzhappilangad Beach',
                    'Payyambalam Beach', 'Shangumughom Beach', 'Varkala Beach', 'Kappad Beach', 'Bekal Beach',
                    'Thiruvambadi Beach', 'Kappil Beach'
                ],
            },
            'East Coast': {
                'West Bengal': [
                    'Henry Island Beach', 'Bakkhali sea beach', 'Frasergunj Sea Beach', 'Gangasagar Sea Beach',
                    'Junput beach', 'Bankiput Sea Beach', 'Mandarmani beach', 'Shankarpur Beach', 'Tajpur beach',
                    'Digha Sea Beach', 'Udaypur Sea Beach'
                ],
                'Odisha': [
                    'Talsari Beach', 'Dagara beach', 'Chandipur-on-sea', 'Gahirmatha Beach', 'Satabhaya beach',
                    'Pentha Sea Beach', 'Hukitola beach', 'Paradeep sea beach', 'Astaranga beach', 'Beleswar beach',
                    'Konark Beach', 'Chandrabhaga beach', 'Ramachandi beach', 'Puri Beach', 'Gopalpur-on-Sea'
                ],
                'Andhra Pradesh': [
                    'Sonpur Beach', 'Donkuru Beach', 'Nelavanka Beach', 'Kaviti Beach', 'Onturu Beach',
                    'Ramayyapatnam Beach', 'Baruva Beach', 'Battigalluru Beach', 'Shivasagar Beach', 'Nuvvalarevu Beach',
                    'Bheemili Beach', 'Rushikonda Beach', 'RK Beach', 'Yarada Beach', 'Gagavaram Beach'
                ],
                'Tamil Nadu': [
                    'Marina Beach', 'Edward Elliot\'s Beach', 'Golden Beach', 'Thiruvanmayur Beach', 'Covelong Beach',
                    'Mahabalipuram Beach', 'Pamban Beach', 'Dhanushkodi Beach', 'Velankanni Beach', 'Kanyakumari Beach',
                    'Vattakotai Beach', 'Sanguthurai Beach', 'Sengumal Beach', 'Thoothukudi Beach', 'Tiruchendur Beach'
                ],
            }
        }

        # Populate regions, states, and beaches without duplicating entries
        for region_name, states in data.items():
            region, _ = Region.objects.get_or_create(name=region_name)
            for state_name, beaches in states.items():
                beaches_text = ', '.join(beaches)
                state, created = State.objects.get_or_create(
                    name=state_name,
                    region=region,
                    defaults={'beaches': beaches_text}
                )
                
                if not created and state.beaches != beaches_text:
                    state.beaches = beaches_text  # Update beaches only if different
                    state.save()

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added {state_name} in {region_name} with beaches'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated beaches for {state_name} in {region_name}'))
