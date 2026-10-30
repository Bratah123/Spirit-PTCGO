"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_gallade_6_psychic_cut,
    dp3_gallade_6_sonic_blade,
)

card = PokemonCardDef(guid='242d022a-c82a-5cb3-9e51-5841b23e7bac', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name', display_name='Gallade', searchable_by=['Gallade', 'Stage 2', 'Gallade'], subtypes=['Stage 2'], collector_number=6, set_code='DP3', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name', family_id=280, abilities=[Attack(title='Sonic Blade', game_text='Put damage counters on the Defending Pokémon until it is 50 HP away from being Knocked Out. If you do, your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, effect=dp3_gallade_6_sonic_blade()), Attack(title='Psychic Cut', game_text='You may choose as many of your face-down Prize cards as you like and put them face up. If you do, this attack does 60 damage plus 20 more damage for each Prize card you chose. (These cards remain face up for the rest of the game.)', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp3_gallade_6_psychic_cut())])
