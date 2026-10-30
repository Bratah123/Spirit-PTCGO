"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    bind_pulse_no_energy_attach,
    downer_material_passive,
)

card = PokemonCardDef(guid='a732a9ed-c611-529c-9599-2db189ce9788', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name', display_name='Azelf', searchable_by=['Azelf', 'Basic', 'Azelf'], subtypes=['Basic'], collector_number=4, set_code='DP2', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=482, abilities=[Ability(title='Downer Material', game_text="If you have Uxie and Mesprit in play, the attack cost of each of your opponent's Basic Pokémon's attacks is Colorless more. You can't use more than 1 Downer Material Poké-Body each turn.", ability_type=AbilityTypes.POKE_BODY, passive=downer_material_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Bind Pulse', game_text="During your opponent's next turn, your opponent can't attach any Special Energy cards from his or her hand to any of his or her Pokémon.", cost={PokemonTypes.PSYCHIC: 1}, damage=10, effect=bind_pulse_no_energy_attach())])
