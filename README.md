# 4elem.io

<b>Przedmiot</b> Programowanie w języku Python</br>
<b>Temat:</b> Implementacja gry typu agar.io z użyciem bibilioteki pygame<br>
<b>Twórcy:</b> Radosław Kopeć, Izabela Czajowska<br/>
<b>Data Rozpoczęcia:</b> 25.03.2020

### Contributors

- [Radosław Kopeć](https://github.com/radekkpc)

- [Izabela Czajowska](https://github.com/iczajowska)

## Harmonogram projektu

### I ETAP

* Server: 14.04.2020r.

1. ✅Zainicjalizowanie danych (tablica klientów wraz z informacjami o nich)
2. ✅Zaimplementowanie nasłuchiwania.
3. ✅Tworzenie osobnego wątku dla każdego podłączonego klienta.
4. ✅Funkcja obsługująca pobieranie i wysyłanie danych do klienta, oraz aktualizacje zmiennych (asynchroniczne wywoływana z funkcji głównej programu w innych wątku)
5. ✅ Ładne Readme.md
6. ✅Klasy reprezentujace gracza,mape,punkt,koło

* Client: 28.04.2020r. (Plik implementujący logikę łączenia się z serwerem, wysyłania i pobierania danych)
1. ✅Funkcja łącząca się, pobierająca id, wysyłająca UserName
2. ✅Wysłanie danych ( pozycja i wszystkie niezbędne dane o grze)
3. ✅Pobieranie danych (Informacje o wszystkich obiektach na mapie)

* Aplikacja (Desktopowa aplikacja wykorzystująca
pygame): 12.05.2020 r.

1. ✅Wyświetlanie mapy
2. ✅Wyświetlanie Gracza
3. ✅Wyświetlanie innych graczy
4. ✅Skalowanie względem lewego górnego rogu (Gracz ma byc zawsze w środku)
5. ✅Zaimplementowanie Poruszania się (Klawiatura lub myszka zobaczy się)
6. ✅Zaimplementowanie odświeżania 30FPS (wysyłania i pobierania danych z serwera w tym czasie)
7. ✅Połączenie Clienta i Aplikacji
8. ✅Implementacja pobierania UserName i rozpoczynania gry za pomocą przycisku
9. ✅Poprawic sterowanie 
10. ✅poprawic wyswietlanie
11. ✅Zmniejszyc zakres widocznosci mapy wieksze obiekty, mniejsza widocznosc
12. Zaimplementowac brak mozliwosci wyjscia za granice mapy
### II ETAP (Udoskonalenia, realizacja mechaniki gry) 20.05.2020 r.

* Client,Serwer,Aplikacja:

1. ✅Stworzenie wyboru żywiołu
2. ✅Stworzenie żywiołów
3. Interakcja między żywiołami
4. ✅Dodanie jedzonka na mapie
5. Dodanie levelowania
6. Dodanie umiejętności

### III ETAP (Dopieszczanie grafiki) Jak starczy czasu 09.06.2020 r.

1. ✅Obrazy ładowne z plików przeźroczyste tło
2. Zredukowanie przeskoków (interpolacja liniowa gdzie tylko się da)
3. Ranking graczy
4. Korona przy Nicku najlepszego gracza :P

### Dodadkowe info

- funkcja select,
- socety udp tcp, kop
- kopiuj wklej ticka do readme jak cos zrobisz ✅
- żeby odpalic w 1 terminalu: python server.py
- w 2 terminalu python app.py

## Opis gry