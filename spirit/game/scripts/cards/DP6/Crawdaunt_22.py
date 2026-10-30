"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_crawdaunt_22_gripthrow,
    dp6_crawdaunt_22_prop_up_pinchers,
)

card = PokemonCardDef(guid='f4c301af-f23c-5185-bfa6-fecaf8c2fe19', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name', display_name='Crawdaunt', searchable_by=['Crawdaunt', 'Stage 1', 'Crawdaunt'], subtypes=['Stage 1'], collector_number=22, set_code='DP6', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name', family_id=341, abilities=[Attack(title='Gripthrow', game_text='Flip a coin. If heads, your opponent returns the Defending Pokémon and all cards attached to it to his or her hand.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, effect=dp6_crawdaunt_22_gripthrow()), Attack(title='Prop-up Pinchers', game_text='If Crawdaunt has a Technical Machine card attached to it, this attack does 50 damage plus 30 more damage.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=dp6_crawdaunt_22_prop_up_pinchers())])
