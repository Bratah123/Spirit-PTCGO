from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38ab5e40-9343-5775-b3be-76189b8b3ffc",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    display_name="Hisuian Growlithe",
    searchable_by=["Hisuian Growlithe", "Basic", "HisuianGrowlithe"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=58,
    abilities=[
        Attack(
            title="Defensive Posture",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)