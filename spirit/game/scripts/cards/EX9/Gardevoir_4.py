"""STUB: effect not implemented — do not guess mechanics.
Gardevoir (EX9 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import heal_dance, poke_power_condition


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


card = PokemonCardDef(
    guid="12e02733-16aa-5c5f-9fee-8d08be4740e3",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Heal Dance",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Heal Dance",
            condition=poke_power_condition(),
            game_text="Once during your turn (before your attack), you may remove 2 damage counters from 1 of your Pok\u00e9mon. You can't use more than 1 Heal Dance Pok\u00e9-Power each turn. This power can't be used if Gardevoir is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
                        effect=heal_dance(2),
        ),
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=sonic_boom,
        ),
    ],
)