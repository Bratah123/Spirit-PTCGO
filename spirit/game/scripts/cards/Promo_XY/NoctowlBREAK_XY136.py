"""STUB: effect not implemented — do not guess mechanics.
Noctowl BREAK (Promo_XY #XY136): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04d44328-1750-5b76-bff9-bd42715bc00d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoctowlBREAK.Name",
    display_name="Noctowl BREAK",
    searchable_by=["Noctowl BREAK", "BREAK", "NoctowlBREAK"],
    subtypes=["BREAK"],
    collector_number=136,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    family_id=164,
    abilities=[
        Attack(
            title="Night Scan",
            game_text="Your opponent reveals his or her hand. This attack does 30 more damage for each Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)