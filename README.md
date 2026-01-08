# PixelProof-Reborn 🛡️
**En videreføring av bacheloroppgaven ved Universitetet i Agder (2023).**

PixelProof er en plattform utviklet for å oppdage deepfakes i bilder og videoer, med mål om å beskytte allmennheten mot desinformasjon [30, 80]. Dette prosjektet gjenskaper og forbedrer den opprinnelige arkitekturen fra bacheloroppgaven "The PixelProof Project" [2].

## 🏗️ Arkitektur

Systemet er bygget som en fullstack-applikasjon med følgende komponenter [425]:

* **Frontend:** Flask/Jinja2 med fokus på enkelhet og brukervennlighet [311, 588].
* **Backend:** Asynkron Python-server for håndtering av videoprosessering [329, 783].
* **AI-motor:** Ansiktsdeteksjon med `dlib` og deepfake-analyse med moderne konvolusjonelle nevrale nettverk (CNN) [112, 455, 487].
* **Database:** Lagring av metadata og "crowd-sourcing"-resultater for forbedring av modeller [34, 508].

## 🚀 Funksjonalitet (under utvikling)

- [ ] Validering og nedlasting av YouTube-videoer [374, 492].
- [ ] Frame-sampling og ansiktsgjenkjenning i video [433].
- [ ] Crowd-sourcing modul for brukervalidering [355].
- [ ] Integrasjon med nyere AI-modeller for høyere nøyaktighet.
