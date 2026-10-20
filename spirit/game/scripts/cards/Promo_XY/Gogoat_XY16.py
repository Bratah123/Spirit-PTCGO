"""STUB: effect not implemented — do not guess mechanics.
Gogoat (Promo_XY #XY16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91735d3c-c6ea-5183-9e1f-dc7229cc45d8",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name",
    display_name="Gogoat",
    searchable_by=["Gogoat", "Stage 1", "Gogoat"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    family_id=672,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Forest Press",
            game_text="Flip a coin for each Grass Energy attached to this Pok\u00e9mon. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)