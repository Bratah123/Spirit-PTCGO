from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def mirror_pain(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    count = damage_counters_on(lambda c: target)(ctx)
    if count > 0 and ctx.defender is not None:
        await ctx.deal_damage(count * 10, target=ctx.defender, as_counters=True)


card = PokemonCardDef(
    guid="aaa3375b-63e4-5044-ac23-7a3a29b128fe",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Single Strike", "Wobbuffet"],
    subtypes=["Basic", "Single Strike"],
    collector_number=66,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=202,
    abilities=[
        Attack(
            title="Mirror Pain",
            game_text="Put damage counters on your opponent's Active Pok\u00e9mon equal to the number of damage counters on 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mirror_pain,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)