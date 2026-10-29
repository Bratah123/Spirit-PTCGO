from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    charging_up,
    charging_up_condition,
    turning_point,
)

card = PokemonCardDef(
    guid="148e39c9-f29f-5b3c-b763-bac9acafc0bf",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naganadel.Name",
    display_name="Naganadel",
    searchable_by=["Naganadel", "Stage 1", "Ultra Beast", "Naganadel"],
    subtypes=["Stage 1", "Ultra Beast"],
    collector_number=108,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    family_id=803,
    abilities=[
        Ability(
            title="Charging Up",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=charging_up,
            activation=Activations.ONCE_PER_TURN,
            condition=charging_up_condition,
        ),
        Attack(
            title="Turning Point",
            game_text="If you have exactly 3 Prize cards remaining, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=turning_point
        ),
    ],
)