from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd64b9be-7f7a-5a13-a0ae-4b88684f9b29",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionV.Name",
    display_name="Drapion V",
    searchable_by=["Drapion V", "Basic", "V", "DrapionV"],
    subtypes=["Basic", "V"],
    collector_number=182,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=452,
    abilities=[
        Ability(
            title="Wild Style",
            game_text="This Pok\u00e9mon's attacks cost Colorless less for each of your opponent's Single Strike, Rapid Strike, and Fusion Strike Pok\u00e9mon in play.",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamic Tail",
            game_text="This attack also does 60 damage to 1 of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=190,
            effect=unimplemented,
        ),
    ],
)