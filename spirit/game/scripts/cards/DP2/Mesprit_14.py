"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    teleportation_burst,
    upper_material_passive,
)

card = PokemonCardDef(guid='3e9e5abd-b11a-5035-9904-cdddc842e4aa', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name', display_name='Mesprit', searchable_by=['Mesprit', 'Basic', 'Mesprit'], subtypes=['Basic'], collector_number=14, set_code='DP2', rarity=Rarities.RareHolo, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=481, abilities=[Ability(title='Upper Material', game_text="If you have Uxie and Azelf in play, the Retreat Cost for each Uxie, Mesprit, and Azelf (both yours and your opponent's) is 0.", ability_type=AbilityTypes.POKE_BODY, passive=upper_material_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Teleportation Burst', game_text='You may switch Mesprit with 1 of your Benched Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=teleportation_burst(30))])
