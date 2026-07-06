from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a214877-fad3-51c4-b34d-96b3648cd460",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Swim Freely",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Floe Return",
            game_text="Shuffle any amount of Water Energy from your Pok\u00e9mon into your deck. This attack does 40 damage for each card you shuffled into your deck in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)