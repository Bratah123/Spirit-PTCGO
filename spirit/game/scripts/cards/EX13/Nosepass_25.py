"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    rock_slide_bench2,
)

card = PokemonCardDef(guid='6c0a529e-aca8-5ffe-8b58-6e21de1972e4', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name', display_name='Nosepass', searchable_by=['Nosepass', 'Basic', 'Nosepass'], subtypes=['Basic'], collector_number=25, set_code='EX13', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.WATER, family_id=299, abilities=[Attack(title='Supersonic', game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.CONFUSED, flip=True)), Attack(title='Rock Slide', game_text="Does 10 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=rock_slide_bench2(10))])
