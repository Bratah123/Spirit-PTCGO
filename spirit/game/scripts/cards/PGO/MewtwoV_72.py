from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17788c8e-c675-52e8-aef1-79996fb495ed",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoV.Name",
    display_name="Mewtwo V",
    searchable_by=["Mewtwo V", "Basic", "V", "MewtwoV"],
    subtypes=["Basic", "V"],
    collector_number=72,
    set_code="PGO",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Transfer Break",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)