from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7256e884-9c4d-5004-aa26-cc71c361f26d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=212,
    set_code="SWSH1",
    rarity=Rarities.RareSecret,
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