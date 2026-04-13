# Övning 22 - Lasttesta med Locust

Starta Flask-applikationen books från övning 13. Tänk på att exponera porten till containern med `-p 5000:5000` när du startar containern!

I containern går du in i katalogen `ovningar/13/books`:

```sh
cd ovningar/13/books
```

Starta Flask-appen med:

```sh
python app.py
```

Nu är bok-APIet igång och lyssnar på port 5000.

Öppna en ny terminal och starta en ny anslutning till containern:

```sh
docker exec -it testlab bash
```

> _testlab_ är namnet på containern, heter din container något annat måste du ändra det till korrekt namn. Du kan också använda container id istället för namn, se `docker ps` för container id och name.

I katalogen för övning 22 finns en `locustfile.py` som innehåller testerna jag visade i presentationen. Du kan vända den som grund för dina tester.

Kör testet:

```sh
locust -f locustfile.py --host=http://localhost:5000 \
    --headless -u 50 -r 10 --run-time 60s
```

- `-u 50` anger att det skall vara 50 simulerade användare.
- `-r 10` anger att vi skall starta 10 nya användare per sekund.
- `--run-time 60` anger att vi vill köra testet i 60 sekunder.

Analysera resultatet:
- Vad är p95 response time?
- Hur hög är failure rate?

Kan du hitta fler api-endpoints i `app.py`, för att skriva fler tester i `locustfile.py` ?

## Extrauppgift: Stresstest!

Öka från `-u 200` till `-u 500` i korta steg. Var går gränsen?

