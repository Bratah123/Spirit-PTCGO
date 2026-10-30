"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    offensive_needle,
    sticky_no_retreat_passive,
)

card = PokemonCardDef(guid='076b0394-112e-5120-9fd6-39e6ff60c63a', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name', display_name='Ariados', searchable_by=['Ariados', 'Stage 1', 'Ariados'], subtypes=['Stage 1'], collector_number=20, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name', family_id=167, abilities=[Ability(title='Sticky', game_text="The Retreat Cost for each player's Pokémon (excluding Ariados) is Colorless more.", ability_type=AbilityTypes.POKE_BODY, passive=sticky_no_retreat_passive()), Attack(title='Offensive Needle', game_text='Flip a coin. If heads, the Defending Pokémon is now Poisoned. If tails, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=offensive_needle())])
