"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.ex import (
    delta_reactor_passive,
)

card = PokemonCardDef(guid='b38b1e11-fa7c-5948-a4b9-d5ec70a84c41', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name', display_name='Gyarados δ', searchable_by=['Gyarados δ', 'Stage 1', 'Gyarados'], subtypes=['Stage 1'], collector_number=8, set_code='EX13', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name', family_id=130, abilities=[Ability(title='Delta Reactor', game_text='As long as any Stadium card with Holon in its name is in play, each of your Pokémon that has δ on its card does 10 more damage to the Defending Pokémon (before applying Weakness and Resistance).', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=delta_reactor_passive(10)), Attack(title='Hyper Beam', game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=discard_opponent_energy_attack(1, flip=True)), Attack(title='Heavy Impact', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3}, damage=80)])
