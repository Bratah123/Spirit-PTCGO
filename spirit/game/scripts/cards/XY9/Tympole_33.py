from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _has_round(p):
    return any(getattr(a, "title", None) == "Round" for a in (getattr(def_for(p.archetype_id), "abilities", None) or []))


async def _round(ctx):
    """10x the number of your Pokemon in play that have the Round attack."""
    await ctx.deal_damage(10 * sum(1 for p in ctx.my_pokemon_in_play() if _has_round(p)))


card = PokemonCardDef(
    guid="9445aa63-cc4a-57cc-b0f9-a2687b43efe6",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic", "Tympole"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=535,
    abilities=[
        Attack(
            title="Get Loud",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Round",
            game_text="This attack does 10 damage times the number of your Pok\u00e9mon in play that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=_round,
        ),
    ],
)