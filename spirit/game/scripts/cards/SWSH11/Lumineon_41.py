from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5b6d4a4-c116-50c7-92d8-539f61853163",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name",
    display_name="Lumineon",
    searchable_by=["Lumineon", "Stage 1", "Lumineon"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    family_id=456,
    abilities=[
        Attack(
            title="Swim Freely",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)