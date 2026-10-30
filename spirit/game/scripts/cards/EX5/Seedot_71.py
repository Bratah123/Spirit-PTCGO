"""STUB: effect not implemented — do not guess mechanics.
Seedot (EX5 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


from spirit.game.card_effects.ex import seedot_growth

card = PokemonCardDef(
    guid="339b3846-adc2-5d39-adbe-b01cab0cd334",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    display_name="Seedot",
    searchable_by=["Seedot", "Basic", "Seedot"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=273,
    abilities=[
        Attack(
            title="Growth Spurt",
            game_text="Attach a Grass Energy card from your hand to Seedot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=seedot_growth(),
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)