from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb0a1c6d-4123-5c55-be80-e9291bcb78cc",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=197,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Slimy Room",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent tries to attach an Energy card from their hand to a Pok\u00e9mon, they must flip a coin. If tails, your opponent discards that Energy card instead of attaching it, and this doesn't use up their Energy attachment for the turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Buster Tail",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=120,
        ),
    ],
)