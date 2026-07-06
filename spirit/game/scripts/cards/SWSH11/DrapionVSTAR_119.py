from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea4871db-def6-5344-9b57-4773b6046920",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionVSTAR.Name",
    display_name="Drapion VSTAR",
    searchable_by=["Drapion VSTAR", "VSTAR", "DrapionVSTAR"],
    subtypes=["VSTAR"],
    collector_number=119,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionV.Name",
    family_id=452,
    abilities=[
        Ability(
            title="Hazard Star",
            game_text="During your turn, you may make your opponent's Active Pok\u00e9mon Paralyzed and Poisoned. During Pok\u00e9mon Checkup, put 3 damage counters on that Pok\u00e9mon instead of 1. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Big Bang Arm",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)