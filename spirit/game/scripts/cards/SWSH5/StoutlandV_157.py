from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3bcd0555-e43f-55c0-b490-d2660a763208",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StoutlandV.Name",
    display_name="Stoutland V",
    searchable_by=["Stoutland V", "Basic", "V", "StoutlandV"],
    subtypes=["Basic", "V"],
    collector_number=157,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=508,
    abilities=[
        Attack(
            title="Double Dip Fangs",
            game_text="If your opponent's Basic Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=unimplemented,
        ),
    ],
)