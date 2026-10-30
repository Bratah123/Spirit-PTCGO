"""STUB: effect not implemented — do not guess mechanics.
Misdreavus (EX12 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    deep_sleep_passive,
    dream_eater,
    return_trance,
)

card = PokemonCardDef(guid='958be97e-0208-5fae-8bc6-18fd80686e5d', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name', display_name='Misdreavus', searchable_by=['Misdreavus', 'Basic', 'Misdreavus'], subtypes=['Basic'], collector_number=40, set_code='EX12', rarity=Rarities.Uncommon, hp=50, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.FIGHTING, family_id=200, abilities=[Ability(title='Deep Sleep', game_text='As long as Misdreavus is your Active Pokémon, each player flips 2 coins for his or her Pokémon that is Asleep between turns. If either coin is tails, that Pokémon is still Asleep.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=deep_sleep_passive()), Attack(title='Return Trance', game_text='Return an Energy card attached to Misdreavus to your hand. The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=return_trance()), Attack(title='Dream Eater', game_text='If the Defending Pokémon is not Asleep, this attack does nothing.', cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=dream_eater(50))])
