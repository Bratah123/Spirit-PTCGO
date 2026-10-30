"""STUB: effect not implemented — do not guess mechanics.
Wobbuffet (EX12 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    grind_energy,
    shadow_tag_delayed,
    stages_retreat_tax_passive,
)

card = PokemonCardDef(guid='6f6d59a8-bcc0-5d4c-b7ed-3d0472a3e276', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name', display_name='Wobbuffet', searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'], subtypes=['Basic'], collector_number=28, set_code='EX12', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=202, abilities=[Ability(title='Stages of Evolution', game_text='As long as Wobbuffet is an Evolved Pokémon, your opponent pays Colorless more to retreat his or her Active Pokémon.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=stages_retreat_tax_passive(1)), Attack(title='Grind', game_text='Does 10 damage times the amount of Energy attached to Wobbuffet.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=grind_energy(10)), Attack(title='Shadow Tag', game_text="Put 7 damage counters on the Defending Pokémon at the end of your opponent's next turn.", cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, effect=shadow_tag_delayed(7))])
