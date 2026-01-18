

# Asteroids — v2.3.0

A lightweight Python reimplementation of the classic arcade game "Asteroids." Fast-paced and focused on gameplay variety through multiple modes and simple controls.

## Overview
Fly your ship, destroy asteroids, and survive as long as you can. This version adds multiple game modes that change scoring, bullet behavior, fire rate, and difficulty pacing.

## Current release
v2.3.0 — WORKING PAUSE MENU + QOL + NEW RENDERER
- Pause menu now actually pauses the game
- Exit to main menu option available
- Ability to resize the window

(See Releases on GitHub for full changelogs and assets.)

## How to play
- Controls:
  - W / A / S / D — Move (thrust / rotate / reverse as implemented)
  - L — Fire laser (shot behavior being reworked)
  - Esc - Pause game
## Game modes
- Tank Mode
  - 1.5× score multiplier
  - Larger bullets
  - Higher shooting cooldown (slower fire rate)
- Normal Mode
  - Standard scoring and firing behavior
- Minigun Mode
  - Extremely fast fire rate
  - No points awarded
- Hard Mode
  - Asteroids spawn faster (increased difficulty)
  - 2x score multiplier

## Scoring
- 1 point is awarded for each asteroid split in half/destroyed
- Tank Mode multiplies points by 1.5.
- Minigun Mode disables score accumulation.
- Hard mode multiplies points by 2.

## Roadmap
Planned improvements:
- More character colors or even diffrent models
- Reworking laser as it is buggy
- Additional QoL and renderer refinements

