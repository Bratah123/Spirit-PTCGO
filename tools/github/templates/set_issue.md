$progress_block

Part of $epic_ref ($epic_title).

| Property | Value |
|---|---|
| **Set** | $set_label |
| **Released** | $release |
| **PTCGO code** | $ptcgo_code |
| **Cards** | $card_summary |
| **Scripts** | $script_links |

### Full Completion Checklist
- [ ] Every card has a script with no `effect=unimplemented` (ticked by the bot)
- [ ] Card art is in `spirit/assets/cards/` and the set bundle builds

### Engine APIs needed
<!-- List any new EffectContext / passive / bracket work this set needs. -->
_None identified yet_

### How to work on this set
1. Download the set JSON:
   ```sh
   curl -L --create-dirs -o spirit/game/scripts/cards/$set_dir/$set_id.json https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/master/cards/en/$set_id.json
   ```
2. Generate the scripts and art (only once, because it overwrites existing scripts):
   ```sh
   python -m spirit.tools.import_set spirit/game/scripts/cards/$set_dir/$set_id.json --set-code $set_dir
   ```
3. Script the card logic for each card! (Make sure no use of `unimplemented` shows up, thats how our automatic tracker track progress)

4. Check:
   ```sh
   python -m spirit.tools.effect_smoke --set $set_dir --all
   ```

$cards_block
