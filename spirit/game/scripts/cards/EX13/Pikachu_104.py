"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    spring_back,
)

card = PokemonCardDef(guid='51fe9552-a34f-5523-b123-f58a42e882b4', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', display_name='Pikachu ★', searchable_by=['Pikachu ★', 'Basic', 'Star', 'Pikachu'], subtypes=['Basic', 'Star'], collector_number=104, set_code='EX13', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=25, abilities=[Attack(title='Thundershock', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=condition_attack(SpecialConditions.PARALYZED, flip=True)), Attack(title='Spring Back', game_text='If your opponent has only 1 Prize card left, this attack does 20 damage plus 50 more damage.', cost={PokemonTypes.LIGHTNING: 2}, damage=20, damage_operator='+', effect=spring_back(20, 50))])
