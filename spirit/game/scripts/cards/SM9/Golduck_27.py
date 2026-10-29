from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for

from spirit.game.card_effects.sm9 import (
    swim,
)

async def amnesia(ctx):
    """20 damage; lock 1 of the Defending Pokémon's attacks next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", []) or []
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to lock")
    if picked is None:
        return
    _, chosen = picked
    ctx.session.turn_state.lock_attack(defender.entity_id, chosen.ability_id)

card = PokemonCardDef(
    guid="51e3e283-ad71-5908-bf1b-c774aad9bd48",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=amnesia,
        ),
        Attack(
            title="Swim",
            game_text="If any of your opponent's Pok\u00e9mon have any Water Energy attached to them, you may do 90 damage to 1 of your opponent's Benched Pok\u00e9mon instead of their Active Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=swim,
        ),
    ],
)