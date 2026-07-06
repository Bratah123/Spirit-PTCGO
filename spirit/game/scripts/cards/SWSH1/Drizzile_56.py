from spirit.game.card_effects.pokemon import shady_dealings
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d71d8e05-ed88-5c51-9d1c-3f4116a93b2c",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    display_name="Drizzile",
    searchable_by=["Drizzile", "Stage 1", "Drizzile"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    family_id=816,
    abilities=[
        Ability(
            title="Shady Dealings",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for a Trainer card, reveal it, and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=shady_dealings(1),
        ),
        Attack(
            title="Water Drip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)