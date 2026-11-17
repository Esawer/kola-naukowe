from django.db import models
from django.utils import timezone


class Club(models.Model):
    class Color(models.TextChoices):
        BLUE = "blue", "Niebieski"
        CYAN = "cyan", "Turkusowy"
        TEAL = "teal", "Morski"
        EMERALD = "emerald", "Zielony"
        LIME = "lime", "Limonkowy"
        AMBER = "amber", "Bursztynowy"
        ORANGE = "orange", "Pomarańczowy"
        VIOLET = "violet", "Fioletowy"

    CLUB_BADGE_STYLES = {
        "blue":    "border-blue-200 bg-blue-50 text-blue-700 dark:border-blue-900 dark:bg-blue-950 dark:text-blue-300",
        "cyan":    "border-cyan-200 bg-cyan-50 text-cyan-700 dark:border-cyan-900 dark:bg-cyan-950 dark:text-cyan-300",
        "teal":    "border-teal-200 bg-teal-50 text-teal-700 dark:border-teal-900 dark:bg-teal-950 dark:text-teal-300",
        "emerald": "border-emerald-200 bg-emerald-50 text-emerald-700 dark:border-emerald-900 dark:bg-emerald-950 dark:text-emerald-300",
        "lime":    "border-lime-200 bg-lime-50 text-lime-700 dark:border-lime-900 dark:bg-lime-950 dark:text-lime-300",
        "amber":   "border-amber-200 bg-amber-50 text-amber-700 dark:border-amber-900 dark:bg-amber-950 dark:text-amber-300",
        "orange":  "border-orange-200 bg-orange-50 text-orange-700 dark:border-orange-900 dark:bg-orange-950 dark:text-orange-300",
        "violet":  "border-violet-200 bg-violet-50 text-violet-700 dark:border-violet-900 dark:bg-violet-950 dark:text-violet-300",
    }

    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=2500)
    leader = models.CharField(max_length=500)
    color = models.CharField(max_length=16, choices=Color.choices, default=Color.BLUE)

    @property
    def club_badge(self):
        return self.CLUB_BADGE_STYLES.get(self.color, self.CLUB_BADGE_STYLES["blue"])

    def __str__(self):
        return self.name

class Activity(models.Model):
    class Category(models.TextChoices):
        WYKLAD = "wykład", "Wykład"
        WARSZTAT = "warsztat", "Warsztat"
        KONKURS = "konkurs", "Konkurs"
        SPOTKANIE = "spotkanie", "Spotkanie"
        WYCIECZKA = "wycieczka", "Wycieczka"

    name = models.CharField(max_length=200)
    desc = models.TextField()
    location = models.CharField(max_length=500)
    custodian = models.CharField(max_length=500)
    limit = models.IntegerField()
    current_participants = models.IntegerField(default=0)
    additional_info = models.CharField(max_length=2500)
    date = models.DateField()

    CATEGORY_COLORS = {
        Category.WYKLAD: "border-t-blue-500 dark:border-t-blue-400",
        Category.WARSZTAT: "border-t-emerald-500 dark:border-t-emerald-400",
        Category.KONKURS: "border-t-orange-500 dark:border-t-orange-400",
        Category.SPOTKANIE: "border-t-violet-500 dark:border-t-violet-400",
        Category.WYCIECZKA: "border-t-rose-500 dark:border-t-rose-400",
    }

    category = models.CharField(
        max_length=25,
        choices=Category.choices,
        default=Category.SPOTKANIE,
    )

    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    @property
    def is_full(self):
        return self.current_participants >= self.limit

    @property
    def is_past(self):
        return self.date < timezone.localdate()

    @property
    def occupancy_percent(self):
        if not self.limit:
            return 0
        return round(self.current_participants * 100 / self.limit)

    @property
    def get_category_color(self):
        return self.CATEGORY_COLORS.get(
            self.category, "border-t-slate-400 dark:border-t-slate-500"
        )

    def __str__(self):
        return self.name