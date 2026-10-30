"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    leaf_tornado,
    sprouting_attach_grass,
)

card = PokemonCardDef(guid='ffad56ef-7c04-5b05-b7e2-345c18f2aa23', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name', display_name='Celebi', searchable_by=['Celebi', 'Basic', 'Celebi'], subtypes=['Basic'], collector_number=7, set_code='DP2', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=251, abilities=[Attack(title='Sprouting', game_text='Search your deck for a Grass Energy card and attach it to Celebi. Shuffle your deck afterward.', cost={}, effect=sprouting_attach_grass()), Attack(title='Leaf Tornado', game_text='You may move any number of basic Grass Energy cards attached to your Pokémon to your other Pokémon in any way you like.', cost={PokemonTypes.GRASS: 2}, damage=30, effect=leaf_tornado(30))])
