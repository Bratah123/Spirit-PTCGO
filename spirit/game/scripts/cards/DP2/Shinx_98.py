"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    plasma_attach_lightning,
)

card = PokemonCardDef(guid='703223f8-e55a-5ce8-8e8c-5519efa4d3f4', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name', display_name='Shinx', searchable_by=['Shinx', 'Basic', 'Shinx'], subtypes=['Basic'], collector_number=98, set_code='DP2', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=403, abilities=[Attack(title='Plasma', game_text='Flip a coin. If heads, search your discard pile for a Lightning Energy card and attach it to Shinx.', cost={PokemonTypes.LIGHTNING: 1}, damage=10, effect=plasma_attach_lightning())])
