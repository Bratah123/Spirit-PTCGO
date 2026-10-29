from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.sm7 import (
    feint_attack,
)


async def poison_point(ctx):
    """Active Spot only: if damaged by an opponent's attack (even if
    Knocked Out), the Attacking Pokemon is now Poisoned."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="e5c0c36a-8718-5e11-ab06-08c7c031e009",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Poison Payback",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=poison_point,
        ),
        Attack(
            title="Feint Attack",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=feint_attack,
        ),
    ],
)