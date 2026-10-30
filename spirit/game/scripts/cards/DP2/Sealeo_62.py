"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='d5d38f6f-ddf7-5cf2-9524-7f4d1f2b36a4', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name', display_name='Sealeo', searchable_by=['Sealeo', 'Stage 1', 'Sealeo'], subtypes=['Stage 1'], collector_number=62, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name', family_id=363, abilities=[Attack(title='Ice Rider', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2}, effect=snipe_attack(30, pool='any'))])
