from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_team_plasma_pokemon


async def frozen_city_watch(ctx):
    """Whenever any player attaches an Energy from their hand to a Pokemon
    (excluding Team Plasma Pokemon), put 2 damage counters on that Pokemon.
    Observes manual attaches and effect attaches that count as the turn's
    attachment (the engine's ON_ENERGY_ATTACHED scope)."""
    pokemon = getattr(ctx, "energy_receiver", None)
    if pokemon is None or is_team_plasma_pokemon(pokemon):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False, as_counters=True)


card = StadiumCardDef(
    guid="b676ca51-b6cf-5d9f-8b1e-45a89cb027d4",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FrozenCity.Name",
    display_name="Frozen City",
    searchable_by=["Frozen City", "Stadium", "Team Plasma"],
    subtypes=["Stadium", "Team Plasma"],
    collector_number=100,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Frozen City",
            game_text="Whenever any player attaches an Energy from his or her hand to Pok\u00e9mon (excluding Team Plasma Pok\u00e9mon), put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=frozen_city_watch,
        ),
    ],
)
