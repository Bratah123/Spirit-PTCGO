from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9db74d2d-4cae-5a15-b837-26eaa9dc9b5d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZapdosV.Name",
    display_name="Galarian Zapdos V",
    searchable_by=["Galarian Zapdos V", "Basic", "V", "GalarianZapdosV"],
    subtypes=["Basic", "V"],
    collector_number=80,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=145,
    abilities=[
        Ability(
            title="Fighting Instinct",
            game_text="This Pok\u00e9mon's attacks cost Colorless less for each of your opponent's Pok\u00e9mon V in play.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Kick",
            game_text="Before doing damage, discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=unimplemented,
        ),
    ],
)