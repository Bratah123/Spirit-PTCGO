from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee12ce45-5b07-5b1c-9a65-f8373969fcc9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArctovishV.Name",
    display_name="Arctovish V",
    searchable_by=["Arctovish V", "Basic", "V", "ArctovishV"],
    subtypes=["Basic", "V"],
    collector_number=176,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=883,
    abilities=[
        Attack(
            title="Ancient Freeze",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon V or a Pok\u00e9mon-GX, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)