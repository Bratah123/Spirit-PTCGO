"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    flamethrower_discard_fire,
    outrage_flip,
)

card = PokemonCardDef(guid='f74a5447-f27b-5960-bb6f-1252c7d0758e', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name', display_name='Rayquaza δ', searchable_by=['Rayquaza δ', 'Basic', 'Rayquaza'], subtypes=['Basic'], collector_number=26, set_code='EX13', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.COLORLESS, family_id=384, abilities=[Attack(title='Outrage', game_text='Flip a coin. If tails, this attack does nothing. If heads, this attack does 10 damage plus 10 more damage for each damage counter on Rayquaza.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=outrage_flip()), Attack(title='Flamethrower', game_text='Discard a Fire Energy attached to Rayquaza.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=flamethrower_discard_fire())])
