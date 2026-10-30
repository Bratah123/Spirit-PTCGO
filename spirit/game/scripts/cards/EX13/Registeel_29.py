"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.ex import (
    clear_body_passive,
)

card = PokemonCardDef(guid='7829dbe6-0b45-58f5-bd79-af95b19476af', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name', display_name='Registeel', searchable_by=['Registeel', 'Basic', 'Registeel'], subtypes=['Basic'], collector_number=29, set_code='EX13', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, family_id=379, abilities=[Ability(title='Clear Body', game_text="Registeel can't be affected by any Special Conditions.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=clear_body_passive()), Attack(title='Hyper Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1}, damage=30, effect=discard_opponent_energy_attack(1, flip=True))])
