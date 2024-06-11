from django.views.generic import ListView, DetailView

from dt_bands.models import Band, BandMember, Instrument


class BandListView(ListView):
    model = Band
    template_name = 'bands/BandView.html'  # Mise à jour du nom du fichier template


class BandDetailView(DetailView):
    model = Band
    template_name = 'bands/BandView.html'  # Mise à jour du nom du fichier template


class BandMemberListView(ListView):
    model = BandMember
    template_name = 'bands/BandMemberView.html'  # Mise à jour du nom du fichier template


class BandMemberDetailView(DetailView):
    model = BandMember
    template_name = 'bands/BandMemberView.html'  # Mise à jour du nom du fichier template


class InstrumentListView(ListView):
    model = Instrument
    template_name = 'bands/InstrumentView.html'  # Mise à jour du nom du fichier template


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = 'bands/InstrumentView.html'  # Mise à jour du nom du fichier template
