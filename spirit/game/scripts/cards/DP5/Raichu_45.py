"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp5_raichu_45_agility,
    dp5_raichu_45_thunderbolt,
)

card = PokemonCardDef(guid='e3118db6-86d7-549c-b54e-6b9904c9c65f', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name', display_name='Raichu', searchable_by=['Raichu', 'Stage 1', 'Raichu'], subtypes=['Stage 1'], collector_number=45, set_code='DP5', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', family_id=25, abilities=[Attack(title='Agility', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Raichu during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=dp5_raichu_45_agility()), Attack(title='Thunderbolt', game_text='Discard all Energy cards attached to Raichu.', cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=dp5_raichu_45_thunderbolt())])
