from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="719ef6ce-7bb8-527d-b401-7b4db84e19ca",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Ability(
            title="Hustle Bark",
            game_text="If your opponent has any Pok\u00e9mon VMAX in play, this Pok\u00e9mon's attacks cost ColorlessColorlessColorless less.",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)