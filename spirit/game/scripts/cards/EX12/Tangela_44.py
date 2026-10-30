"""STUB: effect not implemented — do not guess mechanics.
Tangela (EX12 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import magma_ring_no_retreat
from spirit.game.card_effects.ex import (
    entangling_vines_lock_basic,
    reactive_healing_on_attach,
)

card = PokemonCardDef(guid='f2bb927d-a029-58aa-9846-b7ebdef44b38', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name', display_name='Tangela', searchable_by=['Tangela', 'Basic', 'Tangela'], subtypes=['Basic'], collector_number=44, set_code='EX12', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, family_id=114, abilities=[Ability(title='Reactive Healing', game_text='Whenever you attach a React Energy card from your hand to Tangela, remove all damage counters from Tangela.', ability_type=AbilityTypes.POKE_BODY, effect=reactive_healing_on_attach(), trigger=Triggers.ON_ENERGY_ATTACHED), Attack(title='Entangling Vines', game_text="If the Defending Pokémon is a Basic Pokémon, that Pokémon can't attack during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=entangling_vines_lock_basic()), Attack(title='Gentle Wrap', game_text="The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=30, effect=magma_ring_no_retreat())])
