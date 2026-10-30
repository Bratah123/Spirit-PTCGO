"""STUB: effect not implemented — do not guess mechanics.
Torkoal (EX12 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    cry_for_help,
    fireworks_discard_fire,
)

card = PokemonCardDef(guid='41668f34-930f-5d6d-8c71-f78eeec6a977', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name', display_name='Torkoal', searchable_by=['Torkoal', 'Basic', 'Torkoal'], subtypes=['Basic'], collector_number=27, set_code='EX12', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=324, abilities=[Attack(title='Cry for Help', game_text='Search your deck for a Fire Pokémon (excluding Pokémon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=cry_for_help(PokemonTypes.FIRE)), Attack(title='Fireworks', game_text='Flip a coin. If tails, discard a Fire Energy attached to Torkoal.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=fireworks_discard_fire())])
