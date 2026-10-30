from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import heavy_metal_flip


card = PokemonCardDef(
    guid="62107479-5597-5302-a813-0443326c2b60",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu δ",
    searchable_by=["Pikachu \u03b4", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Electric Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Heavy Metal",
            game_text="Flip a coin for each Metal Energy attached to Pikachu. This attack does 10 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=heavy_metal_flip(10, 20),
        ),
    ],
)
