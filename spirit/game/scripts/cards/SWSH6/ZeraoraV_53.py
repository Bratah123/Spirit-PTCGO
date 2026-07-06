from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b48e308d-0f44-5423-ade8-47bbe16f48c3",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    display_name="Zeraora V",
    searchable_by=["Zeraora V", "Basic", "V", "Rapid Strike", "ZeraoraV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=53,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Cross Fist",
            game_text="If 1 of your other Rapid Strike Pok\u00e9mon used an attack during your last turn, this attack also does 160 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)