from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import detect_flip_protect


card = PokemonCardDef(
    guid="c2b4d8c6-6dfe-5539-891b-c3b13af57d13",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose δ",
    searchable_by=["Zangoose \u03b4", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="POP5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Detect",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Zangoose during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=detect_flip_protect(),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
