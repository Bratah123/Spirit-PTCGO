from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54d210b3-ba37-589b-9110-3682a957fe06",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottVSTAR.Name",
    display_name="Whimsicott VSTAR",
    searchable_by=["Whimsicott VSTAR", "VSTAR", "WhimsicottVSTAR"],
    subtypes=["VSTAR"],
    collector_number=65,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottV.Name",
    family_id=547,
    abilities=[
        Attack(
            title="Trick Wind",
            game_text="During your opponent's next turn, they can't play any Pok\u00e9mon Tool or Special Energy cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Fluffball Star",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon for each Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)