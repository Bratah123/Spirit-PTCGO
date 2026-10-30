"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(guid='1bc47d21-ac02-5cc8-8122-654ce1f8340e', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name', display_name='Spinarak', searchable_by=['Spinarak', 'Basic', 'Spinarak'], subtypes=['Basic'], collector_number=103, set_code='DP2', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=167, abilities=[Attack(title='Impound', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=magma_ring_no_retreat()), Attack(title='Double Scratch', game_text='Flip 2 coins. This attack does 20 damage times the number of heads.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=flip_damage(2, per_heads=20))])
