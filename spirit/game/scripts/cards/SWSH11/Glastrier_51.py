from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae268100-fbfc-59a1-b494-8cec412af018",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glastrier.Name",
    display_name="Glastrier",
    searchable_by=["Glastrier", "Basic", "Glastrier"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=896,
    abilities=[
        Attack(
            title="Freeze Down",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)