"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    call_in_draw_chimecho,
    strange_bell,
)

card = PokemonCardDef(guid='d1095ab3-3d69-5c6c-84dd-08b2a816f604', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name', display_name='Chimecho', searchable_by=['Chimecho', 'Basic', 'Chimecho'], subtypes=['Basic'], collector_number=22, set_code='DP2', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=358, abilities=[Attack(title='Call In', game_text='Draw a card. If Chingling is anywhere under Chimecho, draw 2 more cards.', cost={PokemonTypes.COLORLESS: 1}, effect=call_in_draw_chimecho()), Attack(title='Strange Bell', game_text='If the Defending Pokémon is a Basic Pokémon, that Pokémon is now Confused.', cost={PokemonTypes.PSYCHIC: 1}, damage=20, effect=strange_bell(20))])
