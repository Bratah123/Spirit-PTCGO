"""STUB: effect not implemented — do not guess mechanics.
Tropius (EX5 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import fruition

card = PokemonCardDef(
    guid="cd40e3ac-a259-5bc3-b1fd-7c8b3610329b",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Fruition",
            game_text="Move 1 Energy card attached to Tropius to another of your Pok\u00e9mon and remove 4 damage counters from that Pok\u00e9mon (all if there are less than 4).",
            cost={PokemonTypes.GRASS: 1},
            effect=fruition(40),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)