from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4b957a8-0f26-5aeb-b968-294fdf0bee7e",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="CEL25",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=889,
    abilities=[
        Ability(
            title="Growl of the Shield",
            game_text="All of your Fighting Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon VMAX (after applying Weakness and Resistance). You can't apply more than 1 Growl of the Shield Ability at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)