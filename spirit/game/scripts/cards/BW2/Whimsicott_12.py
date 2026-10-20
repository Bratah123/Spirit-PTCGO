from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


async def encore(ctx):
    """20 damage. Choose 1 attack; defender can only use that attack next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [
        e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
        if isinstance(e, dict) and e.get("abilityType") == "Attack"
        and e.get("abilityID")
    ]
    if not entries:
        return
    index = 0
    if len(entries) > 1:
        index = await ctx.choose(
            "Choose an attack the Defending Pokémon may use",
            [e.get("title", {}).get("id", "Attack") for e in entries],
        )
    chosen_id = entries[index]["abilityID"]
    state = ctx.session.turn_state
    for entry in entries:
        if entry["abilityID"] != chosen_id:
            state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
                state.turn_number + 1


card = PokemonCardDef(
    guid="6b482de6-0d68-5459-9cf5-edeb768cdb0b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Encore",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. During your opponent's next turn, that Pok\u00e9mon can only use that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=encore,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)
