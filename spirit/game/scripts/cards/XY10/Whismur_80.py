from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _has_round(p):
    return any(getattr(a, "title", None) == "Round" for a in (getattr(def_for(p.archetype_id), "abilities", None) or []))


async def _round(ctx):
    """10x the number of your Pokemon that have the Round attack."""
    await ctx.deal_damage(10 * sum(1 for p in ctx.my_pokemon_in_play() if _has_round(p)))


card = PokemonCardDef(
    guid="5388fd26-c3fd-580b-b3c6-62c25f5903b5",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Round",
            game_text="This attack does 10 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=_round,
        ),
    ],
)