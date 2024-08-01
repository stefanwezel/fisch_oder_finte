# Fisch oder Finte?

Eine der ältesten Fragen der Menschheitsgeschichte! Handelt es sich um eine Fischart die es tatsächlich gibt oder um eine Erfundene? Es gibt zwei Möglichkeiten dein Fischwissen zu testen, welche im Folgenden beschrieben werden.

## Webapp (Für Breitensportler)
Besuche hierfür einfach [die Website](https://fischoderfinte.de) und lege los. In jeder Runde werden dir Namen von vier verschiedene Fischarten angezeigt, und deine Aufgabe ist es die eine erfundene Art auszuwählen.



## CLI Game (Für nerdige Hacker)

Sobald du das repository ge-cloned hast kannst du dein Fischwissen testen, indem du in deiner Konsole `python play_in_cli.py` ausführst. Ansonsten gelten die gleichen Regeln und alles andere sollte sich von selbst erklären :) Das Spiel braucht nicht viele libraries. Starte mit einem frischem `conda` environment mit einer halbwegs neuen python Version (z.B. `conda create -n "fisch" python=3.12`). Danach kannst du mit `pip install -r requirements.txt` die nötigen dependencies installieren.


## Contributing & Installation

Um an "Fisch oder Finte" zu entwickeln kannst du entweder das `requirements.txt` direkt nutzen um die nötigen libraries zu installieren oder du kannst `Docker` nutzen um in einem Container zu entwickeln. Das `docker-compose.yml` baut ein Image und startet einen Container der direkt eine lokale Version der Webapp startet. Das kannst du einfach mit dem command `docker compose up --build` (oder `docker-compose up --build` für die `^docker compose v1`) triggern. Das ganze wird dann im "development mode" sein, und deine changes sollten direkt in der lokal laufenden App verfügbar sein. Um ein "production" Container zu starten kannst du den command `docker compose -f docker-compose.prod.yml --build` nutzen. Wenn du an neuen Features/Fixes arbeitest, zweige einen Branch von `main` ab und erstelle anschließend, wenn du fertig bist, einen pull request.