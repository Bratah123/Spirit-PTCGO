from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def torment(ctx):
    """Choose 1 of the Defending Pokémon's attacks; it can't use
    that attack during your opponent's next turn."""
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
            "Choose an attack to lock",
            [e.get("title", {}).get("id", "Attack") for e in entries],
        )
    entry = entries[index]
    state = ctx.session.turn_state
    state.attack_locks[(defender.entity_id, entry["abilityID"])] = \
        state.turn_number + 1


card = PokemonCardDef(
    guid="6b699858-0eee-5a75-a45d-b9319e5bc6c6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=torment,
        ),
        Attack(
            title="Tumbling Tackle",
            game_text="Both this Pok\u00e9mon and the Defending Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP, self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)