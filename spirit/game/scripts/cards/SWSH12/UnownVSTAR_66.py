from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db5a6a5e-0350-58b3-955c-8dd6868d1ab3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownVSTAR.Name",
    display_name="Unown VSTAR",
    searchable_by=["Unown VSTAR", "VSTAR", "UnownVSTAR"],
    subtypes=["VSTAR"],
    collector_number=66,
    set_code="SWSH12",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    family_id=201,
    abilities=[
        Attack(
            title="Tri Power",
            game_text="Flip 3 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Star Cipher",
            game_text="Until this Pok\u00e9mon leaves play, it gains an Ability that has the effect \"The Weakness of each of your opponent's Pok\u00e9mon in play is now Psychic. (The amount of Weakness doesn't change.)\" (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)