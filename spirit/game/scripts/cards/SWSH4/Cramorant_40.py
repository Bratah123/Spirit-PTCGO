from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import full_stack


async def continuous_gulp_missile(ctx):
    """Discard any number of Benched Arrokuda; 60 damage for each discarded."""
    arrokuda = [p for p in ctx.my_bench()
                if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Arrokuda"]
    picks = []
    if arrokuda:
        picks = await ctx.choose_cards(
            arrokuda, len(arrokuda), minimum=0,
            prompt="Choose Arrokuda to discard from your Bench",
        )
    for pokemon in picks:
        await ctx.discard_cards(full_stack(pokemon))
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="7752b7b3-69e9-52ab-932f-c48d09aedd76",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cramorant.Name",
    display_name="Cramorant",
    searchable_by=["Cramorant", "Basic", "Cramorant"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Continuous Gulp Missile",
            game_text="Discard any number of Arrokuda from your Bench. This attack does 60 damage for each Arrokuda you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=continuous_gulp_missile,
        ),
    ],
)
