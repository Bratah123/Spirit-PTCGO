from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


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
    guid="49a25195-b8ad-5616-bfd5-e5a3d9c6c9a2",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1", "Simisage"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=torment,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)