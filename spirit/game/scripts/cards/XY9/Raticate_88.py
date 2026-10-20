from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, TrainerType
from spirit.game.card_effects.passives_common import condition_immunity_passive


async def _dirty_shock(ctx):
    """Poison the opponent's Active and discard all Pokemon Tool cards attached to it."""
    d = ctx.opponent_active()
    if d is None:
        return
    await ctx.apply_special_condition(d, SpecialConditions.POISONED)
    if ctx.effects_blocked(d):
        return
    tools = [c for c in d.children if c.get_attribute(AttrID.TRAINER_TYPE) in
             (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="6dfffb0c-7772-5349-bc80-548dc0f14fa2",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Ability(
            title="Antibodies",
            game_text="This Pok\u00e9mon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pok\u00e9mon.)",
            passive=condition_immunity_passive(),
        ),
        Attack(
            title="Dirty Shock",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Discard all Pok\u00e9mon Tool cards attached to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_dirty_shock,
        ),
    ],
)