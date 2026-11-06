from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


async def _gnaw_through(ctx):
    """Discard a Pokemon Tool card attached to the Defending Pokemon."""
    d = ctx.defender
    if d is None or ctx.effects_blocked(d):
        return
    tools = [c for c in d.children
             if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]
    if tools:
        await ctx.discard_cards(tools[:1])


async def _super_fang(ctx):
    """Put damage counters on the Defending Pokemon until its remaining HP is 10."""
    d = ctx.defender
    if d is None:
        return
    amount = d.get_attribute(AttrID.HP, 0) - 10
    if amount >= 10:
        await ctx.deal_damage(amount - amount % 10, target=d, as_counters=True)


card = PokemonCardDef(
    guid="a592835b-5a78-57bd-b189-872307284e38",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Discard a Pok\u00e9mon Tool card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gnaw_through,
        ),
        Attack(
            title="Super Fang",
            game_text="Put damage counters on the Defending Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_super_fang,
        ),
    ],
)