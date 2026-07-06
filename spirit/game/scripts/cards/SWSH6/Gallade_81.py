from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a88eba63-348e-5a6e-857d-bf7fe0050775",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name",
    display_name="Gallade",
    searchable_by=["Gallade", "Stage 2", "Gallade"],
    subtypes=["Stage 2"],
    collector_number=81,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Feint",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Dynablade",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon V in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)