from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="973a434c-a358-53bb-9edb-b6578dc8aeec",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=119,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Strong Breeze",
            game_text="Your opponent shuffles their Active Pok\u00e9mon and all attached cards into their deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Bird",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            effect=unimplemented,
        ),
    ],
)