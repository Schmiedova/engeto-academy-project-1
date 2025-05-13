# Projekt 1: Textový analyzátor

Jednoduchý konzolový program v Pythonu pro analýzu textů, vytvořený jako první projekt do Engeto Online Python Akademie.

---

## Popis

Program:

1. Načte předpřipravené texty ze souboru `task_template.py` (proměnná `TEXTS`).
2. Zeptá se uživatele na přihlašovací jméno a heslo.
3. Ověří, zda jsou zadané údaje registrované (uživatel–heslo jsou uloženy ve slovníku `USERS`).
4. Pokud uživatel existuje, vypíše uvítací zprávu a nabídne výběr jednoho ze tří textů.
5. Pro vybraný text spočítá a zobrazí:
   - celkový počet slov  
   - počet titlecase slov (začínajících velkým písmenem)  
   - počet slov psaných VELKÝMI PÍSMENY  
   - počet slov psaných malými písmeny  
   - počet číselných řetězců a jejich součet  
6. Vykreslí v konzoli jednoduchý vodorovný „bar chart“ četností délek slov (dynamicky upravuje šířku podle největší četnosti).

Pokud uživatel není registrovaný, program vypíše chybovou hlášku a ukončí se.

---

## Požadavky

- Python 3.6+
- Žádné externí knihovny (používá pouze standardní knihovnu)

---

## Instalace

1. Naklonujte si repozitář:
   ```bash
   git clone https://github.com/Schmiedova/engeto-academy-project-1.git
   cd engeto-academy-project-1

2. Ověřte, že ve složce máte:
- text_analyzer.py
- task_template.py (obsahuje proměnnou TEXTS)

---


## Použití

1. Spusťte skript:
   bash
   python text_analyzer.py

2. Zadejte své uživatelské jméno a heslo. Registrovaní uživatelé:
   - bob / 123
   - ann / pass123
   - mike / password123
   - liz / pass123

3. Vyberte číslo textu (1–3).

4. Prozkoumejte statistiky a graf četností délek slov.

---

## Struktura kódu

1. Hlavička
- Informace o autorovi a projektu.

2. Importy
- sys, string, task_template.TEXTS

3. Uživatelská kontrola
- Ověření existence a správnosti hesla.

4. Výběr textu
- Kontrola platnosti vstupu (číselný, v rozmezí).

5. Analýza textu
- Rozdělení na slova, čištění interpunkcí, kategorizace (titlecase, uppercase, lowercase, numeric).

6. Výpis statistik
- Počty slov, titlecase, uppercase, lowercase, numeric a součet čísel.

7. Graf četností
- Dynamické nastavení šířky „sloupcového“ grafu podle nejvyšší četnosti slov dané délky.

---

## Autor
Michaela Schmiedová
- Engeto Online Python Akademie
- email: michaela.schmiedova@email.cz
- discord: misa_47996