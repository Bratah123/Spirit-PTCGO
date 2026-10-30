"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.dp import (
    dp5_grotle_37_planting,
)

card = PokemonCardDef(guid='e03bc323-1474-5937-871c-6cff65bf517a', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name', display_name='Grotle', searchable_by=['Grotle', 'Stage 1', 'Grotle'], subtypes=['Stage 1'], collector_number=37, set_code='DP5', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name', family_id=387, abilities=[Attack(title='Planting', game_text='Attach a Grass Energy card from your hand to 1 of your Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp5_grotle_37_planting()), Attack(title='Body Slam', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
