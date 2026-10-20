from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import flip_damage


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def _double_scrapper(ctx):
    """Discard up to 2 Pokemon Tool cards attached to the opponent's Pokemon."""
    pool = [t for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
            for t in p.children if _is_tool(t)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose Pokémon Tools to discard")
    if picks:
        await ctx.discard_cards(list(picks))


card = PokemonCardDef(
    guid="ebb8aca8-bdbf-52a7-96df-419be16e0c28",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name",
    display_name="Beedrill-EX",
    searchable_by=["Beedrill-EX", "Basic", "EX", "BeedrillEX"],
    subtypes=["Basic", "EX"],
    collector_number=157,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=15,
    abilities=[
        Attack(
            title="Double Scrapper",
            game_text="Discard up to 2 Pok\u00e9mon Tool cards attached to your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_double_scrapper,
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(4, per_heads=40),
        ),
    ],
)