from spirit.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="436e4ef7-954e-5bec-b1ab-763ac896275e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Basic", "Shedinja"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=292,
    unplayable_from_hand=True,
    abilities=[
        Ability(
            title="Shell Survival",
            game_text="Put this Pok\u00e9mon into play only with the effect of Ninjask's Cast-Off Shell Ability. (When you are setting up to play, you cannot put it face down as your Active Pok\u00e9mon or on your Bench.)",
        ),
        Attack(
            title="Life Squeeze",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=life_squeeze,
        ),
    ],
)