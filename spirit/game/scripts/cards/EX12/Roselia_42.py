"""STUB: effect not implemented — do not guess mechanics.
Roselia (EX12 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    flick_poison_switch,
    reactive_aroma_between_turns,
)

card = PokemonCardDef(guid='1d1dcf44-e942-5c93-ba4d-a88a362bb4b1', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name', display_name='Roselia', searchable_by=['Roselia', 'Basic', 'Roselia'], subtypes=['Basic'], collector_number=42, set_code='EX12', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=315, abilities=[Ability(title='Reactive Aroma', game_text="As long as Roselia has any React Energy cards attached to it, remove 1 damage counter from each of your Pokémon (excluding Pokémon-ex) that has any React Energy cards attached to it between turns. You can't use more than 1 Reactive Aroma Poké-Body each turn.", ability_type=AbilityTypes.POKE_BODY, effect=reactive_aroma_between_turns(), trigger=Triggers.BETWEEN_TURNS), Attack(title='Flick Poison', game_text="Switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch. The new Defending Pokémon is now Poisoned.", cost={PokemonTypes.COLORLESS: 1}, effect=flick_poison_switch())])
