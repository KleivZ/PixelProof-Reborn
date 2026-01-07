# PixelProof-Reborn 🛡️
**En videreføring av bacheloroppgaven ved Universitetet i Agder (2023).**

[cite_start]PixelProof er en plattform utviklet for å oppdage deepfakes i bilder og videoer, med mål om å beskytte allmennheten mot desinformasjon[cite: 30, 80]. [cite_start]Dette prosjektet gjenskaper og forbedrer den opprinnelige arkitekturen fra bacheloroppgaven "The PixelProof Project"[cite: 2].

## 🏗️ Arkitektur
[cite_start]Systemet er bygget som en fullstack-applikasjon med følgende komponenter[cite: 425]:
- [cite_start]**Frontend:** Flask/Jinja2 med fokus på enkelhet og brukervennlighet[cite: 311, 588].
- [cite_start]**Backend:** Asynkron Python-server for håndtering av videoprosessering[cite: 329, 783].
- [cite_start]**AI-motor:** Ansiktsdeteksjon med `dlib` og deepfake-analyse med moderne konvolusjonelle nevrale nettverk (CNN)[cite: 112, 455, 487].
- [cite_start]**Database:** Lagring av metadata og "crowd-sourcing"-resultater for forbedring av modeller[cite: 34, 508].

## 🚀 Funksjonalitet (under utvikling)
- [ ] [cite_start]Validering og nedlasting av YouTube-videoer[cite: 374, 492].
- [ ] [cite_start]Frame-sampling og ansiktsgjenkjenning i video[cite: 433].
- [ ] [cite_start]Crowd-sourcing modul for brukervalidering[cite: 355].
- [ ] Integrasjon med nyere AI-modeller for høyere nøyaktighet.
