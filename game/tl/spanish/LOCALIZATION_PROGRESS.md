# Spanish Localization Progress

## Method

- Work in ordered passes, not random isolated fixes.
- Preserve Ren'Py syntax, variables, tags, pauses and speaker ids.
- Follow `VOICE_GUIDE.md` for character voice and glossary.
- After each edited batch, run checks for broken string literals and known machine-translation artifacts.

## Status

### Foundation

- Voice guide: done.
- UI/system/profile/credits cleanup: done.
- Global machine-artifact cleanup pass: done.
- Soulless terminology: standardized as `Desalmados`.
- Duplicate Spanish `old/new` string declarations: removed; Ren'Py duplicate string check passed.

### Script Pass

- `script.rpy` opening Lora/MC recording scene: edited.
- `script.rpy` NoGlory/Sofia tutorial variants: edited.
- `script.rpy` first war/radio scene opening: edited.
- `script.rpy` war continuation, family dinner, Norman/Lora/Li Wei flashback opening: edited.
- `script.rpy` Anya street rescue, club arrival, Amy/internal Anya conflict, Olivia reunion, departure, car chase and jungle setup through the guidebook rustle: edited.
- `script.rpy` repeated Olivia timed variants and selected duplicated machine artifacts: fixed.
- `script.rpy` jungle encounter, Shiya reunion, alien ship explanation, first ship exploration, key-card door, robot/C4 scene, radio attack, glowing-key reveal and end-of-prologue hostage confrontation: edited.
- `script.rpy` selected duplicate/update-block artifacts for this area: fixed.
- `script.rpy` post-hostage/end-of-prologue aftermath, end-card notes, and selected duplicate spaceship/end-prologue blocks: edited.
- `script.rpy` late spaceship/end-prologue combat and extraction duplicate blocks: edited; Azarkhan collapse, Olivia combat calls, Miriel intervention and portal/extraction lines tightened.
- `script.rpy` targeted machine-calque cleanup for `hell`, `safe and sound`, `pulling the strings`, `don’t add up`, gun-sight and traffic lines: fixed.
- `script.rpy` second quality pass started: tutorial/war repeat blocks, homedinner/Anna/bar micro-scenes, late jungle/spaceship duplicate route and obvious tag/action artifacts (`Right`, `Sigh`, `Rude`, `No promises`, repeated `exactamente`) corrected.
- `script.rpy` spaceship duplicate terminology tightened: `tarjeta de acceso`, `mecanismo de apertura`, `nave`, `máquina asesina`; selected Olivia/Shiya/Richard banter restored to natural Spanish.
- `script.rpy` pre-Story01 quality layer: Norman/Shiya handler terminology standardized as `enlace operativo`; late jungle duplicate dialogue, `{b}you{/b}` tag artifacts, corridor/keycard fragments, status/combat command lines and selected family/bar echoes corrected.
- `script.rpy` current handoff state: paused broad script pass to work through `Story01.rpy` scene by scene; remaining script issues are expected to be smaller scattered artifacts rather than the large broken clusters already corrected.
- `anya_replay.rpy` Lora replay micro-pass: corrected gender/name drift and restored a warmer, predatory Lora voice.
- `Story01.rpy` early post-transfer inner monologue micro-pass: corrected obvious machine-breakage and tightened MC voice.
- `Story01.rpy` / `Story04.rpy` micro-cleanup: fixed stray `Understood`, agreement/hesitation phrasing and selected duplicate combat artifacts.
- Latest check: duplicate `old/new` declarations 0; edited-window `Story01.rpy` final2 complex-reveal/mimic/combat/crypt quality-artifact hits 0; selected Story01 red-phrase search 0; Cyrillic in edited dialogue 0; placeholder/tag mismatches 0; speaker mismatches 0.
- Current script quality: prologue and main spaceship/end-prologue spine are readable and increasingly consistent; repeated alternate-route blocks still need further manual review because quality is uneven outside the corrected batches.
- Next target: sweep the remaining Story02-labeled update blocks appended inside `Story01.rpy`, plus nearby `gate4/laborat` route artifacts, before moving back to `Story02.rpy`.

### Story Passes

