### 4elem.io

Harmonogram projektu
Temat: Implementacja gry typu agar.io z użyciem bibilioteki pygame
Radosław Kopeć
Izabela Czajowska


###### I ETAP

* Server: 14.04.2020r.
------
Zainicjalizowanie danych (tablica klientów wraz z informacjami o nich)
-Zaimplementowanie nasłuchiwania.
-Tworzenie osobnego wątku dla każdego podłączonego klienta.
-Funkcja obsługująca pobieranie i wysyłanie danych do klienta, oraz aktualizacje zmiennych (asynchroniczne wywoływana z funkcji głównej programu w innych wątku)

* Client: 28.04.2020r.
------
(Plik implementujący logikę łączenia się z serwerem, wysyłania i pobierania danych)
⋅⋅⋅-Funkcja łącząca się, pobierająca id, wysyłająca UserName
⋅⋅⋅-Wysłanie danych ( pozycja i wszystkie niezbędne dane o grze)
⋅⋅⋅-Pobieranie danych (Informacje o wszystkich obiektach na mapie)

* Aplikacja (Desktopowa aplikacja wykorzystująca
pygame): 12.05.2020 r.
------
-Wyświetlanie mapy
-Wyświetlanie Gracza
-Wyświetlanie innych graczy
-Skalowanie względem prawego górnego rogu (Gracz ma byc zawsze w środku)
-Zaimplementowanie Poruszania się (Klawiatura lub myszka zobaczy się)
-Zaimplementowanie odświeżania 30FPS (wysyłania i pobierania danych z serwera 	 w tym czasie)
-Połączenie Clienta i Aplikacji
-Implementacja pobierania UserName i rozpoczynania gry za pomocą przycisku

###### II ETAP (Udoskonalenia, realizacja mechaniki gry) 20.05.2020 r.
* Client,Serwer,Aplikacja:
-Stworzenie wyboru żywiołu
-Stworzenie żywiołów
-Interakcja między żywiołami
-Dodanie jedzonka na mapie
-Dodanie ewoluowania
-Dodanie umiejętności

###### III ETAP (Dopieszczanie grafiki) Jak starczy czasu 09.06.2020 r.
-Obrazy ładowne z plików przeźroczyste tło
-Zredukowanie przeskoków (interpolacja liniowa gdzie tylko się da)
-Ranking graczy
-Korona przy Nicku najlepszego gracza :P

funkcja select,
socety udp tcp
