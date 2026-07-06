from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aed7ca71-7937-55d0-84ee-b65070ea7f82",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic", "Wooloo"],
    subtypes=["Basic"],
    collector_number=222,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)