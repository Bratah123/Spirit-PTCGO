"""STUB: effect not implemented — do not guess mechanics.
Mew (EX12 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    link_blast,
    type_change_copy_defending,
)

card = PokemonCardDef(guid='cc7b0b85-53aa-539b-ae35-1763d2b02dcb', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name', display_name='Mew', searchable_by=['Mew', 'Basic', 'Mew'], subtypes=['Basic'], collector_number=10, set_code='EX12', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=151, abilities=[Ability(title='Type Change', game_text="Once during your turn (before your attack), you may choose 1 of the Defending Pokémon. Mew is the same type as that Pokémon (all if that Pokémon is more than 1 type) until the end of your turn. This power can't be used if Mew is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=type_change_copy_defending(), activation=Activations.ONCE_PER_TURN), Attack(title='Link Blast', game_text="If Mew and the Defending Pokémon have a different amount of Energy attached to them, this attack's base damage is 20 instead of 50.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=link_blast(50, 20))])
