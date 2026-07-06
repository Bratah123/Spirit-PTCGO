from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77fc6d36-e8c2-52f9-81eb-ac0ebe6ad0ae",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremVMAX.Name",
    display_name="Kyurem VMAX",
    searchable_by=["Kyurem VMAX", "VMAX", "KyuremVMAX"],
    subtypes=["VMAX"],
    collector_number=197,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremV.Name",
    family_id=646,
    abilities=[
        Ability(
            title="Glaciated World",
            game_text="Once during your turn, you may discard the top card of your deck. If that card is a Water Energy card, attach it to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Frost",
            game_text="You may discard any amount of Water Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)