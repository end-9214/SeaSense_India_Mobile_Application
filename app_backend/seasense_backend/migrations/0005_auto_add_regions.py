from django.db import migrations

def create_regions_with_states(apps, schema_editor):
    Region = apps.get_model('seasense_backend', 'Region')
    State = apps.get_model('seasense_backend', 'State')

    # Delete any existing regions with the same names to avoid duplicate issues
    Region.objects.filter(name__in=['East Coast', 'West Coast']).delete()

    # Define regions with specific IDs
    regions = [
        {'id': 1, 'name': 'East Coast'},
        {'id': 2, 'name': 'West Coast'}
    ]

    # Define states and beaches for each region
    states_data = {
        1: [  # East Coast
            {'name': 'West Bengal', 'beaches': 'Henry Island Beach, Bakkhali Beach, Frasergunj Beach, Gangasagar Beach, Junput Beach, Bankiput Beach, Mandarmani Beach, Shankarpur Beach, Tajpur Beach, Digha Beach, Udaypur Beach'},
            {'name': 'Odisha', 'beaches': 'Puri Beach, Talsari Beach, Dagara Beach, Chandipur-on-sea, Gahirmatha Beach, Satabhaya Beach, Pentha Sea Beach, Hukitola Beach, Paradeep Sea Beach, Astaranga Beach, Beleswar Beach, Konark Beach, Chandrabhaga Beach, Ramachandi Beach, Satpada Beach, Parikud Beach, Ganjam Beach, Aryapalli Beach, Gopalpur-on-Sea, Dhabaleshwar Beach, Sonapur Beach'},
            {'name': 'Andhra Pradesh', 'beaches': 'Sonpur Beach, Donkuru Beach, Nelavanka Beach, Kaviti Beach, Onturu Beach, Ramayyapatnam Beach, Baruva Beach, Battigalluru Beach, Shivasagar Beach, Nuvvalarevu Beach, Kalingapatnam Beach, Rushikonda Beach, RK Beach, Yarada Beach, Manginapudi Beach, Suryalanka Beach, Vodarevu Beach, Mypadu Beach'},
            {'name': 'Tamil Nadu', 'beaches': 'Marina Beach, Edward Elliot\'s Beach, Golden Beach, Thiruvanmayur Beach, Silver Beach, Covelong Beach, Mahabalipuram Beach, Olaikuda Beach, Pamban Beach, Dhanushkodi Beach, Velankanni Beach, Kanyakumari Beach, Vattakotai Beach, Thoothukudi Beach, Tiruchendur Beach, Poompuhar Beach'}
        ],
        2: [  # West Coast
            {'name': 'Gujarat', 'beaches': 'Dumas Beach, Suvali Beach, Umbharat Beach, Dandi Beach, Dabhari Beach, Diu Beach, Tithal Beach, Mandavi Beach, Khambhat Beach'},
            {'name': 'Maharashtra', 'beaches': 'Aksa Beach, Alibaug Beach, Gorai Beach, Juhu Beach, Manori Beach, Marvé Beach, Versova Beach, Agardanda Beach, Diveagar Beach, Ganpatipule Beach, Guhagar Beach, Kelwa Beach, Tarkarli Beach, Shivaji Park Beach, Anjarle Beach, Dapoli Beach, Dahanu Beach, Srivardhan Beach, Kihim Beach, Mandwa Beach, Velneshwar Beach, Vengurla Beach, Bassein Beach, Bhandarpule Beach, Nagaon Beach, Revdanda Beach, Rewas Beach, Kashid Beach, Karde Beach, Harihareshwar Beach, Bagmandla Beach, Kelshi Beach, Harnai Beach, Bordi Beach, Ratnagiri Beach, Awas Beach, Sasawne Beach, Malvan Beach'},
            {'name': 'Goa', 'beaches': 'Agonda Beach, Arambol Beach, Benaulim Beach, Cavelossim Beach, Chapora Beach, Mandrem Beach, Palolem Beach, Varca Beach, Baga Beach, Candolim Beach, Calangute Beach, Colva Beach, Miramar Beach, Morjim Beach, Bambolim Beach, Cabo de Rama Beach, Anjuna Beach, Utorda Beach, Majorda Beach, Betalbatim Beach, Sernabatim Beach, Cavelossim Beach, Mobor Beach, Betul Beach, Querim Beach, Kalacha Beach, Mandrem Beach, Ashvem Beach, Vagator Beach, Ozran Beach, Sinquerim Beach, Coco Beach, Kegdole Beach, Caranzalem Beach, Dona Paula Beach, Vaiguinim Beach, Siridao Beach, Bogmalo Beach, Baina Beach, Hansa Beach, Hollant Beach, Cansaulim Beach, Velsao Beach, Canaiguinim Beach, Kakolem Beach, Dharvalem Beach, Cola Beach, Patnem Beach, Rajbag Beach, Talpona Beach, Galgibag Beach, Polem Beach, Pebble Beach'},
            {'name': 'Karnataka', 'beaches': 'Karwar Beach, Kudle Beach, Panambur Beach, NITK Beach, Sasihithlu Beach, Maravanthe Beach, Tannirubhavi Beach, Malpe Beach, Murudeshwara Beach, Apsarakonda Beach, Om Beach, Kaup Beach, Kodi Beach, Someshwar Beach, St Mary\'s Island Beach, Mukka Beach, Ullal Beach'},
            {'name': 'Kerala', 'beaches': 'Cherai Beach, Fort Kochi Beach, Kollam Beach, Marari Beach, Meenkunnu Beach, Muzhappilangad Beach, Payyambalam Beach, Shangumughom Beach, Varkala Beach, Kappad Beach, Bekal Beach, Thiruvambadi Beach, Kappil Beach'}
        ]
    }

    # Create or update regions
    for region_data in regions:
        region, created = Region.objects.update_or_create(
            id=region_data['id'],
            defaults={'name': region_data['name']}
        )

    # Create states and beaches for each region
    for region_id, states in states_data.items():
        region = Region.objects.get(id=region_id)
        for state_data in states:
            State.objects.update_or_create(
                name=state_data['name'],
                region=region,
                defaults={'beaches': state_data['beaches']}
            )

class Migration(migrations.Migration):
    dependencies = [
        ('seasense_backend', '0004_auto_20241028_0207'),
    ]

    operations = [
        migrations.RunPython(create_regions_with_states),
    ]
