# 🎮 Monster Arena – Rundenbasiertes Kampfspiel in Python

**Monster Arena** ist ein rundenbasiertes Konsolenspiel, das in Python entwickelt wurde. Der Spieler steuert ein eigenes Monster und tritt in rundenbasierten Kämpfen gegen computergesteuerte Gegner an. Das Projekt dient als Lernplattform für objektorientierte Programmierung mit Python.

---

## 🔥 Features

- Konsole-basierter Monsterkampf
- Unterschiedliche Monster mit eigenen Attributen
- Objektorientiertes Design (inkl. Vererbung und Polymorphie)
- Erweiterbar um Spezialfähigkeiten, Monsterklassen oder GUI

---

## 📁 Projektstruktur

<pre>
monster_arena/
├── game.py              # Einstiegspunkt, Spielsteuerung
├── monster.py           # Monster-Basis und Methoden
├── attack.py            # Angriffslogik
├── battle_manager.py    # Kampfabwicklung
├── README.md            # Projektdokumentation
</pre>

---

## ▶️ Ausführung

### Voraussetzungen
- Python 3.10 oder neuer  
(Optional: eine IDE wie VS Code, PyCharm oder Thonny)

### Starten des Spiels

```bash
python game.py


### Starten des Spiels

```bash
python game.py


| Klasse                | Beschreibung                                            |
| --------------------- | ------------------------------------------------------- |
| `Monster`             | Repräsentiert ein Monster mit HP, Angriff, etc.         |
| `Attack`              | Modelliert einen Angriff mit Schaden & Kosten           |
| `BattleManager`       | Steuert den Ablauf eines Kampfes zwischen zwei Monstern |
| `Game` (in `game.py`) | Einstiegspunkt, Spielmenü und Monsterwahl               |


🚀 Geplante Erweiterungen
Spezialfähigkeiten für bestimmte Monstertypen

Benutzerwahl während der Runden (z. B. Angriff auswählen)

Weitere Monsterklassen mit Vererbung

Highscore- oder XP-System

GUI mit Tkinter oder Web-Frontend mit Flask

📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen siehe LICENSE.

✨ Lernziele
Objektorientierte Programmierung in Python

Strukturierung von Code in Module & Klassen

Einstieg in Game-Design-Logik & mögliche GUI-Erweiterung
