"""STUB: effect not implemented — do not guess mechanics.
Muk (EX12 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    poison_ring,
    stench_no_powers_passive,
)

card = PokemonCardDef(guid='60f7459d-84e6-583c-84dd-735ebd7828df', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name', display_name='Muk', searchable_by=['Muk', 'Stage 1', 'Muk'], subtypes=['Stage 1'], collector_number=11, set_code='EX12', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name', family_id=88, abilities=[Ability(title='Stench', game_text="As long as Muk is your Active Pokémon, each player's Pokémon can't use any Poké-Powers.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=stench_no_powers_passive()), Attack(title='Poison Ring', game_text="The Defending Pokémon is now Poisoned. The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=poison_ring()), Attack(title='Sludge Toss', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=50)])
