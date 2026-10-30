"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    hard_face,
)
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(guid='8df17882-fc72-5962-b8eb-e8a2273757d7', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name', display_name='Shieldon', searchable_by=['Shieldon', 'Stage 1', 'Shieldon'], subtypes=['Stage 1'], collector_number=8, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.ArmorFossil.Name', family_id=410, abilities=[Attack(title='Hard Face', game_text="During your opponent's next turn, any damage done to Shieldon by attacks is reduced by 20 (after applying Weakness and Resistance).", cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=hard_face(20)), Attack(title='Shield Attack', game_text='Flip a coin. If heads, this attack does 40 damage plus 20 more damage.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=flip_bonus(20))])
