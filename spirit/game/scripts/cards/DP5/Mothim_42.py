"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_mothim_42_disturbance_scales,
    dp5_mothim_42_get_help,
    dp5_mothim_42_quick_touch,
)

card = PokemonCardDef(guid='81ab7bd5-1030-5f57-a609-406c41ac8037', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name', display_name='Mothim', searchable_by=['Mothim', 'Stage 1', 'Mothim'], subtypes=['Stage 1'], collector_number=42, set_code='DP5', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name', family_id=414, abilities=[Ability(title='Disturbance Scales', game_text="Any damage done by attacks from your Pokémon to the Defending Pokémon isn't affected by Resistance.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_mothim_42_disturbance_scales(), activation=Activations.ONCE_PER_TURN), Attack(title='Get Help', game_text='Does 30 damage times the number of different types of Wormadam on your Bench.', cost={PokemonTypes.GRASS: 1}, damage=30, damage_operator='x', effect=dp5_mothim_42_get_help()), Attack(title='Quick Touch', game_text='You may switch Mothim with 1 of your Benched Pokémon. If you do, move as many Energy cards attached to Mothim as you like to the new Active Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp5_mothim_42_quick_touch())])
