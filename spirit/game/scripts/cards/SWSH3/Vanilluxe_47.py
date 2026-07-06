from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d534da76-204d-52bf-ad38-18ee956ad1bb",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Ability(
            title="Bitter Cold",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)