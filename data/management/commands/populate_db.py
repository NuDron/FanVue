from datetime import datetime
from django.core.management import BaseCommand
from data.models import Album, Artist, Genre


class Command(BaseCommand):
    help = 'Creates initial data for database.'

    def handle(self, *args, **kwargs):
        artists = [
            "Guns N' Roses",
            "Linkin Park",
            "Korn",
            "Audioslave",
            "Chopin"
        ]
        # Create Genres
        rock = Genre.objects.create(genre='Rock')
        nu_metal = Genre.objects.create(genre='Nu Metal')
        classic = Genre.objects.create(genre='Classic')
        # Bundle genres
        genres = [rock, nu_metal, classic]
        # Prep genre feed
        bands_genres = [
            genres[0],
            genres[0],
            genres[1],
            genres[0],
            genres[2],
        ]
        bios = [
            "Guns N' Roses, often abbreviated as GNR, is an American hard rock band from Los Angeles",
            'Linkin Park is an American rock band from Agoura Hills, California.',
            'Korn (stylized as KoЯn) is an American nu metal band from Bakersfield, California, formed in 1993.',
            "Audioslave was an American rock supergroup formed in Glendale, California in 2001. The four-piece band consisted of Soundgarden's lead singer and rhythm guitarist Chris Cornell with Rage Against the Machine members Tom Morello (lead guitar), Tim Commerford (bass/backing vocals), and Brad Wilk (drums).",
            'Frédéric François Chopin, born Fryderyk Franciszek Chopin (1 March 1810 – 17 October 1849), was a Polish composer and virtuoso pianist of the Romantic period who wrote primarily for solo piano.',
        ]
        albums = [
            [['Chinese Democracy', '23-11-08'], ['The Spaghetti Incident?', '23-11-93']],
            [['Hybrid Theory', '24-10-00'], ['Meteora', '25-3-03'], ['Minutes to Midnight', '15-5-07']],
            [['Korn', '11-10-94'], ['Take a Look in the Mirror', '21-11-03']],
            [['Audioslave', '19-11-02'], ['Out of Exile', '23-5-05'], ['Revelations', '04-09-06']],
            [['Chopin Piano Concertos Nos 1 & 2', '12-2-78'], ['The Best of', '25-4-08']],
        ]
        for x in range(len(artists)):
            # 1 - Create Artist
            created_art = Artist.objects.create(name=artists[x], bio=bios[x], genre=bands_genres[x])
            art_albums = albums[x]
            print(30 * '-')
            print('Artist:', created_art)
            # 2 - Create Albums
            for album in art_albums:
                new_album = Album.objects.create(rel_artist=created_art,
                                                 name=album[0],
                                                 release_date=datetime.strptime(album[1], '%d-%m-%y'))
                print('Album: ', new_album)
