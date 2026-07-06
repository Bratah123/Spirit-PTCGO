from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="02162caa-84a9-5c4e-b5e7-646c8d4b3deb",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkVSTAR.Name",
    display_name="Hisuian Zoroark VSTAR",
    searchable_by=["Hisuian Zoroark VSTAR", "VSTAR", "HisuianZoroarkVSTAR"],
    subtypes=["VSTAR"],
    collector_number=147,
    set_code="SWSH11",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkV.Name",
    family_id=571,
    abilities=[
        Ability(
            title="Phantom Star",
            game_text="During your turn, you may discard your hand and draw 7 cards. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Ticking Curse",
            game_text="This attack does 50 damage for each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)