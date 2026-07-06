from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37d3427f-d90e-5263-9802-d5030ce5ae37",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonV.Name",
    display_name="Flareon V",
    searchable_by=["Flareon V", "Basic", "V", "Single Strike", "FlareonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=169,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Attack(
            title="Flaming Breath",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Column",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)