#IS-118-1-25H-innlevering-2-grp-25
# Medborgerportal - Del 2: Interaktiv historie om Erling og medborgerportalen
# Har fått med 3 ledd &  forskjellige avslutninger basert på valgene.
# intro til spillere også valg funksjoner
def intro():
 print("Velkommen til Erling sin interaktive historie!")
 print("Prosjektet befinner seg i stormingfasen.")
 print("Konflikter og spenning preger teamet, og Erling må ta tre viktige beslutninger.\n")

# Første valget
def beslutning_1():
 print("1) Hvordan håndterer Erling konflikten mellom Silje og Sivert?")
 print("A) Ta det opp i plenum")
 print("B) Individuelle samtaler")
 valg = input("Velg A/B: ").strip().upper()
 if valg == "A":
     print("Plenum: Skaper åpenhet og felles normer, men risiko for eskalering.")
 elif valg == "B":
     print("Individuelle samtaler: Demper temperaturen, men kan oppleves som lukket.")
 else:
     print("Ugyldig valg. Erling nøler, men velger til slutt individuelle samtaler (Jacobsen, 2018).")
     valg = "B"
 return valg

# Andre valget
def beslutning_2():
 print("\n2) Hvordan håndterer Erling uenigheten mellom Hamdi og Jabir?")
 print("A) Felles møte + pilot")
 print("B) Avvente")
 valg = input("Velg A/B: ").strip().upper()
 if valg == "A":
     print("Felles møte: Kombinerer kontroll og dialog, gir læring, men krever tid.")
 elif valg == "B":
     print("Avvente: Gir eierskap, men risiko for eskalering og misforståelser.")
 else:
     print("Ugyldig valg. Erling velger felles møte for å skape struktur (Andersen & Schwencke, 2013).")
     valg = "A"
 return valg

# Tredje valget
def beslutning_3():
 print("\n3) Hvordan bevarer Erling motivasjonen i teamet?")
 print("A) Relasjonsbygging og sosiale aktiviteter")
 print("B) Prioritere fremdrift og leveranser")
 valg = input("Velg A/B: ").strip().upper()
 if valg == "A":
     print("Relasjonsbygging: Styrker trygghet og trivsel, men reduserer tid til leveranser.")
 elif valg == "B":
     print("Leveransefokus: Gir fremdrift og tydelige mål, men kan føre til slitasje.")
 else:
     print("Ugyldig valg. Erling velger relasjonsbygging for å styrke teamet (Gjøsund & Huseby, 2016).")
     valg = "A"
 return valg

# Sluttutfallet basert på valgene
def sluttutfall(v1, v2, v3):
 print("\n--- Sluttutfall ---")
 print("Erling sine valg underveis:")
 print("1)", "Plenum" if v1 == "A" else "Individuelle samtaler")
 print("2)", "Felles møte + pilot" if v2 == "A" else "Avvente")
 print("3)", "Relasjonsbygging" if v3 == "A" else "Leveransefokus")
# Kaller på print funksjonen for å vise resultatet
 print("\nResultat:")
 if v1 == "A" and v2 == "A" and v3 == "A":
     print("Norming: Tillit gjenopprettes, teamet går videre til normingfasen.")
 elif v1 == "B" and v2 == "B" and v3 == "B":
     print("Delvis løsning: Konflikten håndteres delvis, men relasjonene er fortsatt sårbare.")
 else:
     print("Vedvarende storming: Prosjektet mister samhold, prototypen forsinkes.")
# avslutter med å kalle på main funksjonen og ser beslutningene opp mot valgene.       
def main():
 intro()
 v1 = beslutning_1()  # første valget
 v2 = beslutning_2()  # andre valget
 v3 = beslutning_3()  # tredje valget
 sluttutfall(v1, v2, v3)
# holder scriptet fleksibelt, kjørbart alene og som modul.
if __name__ == "__main__":
 main()

# Spør om spiller vil spille en gang til
if __name__ == "__main__":
    spill_igjen = "ja"
    while spill_igjen == "ja":
        main()
        # spør om spilleren vil spille igjen
        spill_igjen = input("\nVil du spille igjen? (ja/nei): ").strip().lower()
        
        # sjekk at svaret er gyldig
        while spill_igjen not in ["ja", "nei"]:
            print("Du må svare ja eller nei til meg .")
            spill_igjen = input("Vil du spille igjen? (ja/nei): ").strip().lower()
    
    print("Takk for at du spilte!")
