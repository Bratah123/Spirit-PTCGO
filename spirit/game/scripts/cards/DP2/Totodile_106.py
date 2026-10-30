"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage

card = PokemonCardDef(guid='0690da86-c586-58e2-9a66-119655e7ac19', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name', display_name='Totodile', searchable_by=['Totodile', 'Basic', 'Totodile'], subtypes=['Basic'], collector_number=106, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=158, abilities=[Attack(title='Bite', cost={}, damage=10), Attack(title='Shining Fang', game_text='If the Defending Pokémon already has any damage counters on it, this attack does 10 damage plus 10 more damage.', cost={PokemonTypes.WATER: 1}, damage=10, damage_operator='+', effect=bonus_if(has_damage('defender'), 10, base=10))])
