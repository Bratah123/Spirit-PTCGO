from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


async def _play_ball(ctx):
    """When played from hand onto the Bench: you may put 3 Poke Ball cards from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if getattr(def_for(c.archetype_id), "display_name", "") == "Pok\u00e9 Ball"]
    if not pool:
        return
    picked = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Choose Poké Ball cards to put into your hand")
    if picked:
        await ctx.put_in_hand(picked)


card = PokemonCardDef(
    guid="3a672028-3296-59f0-a6bd-f08ded551f84",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic", "Foongus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=590,
    abilities=[
        Ability(
            title="Play Ball",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may put 3 Pok\u00e9 Ball cards from your discard pile into your hand.",
            trigger=Triggers.ON_PLAY,
            effect=_play_ball,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)