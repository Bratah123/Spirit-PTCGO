from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def life_squeeze(ctx):
    """Put damage counters on the opponent's Active until its remaining HP is 10."""
    target = ctx.defender
    if target is None:
        return
    current = target.get_attribute(AttrID.HP, 0)
    amount = current - 10
    if amount > 0:
        await ctx.deal_damage(amount, target=target, as_counters=True)


card = PokemonCardDef(
    guid="726d597a-c9ee-5041-8292-3e87e13483ea",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaticateBREAK.Name",
    display_name="Raticate BREAK",
    searchable_by=["Raticate BREAK", "BREAK", "RaticateBREAK"],
    subtypes=["BREAK"],
    collector_number=89,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Super Fang",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=life_squeeze,
        ),
    ],
)