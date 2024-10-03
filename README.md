# Domowa Biblioteka

Aplikacja pozwala na tworzenie bazy biblioteka.db i przechowywanie informacji o książkach, autorach, wypożyczeniach oraz informację czy książka jest na półce.

## Instalacja

1. Pobierz repozytorium z github:
   ```bash
   git git@github.com:piotrsobala/Modul13.4_zadanie_biblioteka.git
   cd Modul13.4_zadanie_biblioteka
   
2. Stwórz wirtualne środowisko 
   python -m venv "folder np. venv"

3. Aktywacja środowiska wirtualnego
   source "sciezka-do-katalogu…/venv/bin/activate"
   
4. Zainstaluj biblioteki i framework z requirements.txt
   pip install -r requirements.txt


5. Inicjalizacja bazy danych.
   a) Inicjalizacja migracji: flask db init 
      #utworzy folder migrations, który będzie zawierał skrypty migracji
   b) Utworzenie migracji flask db migrate -m "Initial migration." 
      #To polecenie wygeneruje plik migracyjny, który będzie zawierał instrukcje do utworzenia tabel author, book, loan i innych powiązanych struktur.
   c) Zastosowanie migracji: flask db upgrade
      #utworzy wszystkie brakujące tabele w bazie SQLite.

6. Uruchom serwer Flask
   flask shell

7. W powłoce możesz wykonywać operacje na bazie danych
   np. Tworzenie nowego autora:
   new_author = Author(name="Sample author")
   b.session.add(new_author)
   db.session.commit()