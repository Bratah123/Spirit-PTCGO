"""STUB: effect not implemented — do not guess mechanics.
Phantump (XY1 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59f52276-0520-55e7-b058-eff8261b43d8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic", "Phantump"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=708,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)