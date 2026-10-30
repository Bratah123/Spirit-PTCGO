"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_kingdra_7_aqua_stream,
    dp6_kingdra_7_dragon_pump,
)

card = PokemonCardDef(guid='0567474d-c7bf-55fa-8d4a-ebcd474e98e0', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name', display_name='Kingdra', searchable_by=['Kingdra', 'Stage 2', 'Kingdra'], subtypes=['Stage 2'], collector_number=7, set_code='DP6', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name', family_id=116, abilities=[Attack(title='Aqua Stream', game_text='Search your discard pile for as many Water Energy cards as you like, show them to your opponent, and this attack does 10 damage for each Water Energy card you chose. Put those cards on top of your deck. Shuffle your deck afterward.', cost={}, damage=10, damage_operator='x', effect=dp6_kingdra_7_aqua_stream()), Attack(title='Dragon Pump', game_text="You may discard 2 cards from your hand. If you do, this attack does 40 damage plus 20 more damage and does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 1}, damage=40, damage_operator='+', effect=dp6_kingdra_7_dragon_pump())])
