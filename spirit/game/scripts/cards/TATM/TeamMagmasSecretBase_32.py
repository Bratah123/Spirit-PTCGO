from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_basic_pokemon


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


async def team_magmas_secret_base_watch(ctx):
    """2 damage counters on any non-Team Magma Basic just benched from hand."""
    pokemon = getattr(ctx, "benched_pokemon", None)
    if pokemon is None or not is_basic_pokemon(pokemon) or _team(pokemon, "Magma"):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False, as_counters=True)


card = StadiumCardDef(
    guid="00a64349-e0e4-532e-a4fb-89d300f40dbd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasSecretBase.Name",
    display_name="Team Magma's Secret Base",
    searchable_by=["Team Magma's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=32,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Team Magma's Secret Base",
            game_text="Whenever any player puts a Basic Pok\u00e9mon (except for Team Magma Pok\u00e9mon) from his or her hand onto his or her Bench, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=team_magmas_secret_base_watch,
        ),
    ]
)
