"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_scizor_29_special_blow,
    dp5_scizor_29_x_scissor,
)

card = PokemonCardDef(guid='cf1730da-e9b6-5462-89e0-5d32300f3a49', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name', display_name='Scizor', searchable_by=['Scizor', 'Stage 1', 'Scizor'], subtypes=['Stage 1'], collector_number=29, set_code='DP5', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name', family_id=123, abilities=[Attack(title='Special Blow', game_text='If the Defending Pokémon has any Special Energy cards attached to it, this attack does 30 damage plus 50 more damage.', cost={PokemonTypes.METAL: 1}, damage=30, damage_operator='+', effect=dp5_scizor_29_special_blow()), Attack(title='X-Scissor', game_text='Flip a coin. If heads, this attack does 50 damage plus 40 more damage.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp5_scizor_29_x_scissor())])
