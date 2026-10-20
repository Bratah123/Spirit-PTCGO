"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Poochyena (TATM #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f9e240f-bce6-5374-8735-78a6832d3e91",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    display_name="Team Magma's Poochyena",
    searchable_by=["Team Magma's Poochyena", "Basic", "TeamMagmasPoochyena"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=261,
    abilities=[
        Attack(
            title="Infiltrate",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)