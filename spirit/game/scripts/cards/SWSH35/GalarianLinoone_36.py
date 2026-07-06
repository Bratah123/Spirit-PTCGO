from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f189dc20-9f3b-5806-b976-5d0b240b0c3c",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    display_name="Galarian Linoone",
    searchable_by=["Galarian Linoone", "Stage 1", "GalarianLinoone"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH35",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)