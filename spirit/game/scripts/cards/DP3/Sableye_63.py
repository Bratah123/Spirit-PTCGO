"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_sableye_63_rummage,
    dp3_sableye_63_shadow_sneak,
)

card = PokemonCardDef(guid='846dc824-7264-5822-992e-b660053046cf', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name', display_name='Sableye', searchable_by=['Sableye', 'Basic', 'Sableye'], subtypes=['Basic'], collector_number=63, set_code='DP3', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=302, abilities=[Attack(title='Rummage', game_text='Look at the top 5 cards of your deck. Choose as many Trainer cards as you like, show them to your opponent, and put them into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=dp3_sableye_63_rummage()), Attack(title='Shadow Sneak', game_text='If you and your opponent have a different number of Prize cards left, this attack does 20 damage plus 20 more damage.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp3_sableye_63_shadow_sneak())])
