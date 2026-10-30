"""Croagunk (POP9 #7)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flip_discard_random_from_opponent_hand, partner_drain_heal


card = PokemonCardDef(
    guid="b12194de-6831-5eb5-a621-e4c010d81b06",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic", "Croagunk"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=flip_discard_random_from_opponent_hand()
        ),
        Attack(
            title="Nimble",
            game_text="If you have Turtwig in play, remove from Croagunk the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=partner_drain_heal('Turtwig')
        ),
    ]
)