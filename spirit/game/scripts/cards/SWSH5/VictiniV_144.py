from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e35c2d0-1962-57ac-9718-e227df1280cd",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    display_name="Victini V",
    searchable_by=["Victini V", "Basic", "V", "VictiniV"],
    subtypes=["Basic", "V"],
    collector_number=144,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V Bullet",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Flare Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)