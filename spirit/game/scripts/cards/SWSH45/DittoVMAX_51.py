from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def max_transform(ctx):
    """Choose 1 of your opponent's Active Pokemon's attacks and use it as this attack."""
    active = ctx.opponent_active()
    if active is None:
        return
    definition = def_for(active.archetype_id)
    candidates = [
        (active, ability) for ability in getattr(definition, "abilities", [])
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, entry["abilityID"])


card = PokemonCardDef(
    guid="d5487ebb-78fd-5d16-b182-706c8afd77da",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoVMAX.Name",
    display_name="Ditto VMAX",
    searchable_by=["Ditto VMAX", "VMAX", "DittoVMAX"],
    subtypes=["VMAX"],
    collector_number=51,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    family_id=132,
    abilities=[
        Attack(
            title="Max Transform",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=max_transform,
        ),
    ],
)