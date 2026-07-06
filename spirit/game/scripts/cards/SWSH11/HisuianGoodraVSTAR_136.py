from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51288336-0dab-5ef6-86b5-d8d77f56ec12",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodraVSTAR.Name",
    display_name="Hisuian Goodra VSTAR",
    searchable_by=["Hisuian Goodra VSTAR", "VSTAR", "HisuianGoodraVSTAR"],
    subtypes=["VSTAR"],
    collector_number=136,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodraV.Name",
    family_id=706,
    abilities=[
        Ability(
            title="Moisture Star",
            game_text="During your turn, you may heal all damage from this Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Rolling Iron",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 80 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)