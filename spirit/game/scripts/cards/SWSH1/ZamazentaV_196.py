from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aaae6968-9dcc-5b93-970a-7af10408f106",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=196,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Dauntless Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon VMAX.",
            effect=unimplemented,
        ),
        Attack(
            title="Assault Tackle",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)