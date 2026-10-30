"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_gardevoir_7_psychic_lock,
    dp3_gardevoir_7_telepass,
)
from spirit.game.card_effects.ex import poke_power_condition

card = PokemonCardDef(guid='61d1abe2-770b-510e-a426-8f36f38207dc', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name', display_name='Gardevoir', searchable_by=['Gardevoir', 'Stage 2', 'Gardevoir'], subtypes=['Stage 2'], collector_number=7, set_code='DP3', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name', family_id=280, abilities=[Ability(title='Telepass', game_text="Once during your turn (before your attack), you may search your opponent's discard pile for a Supporter card and use the effect of that card as the effect of this power. (The Supporter card remains in your opponent's discard pile.) You can't use more than 1 Telepass Poké-Power each turn. This power can't be used if Gardevoir is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=dp3_gardevoir_7_telepass(), activation=Activations.ONCE_PER_TURN, condition=poke_power_condition()), Attack(title='Psychic Lock', game_text="During your opponent's next turn, your opponent can't use any Poké-Powers on his or her Pokémon.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp3_gardevoir_7_psychic_lock())])
