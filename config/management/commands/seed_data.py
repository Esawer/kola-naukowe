import datetime

from django.core.management.base import BaseCommand
from django.db import transaction

from config.models import Activity, Club

CLUBS = [
    {
        "name": "Klub Szachowy",
        "desc": "Klub dla graczy na każdym poziomie: od pierwszych partii po turnieje klubowe.",
        "leader": "Marek Zieliński",
    },
    {
        "name": "Klub Fotograficzny",
        "desc": "Wspólne plenery, przeglądy zdjęć i warsztaty obróbki.",
        "leader": "Julia Wrona",
    },
    {
        "name": "Klub Filmowy",
        "desc": "Seanse z dyskusją, warsztaty montażu i konkursy krótkich form.",
        "leader": "Tomasz Bąk",
    },
    {
        "name": "Klub Górski",
        "desc": "Wycieczki, szkolenia z bezpieczeństwa i spotkania o sprzęcie.",
        "leader": "Katarzyna Lis",
    },
    {
        "name": "Klub Debat Oksfordzkich",
        "desc": "Treningi argumentacji i debaty z publicznością.",
        "leader": "Paweł Nowicki",
    },
]

ACTIVITIES = [
    # Klub Książki
    {
        "club": "Klub Książki",
        "name": "Dyskusja: literatura faktu",
        "desc": "Rozmowa o trzech reportażach wybranych przez klubowiczów.",
        "location": "Biblioteka UKEN, sala 12",
        "custodian": "Anna Kowalska",
        "limit": 25,
        "current_participants": 25,
        "additional_info": "Przynieś własną książkę na wymianę.",
        "date": datetime.date(2026, 10, 14),
        "category": Activity.Category.SPOTKANIE,
    },
    {
        "club": "Klub Książki",
        "name": "Warsztat pisania recenzji",
        "desc": "Praktyczne ćwiczenia z redakcji krótkiej recenzji książki.",
        "location": "Sala 204",
        "custodian": "Anna Kowalska",
        "limit": 15,
        "current_participants": 9,
        "additional_info": "Wymagany laptop.",
        "date": datetime.date(2026, 12, 3),
        "category": Activity.Category.WARSZTAT,
    },
    {
        "club": "Klub Książki",
        "name": "Wycieczka do Biblioteki Jagiellońskiej",
        "desc": "Zwiedzanie zbiorów specjalnych i czytelni z przewodnikiem.",
        "location": "Kraków, ul. Oleandry 3",
        "custodian": "Anna Kowalska",
        "limit": 20,
        "current_participants": 4,
        "additional_info": "Zbiórka o 8:15 przed głównym wejściem.",
        "date": datetime.date(2027, 1, 20),
        "category": Activity.Category.WYCIECZKA,
    },
    # Klub Hazardu
    {
        "club": "Klub Hazardu",
        "name": "Matematyka ruletki",
        "desc": "Wartość oczekiwana, house edge i dlaczego systemy nie działają.",
        "location": "Aula B",
        "custodian": "Robert Mazur",
        "limit": 40,
        "current_participants": 33,
        "additional_info": "",
        "date": datetime.date(2026, 11, 18),
        "category": Activity.Category.WYKLAD,
    },
    {
        "club": "Klub Hazardu",
        "name": "Turniej blackjacka (gra na żetony)",
        "desc": "Turniej towarzyski z podstawową strategią, bez prawdziwych stawek.",
        "location": "Sala 118",
        "custodian": "Robert Mazur",
        "limit": 16,
        "current_participants": 16,
        "additional_info": "Zapisy zamknięte, lista rezerwowa mailowo.",
        "date": datetime.date(2026, 12, 11),
        "category": Activity.Category.KONKURS,
    },
    # Klub Forex
    {
        "club": "Klub Forex",
        "name": "Analiza techniczna od zera",
        "desc": "Świece, poziomy wsparcia i oporu oraz proste formacje.",
        "location": "Sala komputerowa 3",
        "custodian": "Michał Duda",
        "limit": 30,
        "current_participants": 30,
        "additional_info": "Konto demo zalecane, nie wymagane.",
        "date": datetime.date(2026, 10, 28),
        "category": Activity.Category.WARSZTAT,
    },
    {
        "club": "Klub Forex",
        "name": "Konkurs demo-traderów",
        "desc": "Miesięczny konkurs na koncie demo, ranking według zwrotu.",
        "location": "Online",
        "custodian": "Michał Duda",
        "limit": 25,
        "current_participants": 12,
        "additional_info": "Regulamin w opisie wydarzenia.",
        "date": datetime.date(2026, 11, 27),
        "category": Activity.Category.KONKURS,
    },
    {
        "club": "Klub Forex",
        "name": "Spotkanie z praktykiem rynku FX",
        "desc": "Gość z biura maklerskiego o zarządzaniu ryzykiem w praktyce.",
        "location": "Aula A",
        "custodian": "Michał Duda",
        "limit": 50,
        "current_participants": 7,
        "additional_info": "Pytania można wysyłać wcześniej przez formularz klubu.",
        "date": datetime.date(2027, 1, 15),
        "category": Activity.Category.SPOTKANIE,
    },
    # Klub Szachowy
    {
        "club": "Klub Szachowy",
        "name": "Turniej błyskawiczny 5+3",
        "desc": "Siedem rund systemem szwajcarskim, tempo 5 minut plus 3 sekundy.",
        "location": "Sala 210",
        "custodian": "Marek Zieliński",
        "limit": 32,
        "current_participants": 32,
        "additional_info": "Potrzebny własny zegar lub aplikacja.",
        "date": datetime.date(2026, 11, 16),
        "category": Activity.Category.KONKURS,
    },
    {
        "club": "Klub Szachowy",
        "name": "Warsztat debiutów otwartych",
        "desc": "Analiza partii klubowiczów i typowe błędy w otwarciach.",
        "location": "Sala 210",
        "custodian": "Marek Zieliński",
        "limit": 12,
        "current_participants": 5,
        "additional_info": "",
        "date": datetime.date(2026, 12, 2),
        "category": Activity.Category.WARSZTAT,
    },
    {
        "club": "Klub Szachowy",
        "name": "Symultana z mistrzem klubowym",
        "desc": "Jeden gracz przeciw dwudziestu czterem szachownicom.",
        "location": "Aula B",
        "custodian": "Marek Zieliński",
        "limit": 24,
        "current_participants": 11,
        "additional_info": "Zapisuje się tylko grający, publiczność bez limitu.",
        "date": datetime.date(2027, 1, 9),
        "category": Activity.Category.SPOTKANIE,
    },
    # Klub Fotograficzny
    {
        "club": "Klub Fotograficzny",
        "name": "Wykład: światło w portrecie",
        "desc": "Rodzaje światła, softboxy i praca z modelką na planie.",
        "location": "Sala 105",
        "custodian": "Julia Wrona",
        "limit": 35,
        "current_participants": 18,
        "additional_info": "",
        "date": datetime.date(2026, 11, 21),
        "category": Activity.Category.WYKLAD,
    },
    {
        "club": "Klub Fotograficzny",
        "name": "Plener fotograficzny: Stare Miasto",
        "desc": "Trzygodzinny plener z przeglądem zdjęć po powrocie.",
        "location": "Rynek Główny, pod wieżą ratuszową",
        "custodian": "Julia Wrona",
        "limit": 15,
        "current_participants": 15,
        "additional_info": "Zabierz statyw, jeśli masz.",
        "date": datetime.date(2026, 12, 13),
        "category": Activity.Category.WYCIECZKA,
    },
    # Klub Filmowy
    {
        "club": "Klub Filmowy",
        "name": "Seans: kino noir",
        "desc": "Pokaz dwóch klasycznych filmów noir z krótkim wstępem.",
        "location": "Sala kinowa 0.4",
        "custodian": "Tomasz Bąk",
        "limit": 40,
        "current_participants": 26,
        "additional_info": "Wstęp po okazaniu legitymacji studenckiej.",
        "date": datetime.date(2026, 10, 22),
        "category": Activity.Category.SPOTKANIE,
    },
    {
        "club": "Klub Filmowy",
        "name": "Warsztat montażu w DaVinci",
        "desc": "Cięcie, przejścia i podstawy korekcji koloru w darmowej wersji.",
        "location": "Sala komputerowa 2",
        "custodian": "Tomasz Bąk",
        "limit": 14,
        "current_participants": 14,
        "additional_info": "DaVinci Resolve zainstalowane na stanowiskach.",
        "date": datetime.date(2026, 11, 24),
        "category": Activity.Category.WARSZTAT,
    },
    {
        "club": "Klub Filmowy",
        "name": "Konkurs krótkich metraży",
        "desc": "Przegląd trzyminutowych etiud zgłoszonych przez studentów.",
        "location": "Sala kinowa 0.4",
        "custodian": "Tomasz Bąk",
        "limit": 20,
        "current_participants": 3,
        "additional_info": "Zgłoszenia filmów do 10 stycznia.",
        "date": datetime.date(2027, 1, 30),
        "category": Activity.Category.KONKURS,
    },
    # Klub Górski
    {
        "club": "Klub Górski",
        "name": "Wykład: bezpieczeństwo w Tatrach zimą",
        "desc": "Lawiny, sprzęt zimowy i planowanie trasy w warunkach zimowych.",
        "location": "Aula C",
        "custodian": "Katarzyna Lis",
        "limit": 45,
        "current_participants": 21,
        "additional_info": "",
        "date": datetime.date(2026, 11, 4),
        "category": Activity.Category.WYKLAD,
    },
    {
        "club": "Klub Górski",
        "name": "Wycieczka: Babia Góra",
        "desc": "Jednodniowe wyjście granią, ok. 6 godzin w terenie.",
        "location": "Krowiarki, parking główny",
        "custodian": "Katarzyna Lis",
        "limit": 18,
        "current_participants": 18,
        "additional_info": "Obuwie trekkingowe obowiązkowe.",
        "date": datetime.date(2026, 12, 5),
        "category": Activity.Category.WYCIECZKA,
    },
    # Klub Debat Oksfordzkich
    {
        "club": "Klub Debat Oksfordzkich",
        "name": "Warsztat argumentacji",
        "desc": "Budowa tezy, kontrargumenty i ćwiczenia z mowy ciała.",
        "location": "Sala 312",
        "custodian": "Paweł Nowicki",
        "limit": 20,
        "current_participants": 6,
        "additional_info": "",
        "date": datetime.date(2026, 11, 12),
        "category": Activity.Category.WARSZTAT,
    },
    {
        "club": "Klub Debat Oksfordzkich",
        "name": "Debata: AI w edukacji",
        "desc": "Debata oksfordzka z publicznością, dwie drużyny i sędziowie.",
        "location": "Aula A",
        "custodian": "Paweł Nowicki",
        "limit": 60,
        "current_participants": 22,
        "additional_info": "Publiczność głosuje po debacie.",
        "date": datetime.date(2027, 1, 22),
        "category": Activity.Category.SPOTKANIE,
    },
]


class Command(BaseCommand):
    help = "Dosypuje 5 klubów i 20 wydarzeń zróżnicowanych datą, kategorią i obłożeniem."

    @transaction.atomic
    def handle(self, *args, **options):
        new_clubs = 0
        for data in CLUBS:
            _, created = Club.objects.get_or_create(
                name=data["name"],
                defaults={"desc": data["desc"], "leader": data["leader"]},
            )
            new_clubs += int(created)

        club_lookup = {club.name: club for club in Club.objects.all()}

        new_activities = 0
        for data in ACTIVITIES:
            payload = {k: v for k, v in data.items() if k not in {"club", "name", "date"}}
            _, created = Activity.objects.get_or_create(
                club=club_lookup[data["club"]],
                name=data["name"],
                date=data["date"],
                defaults=payload,
            )
            new_activities += int(created)

        self.stdout.write(
            self.style.SUCCESS(
                f"Gotowe. Nowe kluby: {new_clubs}, nowe wydarzenia: {new_activities}. "
                f"Razem klubów: {Club.objects.count()}, wydarzeń: {Activity.objects.count()}."
            )
        )
