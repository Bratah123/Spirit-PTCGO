"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_unownk_68_kind,
)

card = PokemonCardDef(guid='86dc7523-2d70-534a-931d-954c040e9b3a', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.UnownK.Name', display_name='Unown [K]', searchable_by=['Unown [K]', 'Basic', 'UnownK'], subtypes=['Basic'], collector_number=68, set_code='DP3', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=201, abilities=[Ability(title='Kind', game_text='Once during your turn (before your attack), you may remove 2 damage counters from 1 of the Defending Pokémon.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_unownk_68_kind(), activation=Activations.ONCE_PER_TURN), Attack(title='Hidden Power', cost={PokemonTypes.PSYCHIC: 1}, damage=20)])
