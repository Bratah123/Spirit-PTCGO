from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on,
    damage_per,
    flip_or_nothing,
)


card = PokemonCardDef(
    guid="a31430b2-3a7d-5b1b-be01-9e607d89e2a1",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMachop.Name",
    display_name="Giovanni's Machop",
    searchable_by=["Giovanni's Machop", "Basic", "GiovannisMachop"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title="Chop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Fury Punch",
            game_text="Flip a coin. If heads, this attack does 20 damage times the number of damage counters on Giovanni's Machop.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="x",
            effect=flip_or_nothing(then=damage_per(damage_counters_on("self"), 20)),
        ),
    ],
)
