from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="21d2cbae-91ac-58e3-a1e4-0c90114d0027",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorV.Name",
    display_name="Scizor V",
    searchable_by=["Scizor V", "Basic", "V", "ScizorV"],
    subtypes=["Basic", "V"],
    collector_number=118,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=212,
    abilities=[
        Attack(
            title="Hack Off",
            game_text="Discard a Pok\u00e9mon Tool and a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)