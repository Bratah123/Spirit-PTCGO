from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.session.effects import is_pokemon_card, is_supporter_card

_is_pokemon_or_supporter = lambda c: is_pokemon_card(c) or is_supporter_card(c)

card = PokemonCardDef(
    guid="076f5f84-1c8e-59e3-a57b-f3856fbdd408",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Attack(
            title="Dive and Rescue",
            game_text="Put up to 3 in any combination of Pok\u00e9mon and Supporter cards from your discard pile into your hand.",
            cost={PokemonTypes.WATER: 1},
            condition=requires_discard(_is_pokemon_or_supporter),
            effect=recover_from_discard(
                _is_pokemon_or_supporter, count=3,
                prompt="Choose up to 3 Pok\u00e9mon/Supporter cards from your discard pile.",
            ),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)