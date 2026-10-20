"""STUB: effect not implemented — do not guess mechanics.
Electrike (XY5 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ebeed981-b129-579c-99ca-8986f5c46c85",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=309,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)