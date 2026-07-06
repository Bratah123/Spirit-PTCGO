from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce99ea43-7ce3-57c6-9c1f-c7cb7e38938a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonVMAX.Name",
    display_name="Inteleon VMAX",
    searchable_by=["Inteleon VMAX", "VMAX", "Rapid Strike", "InteleonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=79,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    family_id=818,
    abilities=[
        Ability(
            title="Double Gunner",
            game_text="You must discard a Water Energy card from your hand in order to use this Ability. Once during your turn, you may choose 2 of your opponent's Benched Pok\u00e9mon and put 2 damage counters on each of them.",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Spiral",
            game_text="You may put an Energy attached to this Pok\u00e9mon into your hand. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)