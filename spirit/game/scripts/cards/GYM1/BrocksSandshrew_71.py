from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="0d610247-135b-5b20-8ecb-68971bdcc374",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksSandshrew.Name",
    display_name="Brock's Sandshrew",
    searchable_by=["Brock's Sandshrew", "Basic", "BrocksSandshrew"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=27,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to Brock's Sandshrew during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Rolling Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
