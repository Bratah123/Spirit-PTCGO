from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b399fcd4-7536-5bbb-a660-588d2050ed2b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaVSTAR.Name",
    display_name="Origin Forme Palkia VSTAR",
    searchable_by=["Origin Forme Palkia VSTAR", "VSTAR", "OriginFormePalkiaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=40,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    family_id=484,
    abilities=[
        Ability(
            title="Star Portal",
            game_text="During your turn, you may attach up to 3 Water Energy cards from your discard pile to your Water Pok\u00e9mon in any way you like. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Subspace Swell",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)