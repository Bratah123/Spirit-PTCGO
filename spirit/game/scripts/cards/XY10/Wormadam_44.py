from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


async def _link(ctx):
    """Bonus damage for linked Pokemon on your Bench."""
    bench = ctx.my_bench()
    await ctx.deal_damage(ctx.ability.damage + (60 if any(_named(p, "Mothim") for p in bench) else 0))


card = PokemonCardDef(
    guid="3205659b-83e7-5705-b1f2-74c4ea2eea27",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name",
    display_name="Wormadam",
    searchable_by=["Wormadam", "Stage 1", "Wormadam"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Twin Bursts",
            game_text="If Mothim is on your Bench, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=_link,
        ),
    ],
)