- `Story01.rpy`: broad scene-by-scene pass started; opening rescue/news/betrayal, void-and-light sequence, early laboratory awakening, first question branches, and duplicated update blocks through the son/Olivia/location explanations edited for voice and flow.
- `Story01.rpy`: Miriel escort, Olivia reunion, Flora eye-pain intervention, office-wait corridor, and repeated `firstanswernext` variants edited for character voice and natural Spanish.
- `Story01.rpy`: first lore Q&A pass edited; `Confederación Arks`, `razas/subrazas`, `Hilo de Memoria`, `Weavers`, faction summaries, governance and blood/technology explanations tightened.
- `Story01.rpy`: Madam/Astoria interview pass edited; `Muestra-371`, `Nuevo Comienzo`, ship/mission questioning, Lora reveal, `Red de Realidades`, Norman answer, Yong/Astoria aftermath and hostile `dodgebut` branches synced.
- `Story01.rpy`: post-interview `eye` pass edited; Ostorius eye repair, Olivia confrontation, Miriel handoff, Flora's caustic commentary, Father aside, and duplicated `eye` variants through the later route block tightened for voice and flow.
- `Story01.rpy`: Norman grief beat, Olivia/Flora post-interview confrontation, split-party handoff, and duplicated `taxi` variants edited for emotional continuity, MC restraint, Olivia's protective anger and Flora's caustic bite.
- `Story01.rpy`: first city walk and security scanner setup edited; Flora's technical sarcasm, registry/brain-scrape explanation, wrong-execution aside, failed idealist-revolt story and duplicated `street3` scanner variants tightened.
- `Story01.rpy`: Olivia/Miriel flashback quality pass edited; main family-backstory route, short duplicate route and late compressed retelling synced for Olivia's guarded grief, Miriel's measured probing, Anya's sharp concern, school-bullying memories and [mc] restaurant-hiring beat.
- `Story01.rpy`: `street3` guard/taxi/lower-level follow-up edited; patrol chatter, `Hermanos Verdugos`, Flora's taxi banter, sky-warden scanner explanation, Registry/brain-scrape lines, slum survival commentary, club handoff and duplicated early/mid/late route variants tightened for voice and flow.
- `Story01.rpy`: `choice1` internal monologue pass edited; MC's resurrection recap, Azarkhan/son trauma, Lora-as-anchor thread, Confederación Arks/world-shock reflections, informant priority, Lady/Mistress suspicions, Web questions and duplicated compressed memory echoes tightened.
- `Story01.rpy`: `cyberstreet1` echo pass edited; abandoned Sector 8 mood, Flora comms/implant link, relay-node objective, distress-signal bodies, `El Sin Rostro`, invisibility threat, soulless info request and duplicated left-path/right-path variants tightened.
- `Story01.rpy`: `HelpArc` rescue and `bar_cyber` transition pass edited; girl rescue, Flora's reprimand, Miriel's measured thanks, Olivia's department outrage, doctor/handler exchange, Ray/Ivy gatekeeping, Emberlyn rank/dragon lore and early/mid/late duplicate route variants tightened.
- `Story01.rpy`: `bar_cyber` Ivy table scene and `bar_cyber1` Emberlyn entrance edited; assassination-attempt discussion, Ivy's seductive/debt voice, Ray's late denial route, Emberlyn's first power play, Ark/tomb/artifact exposition and selected early/mid/late duplicate variants tightened.
- `Story01.rpy`: `bar_cyber1` Ark/Earth/Yong/Acto de Sangre continuation edited; Lora project hook, holographic projector, Ark identification, Earth-distance/wormhole explanation, Elven Federation death reveal, Soulless attack, warehouse/armory handoff, late Ark negotiation route, first outpost/Executor beat, compressed Executor duplicate, gas/metro attack-plan logic and wider jammer terminology sweep tightened with synced `Arca`, `nave`, `Desalmados`, `interferidor`, `Federación Élfica` and `Ejecutor` terms.
- `Story01.rpy`: `gate2` mission approach edited; cyber-ad satire, Flora mission comms, time-differential/Lora concern, team deployment, gate approach banter, Olivia arrival/oath tension, Flora-vs-Olivia insults, Miriel `Parca Fría` nickname beat, signal-jam warning, quantum-titanium gate, metro bypass, Olivia panic beat and first tunnel-navigation variants tightened; synced duplicate route blocks and preserved `interferidor`, `nave`, `Aldarion`, `Miriel` and `Parca Fría` terminology.
- `Story01.rpy`: `gate2/gate3/gate4` tunnel-combat continuation edited; route choice, ammunition status, underground-neighbor explanation, arachnoid lore, first swarm attack, Olivia command speech, Miriel `Modo Parca` activation, retreat, post-fight status, living-interferidor theory, Inquisition encounter and `Parca Fría` references tightened across main and duplicate route variants.
- `Story01.rpy`: shelter/rest continuation edited; Miriel mask beat, Lora research-team insignia discovery, Olivia collapse and treatment, MC gratitude/Miriel guilt exchange, restaurant flashback with Lora and early Olivia, Miriel avoidance beat, Olivia wake-up transition and selected `gate3/gate4/olivia_fr_scene` duplicates tightened; first `final2` extraction echoes, Flora network-jam troubleshooting, unknown-complex suspicion, `Desalmados` terminology and experiment-reveal setup synced across variants.
- `Story01.rpy`: Olivia intimate branch and immediate `final2` passage continuation edited; Olivia's desire/boundary beats, MC restraint, Miriel's interruption/orders, hidden-human-presence lead, door entry, Flora terminal troubleshooting and selected `gate3/olivia_fr_scene` route echoes tightened; removed an in-dialogue 418-error translator note and synced `interferidor` wording.
- `Story01.rpy`: `final2` complex reveal continuation edited; mimic/Ostorius scare, laboratory origin reveal, restrictions-release combat, evacuation commands, Reny betrayal flashback, planet-sacrifice line, creator save/support notes and later crypt/contamination deduction tightened across main and duplicate variants while preserving wait tags and `[mc]`.
- `Story02.rpy`: terminology and several obvious machine artifacts fixed; full scene-by-scene pass pending.
- `Story03.rpy`: terminology and several obvious machine artifacts fixed; full scene-by-scene pass pending.
- `Story04.rpy`: terminology and several obvious machine artifacts fixed; full scene-by-scene pass pending.

### Later Passes

- `anya_replay.rpy`: opening Anya replay synced with the improved main-scene voice; full pass pending.
- `codex.rpy`: terminology pass done; style pass pending.
- Small UI files: mostly done; final QA pending.
