from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b3f9833-676f-5184-a3d1-028d2a83db1d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianWeezing.Name",
    display_name="Galarian Weezing",
    searchable_by=["Galarian Weezing", "Stage 1", "GalarianWeezing"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Energy Factory",
            game_text="Each basic Darkness Energy attached to your Pok\u00e9mon that have \"Weezing\" in their name provides DarknessDarkness Energy. You can't apply more than 1 Energy Factory Ability at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)