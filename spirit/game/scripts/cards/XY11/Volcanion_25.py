"""STUB: effect not implemented — do not guess mechanics.
Volcanion (XY11 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7360839-d6bf-5670-8091-fee67ddde2e1",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Power Heater",
            game_text="Choose 2 of your Benched Pok\u00e9mon. Attach a Fire Energy card from your discard pile to each of those Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)