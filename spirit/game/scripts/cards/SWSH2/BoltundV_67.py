from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f009bbd-8ab9-5770-af46-ef9f63b03109",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    display_name="Boltund V",
    searchable_by=["Boltund V", "Basic", "V", "BoltundV"],
    subtypes=["Basic", "V"],
    collector_number=67,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=836,
    abilities=[
        Attack(
            title="Electrify",
            game_text="Search your deck for up to 2 Lightning Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bolt Storm",
            game_text="This attack does 30 more damage for each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)