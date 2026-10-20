from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


async def _giga_horn(ctx):
    """Flip 2 coins. If both are tails, this attack does nothing."""
    results = await ctx.flip_coins(2, "Giga Horn")
    if any(results):
        await ctx.deal_damage()


def _is_break(p):
    return "BREAK" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


card = PokemonCardDef(
    guid="272a086a-1307-508c-b232-bb3b52cb7340",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=621,
    abilities=[
        Attack(
            title="Proud Fang",
            game_text="If your opponent has any Pok\u00e9mon BREAK in play, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(_is_break(p) for p in ctx.opponent_pokemon_in_play()), 60),
        ),
        Attack(
            title="Giga Claw",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_giga_horn,
        ),
    ],
)