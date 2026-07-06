from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="539986ca-f4c6-5809-8ec9-73b4895d501e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    display_name="Galarian Linoone",
    searchable_by=["Galarian Linoone", "Stage 1", "GalarianLinoone"],
    subtypes=["Stage 1"],
    collector_number=160,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
    ],
)