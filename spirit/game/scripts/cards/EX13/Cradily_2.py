"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    harsh_fluid_delayed,
)

card = PokemonCardDef(guid='b5d3e3fe-4846-54f8-a78a-fca8aec12cf1', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name', display_name='Cradily δ', searchable_by=['Cradily δ', 'Stage 2', 'Cradily'], subtypes=['Stage 2'], collector_number=2, set_code='EX13', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name', family_id=346, abilities=[Attack(title='Harsh Fluid', game_text="Put 5 damage counters on the Defending Pokémon at the end of your opponent's next turn.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=harsh_fluid_delayed(5)), Attack(title='Poison Tentacles', game_text='The Defending Pokémon is now Poisoned.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=condition_attack(SpecialConditions.POISONED))])
