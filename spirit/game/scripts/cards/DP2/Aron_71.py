"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    steel_tackle_recoil,
)

card = PokemonCardDef(guid='bcd87518-3f57-5548-af1f-0a732004feea', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name', display_name='Aron', searchable_by=['Aron', 'Basic', 'Aron'], subtypes=['Basic'], collector_number=71, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=304, abilities=[Attack(title='Steel Tackle', game_text='Aron does 10 damage to itself.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=steel_tackle_recoil(30, 10))])
