Korpusar hittas här: https://drive.google.com/drive/folders/13OIRR28FzDHKhlw7OwTRl5lJP5-UI6sN?usp=sharing
Korpusarna är strukturerade i 10/100 meningar (per datapunkt) i taget från 1700-2000.
Jag föreslår att man använder de med 10 meningar i taget.
För struktur och vad som finns i varje datapunkt kolla i data_point_class.py.

1. ladda ner korpusar/datasetten och spara dem i en mapp 
2. Ändra pathen i main.py till rätt path
3. för att träna och köra, kör train_large_set() i main.py

kör

python main.py

Om du vill testa med olika features kan du kommentera bort features i data_classifier.py, rad 28-31

