from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.card_effects.support_common import recover_from_discard

card = PokemonCardDef(
    guid="d5dd9abe-8828-52ef-b7bc-23880731b7c8",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=81,
    abilities=[
        Attack(
            title="Magnetic Catch",
            game_text="Shuffle up to 3 Metal Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                predicate=is_metal_energy_card, count=3, to="deck_shuffle",
                prompt="Choose up to 3 Metal Energy to shuffle into your deck.",
            ),
        ),
        Attack(
            title="Rolling Attack",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)