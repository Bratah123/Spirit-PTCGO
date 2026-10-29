from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    power_lariat,
    queens_call,
)

card = PokemonCardDef(
    guid="5f7be99b-82cc-5f97-9aae-598ed16d6830",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=160,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Queen's Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Pok\u00e9mon that isn't a Pok\u00e9mon-GX or Pok\u00e9mon-EX, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=queens_call,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Power Lariat",
            game_text="This attack does 50 more damage for each Evolution Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=power_lariat,
        ),
    ],
)