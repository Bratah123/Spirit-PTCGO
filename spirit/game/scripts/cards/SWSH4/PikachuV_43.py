from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7fe2c2e-4286-5b79-a956-392b78dcea66",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=43,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for up to 2 Lightning Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)