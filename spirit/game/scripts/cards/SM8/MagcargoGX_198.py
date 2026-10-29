from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    burning_magma_gx,
    crushing_charge,
    crushing_charge_condition,
    lava_flow,
)

card = PokemonCardDef(
    guid="c25dcbf3-8404-59a2-9299-edafc5909f6f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagcargoGX.Name",
    display_name="Magcargo-GX",
    searchable_by=["Magcargo-GX", "Stage 1", "GX", "MagcargoGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=198,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Crushing Charge",
            game_text="Once during your turn (before your attack), you may discard the top card of your deck. If it's a basic Energy card, attach it to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=crushing_charge,
            activation=Activations.ONCE_PER_TURN,
            condition=crushing_charge_condition,
        ),
        Attack(
            title="Lava Flow",
            game_text="Discard any amount of basic Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=lava_flow
        ),
        Attack(
            title="Burning Magma-GX",
            game_text="Discard the top 5 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=burning_magma_gx
        ),
    ],
)