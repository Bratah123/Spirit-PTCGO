"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_regice_36_ice_reflect,
    dp6_regice_36_regi_move,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='ea1646f9-88d9-5cdf-b63c-df3d4bb93c86', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name', display_name='Regice', searchable_by=['Regice', 'Basic', 'Regice'], subtypes=['Basic'], collector_number=36, set_code='DP6', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.METAL, family_id=378, abilities=[Ability(title='Regi Move', game_text="Once during your turn (before your attack), you may use this power. Discard 2 cards from your hand and choose 1 of your opponent's Active Pokémon that isn't an Evolved Pokémon. Then, your opponent switches that Pokémon with 1 of his or her Benched Pokémon. This power can't be used if Regice is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp6_regice_36_regi_move(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Ice Reflect', game_text="If Regice was damaged by an attack during your opponent's last turn, the Defending Pokémon is now Paralyzed.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=dp6_regice_36_ice_reflect())])
