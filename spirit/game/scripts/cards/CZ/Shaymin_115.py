from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_energy_card

card = PokemonCardDef(
    guid="39282b0d-10bb-5d36-82e9-e1cf9b108c56",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=492,
    abilities=[
        Attack(
            title="Gather Flowers",
            game_text="Shuffle up to 2 Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                predicate=is_energy_card, count=2, to="deck_shuffle",
                prompt="Choose up to 2 Energy cards to shuffle into your deck.",
            ),
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)