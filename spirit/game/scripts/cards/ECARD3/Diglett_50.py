from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="e6cef32e-f5b0-5916-bde8-2177a4c804b8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=50,
    abilities=[
        Attack(
            title="Burrow",
            game_text="Flip a coin. If heads, prevent all damage done by attacks to Diglett during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=flip_protection(prevent=True),
        ),
    ],
)
