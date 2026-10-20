from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def _wings_of_disaster(ctx):
    """20 to each opposing Pokemon (no W/R); discard all Tools on them."""
    for p in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(20, target=p, ignore_weakness=True, ignore_resistance=True)
    tools = [t for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
             for t in p.children if _is_tool(t)]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="c99e8ffc-d3dd-515a-93ed-c1bdfd353634",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MandibuzzBREAK.Name",
    display_name="Mandibuzz BREAK",
    searchable_by=["Mandibuzz BREAK", "BREAK", "MandibuzzBREAK"],
    subtypes=["BREAK"],
    collector_number=182,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    family_id=630,
    abilities=[
        Attack(
            title="Wings of Disaster",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_wings_of_disaster,
        ),
    ],
)