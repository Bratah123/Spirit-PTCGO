"""STUB: effect not implemented — do not guess mechanics.
Wurmple (EX12 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    poison_payback_on_damaged,
    string_pull_switch,
)

card = PokemonCardDef(guid='c87b51bf-698b-56b8-a06d-d607a32493f9', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name', display_name='Wurmple', searchable_by=['Wurmple', 'Basic', 'Wurmple'], subtypes=['Basic'], collector_number=70, set_code='EX12', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=265, abilities=[Ability(title='Poison Payback', game_text="If Wurmple is your Active Pokémon and is damaged by an opponent's attack (even if Wurmple is Knocked Out), the Attacking Pokémon is now Poisoned.", ability_type=AbilityTypes.POKE_BODY, effect=poison_payback_on_damaged(), trigger=Triggers.ON_DAMAGED_BY_ATTACK), Attack(title='String Pull', game_text="Switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch.", cost={PokemonTypes.COLORLESS: 1}, effect=string_pull_switch())])
