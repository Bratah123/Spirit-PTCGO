from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


async def _link(ctx):
    """Bonus damage for linked Pokemon on your Bench."""
    bench = ctx.my_bench()
    await ctx.deal_damage(ctx.ability.damage + (30 if any(_named(p, "Solosis") for p in bench) else 0))


card = PokemonCardDef(
    guid="48ca6f92-9e5d-53ac-b45e-ce6ba859c7c4",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    display_name="Solosis",
    searchable_by=["Solosis", "Basic", "Solosis"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=577,
    abilities=[
        Attack(
            title="Mini Link",
            game_text="If Solosis is on your Bench, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=_link,
        ),
    ],
)