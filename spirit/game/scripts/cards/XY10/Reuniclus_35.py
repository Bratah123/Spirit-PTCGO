from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


async def _link(ctx):
    """Bonus damage for linked Pokemon on your Bench."""
    bench = ctx.my_bench()
    await ctx.deal_damage(ctx.ability.damage + (30 if any(_named(p, "Solosis") for p in bench) else 0) + (60 if any(_named(p, "Duosion") for p in bench) else 0) + (90 if any(_named(p, "Reuniclus") for p in bench) else 0))


card = PokemonCardDef(
    guid="db9227b1-5789-5046-8ab9-51df0ef597a7",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Link Fusion",
            game_text="If Solosis is on your Bench, this attack does 30 more damage. If Duosion is on your Bench, this attack does 60 more damage. If Reuniclus is on your Bench, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=_link,
        ),
    ],
)