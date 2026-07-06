from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2f7d8d20-2774-5675-88bc-69748b09faf6",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrapploctV.Name",
    display_name="Grapploct V",
    searchable_by=["Grapploct V", "Basic", "V", "GrapploctV"],
    subtypes=["Basic", "V"],
    collector_number=72,
    set_code="SWSH35",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=853,
    abilities=[
        Attack(
            title="Tie Up",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Moonsault Press",
            game_text="Flip a coin. If heads, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)