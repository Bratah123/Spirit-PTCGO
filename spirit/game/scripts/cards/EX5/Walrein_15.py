"""STUB: effect not implemented — do not guess mechanics.
Walrein (EX5 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import crush_draw, poke_power_condition, sheer_cold

card = PokemonCardDef(
    guid="f8983f0b-8cb7-531a-87ed-267396e6ae93",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Ability(
            title="Crush Draw",
            game_text="Once during your turn (before your attack), you may reveal the top card of your deck. If that card is a basic Energy card, attach it to 1 of your Pok\u00e9mon. If not, put the card back on your deck. This power can't be used if Walrein is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=crush_draw(),
        ),
        Attack(
            title="Sheer Cold",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=sheer_cold(),
        ),
    ],
)