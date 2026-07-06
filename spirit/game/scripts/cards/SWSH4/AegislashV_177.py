from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4428f9d9-dd5d-5ebb-9b53-c19aa10e9c13",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashV.Name",
    display_name="Aegislash V",
    searchable_by=["Aegislash V", "Basic", "V", "AegislashV"],
    subtypes=["Basic", "V"],
    collector_number=177,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=681,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)