from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _gnaw_through(ctx):
    """Discard all Pokemon Tool cards from your opponent's Active Pokemon."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    tools = [t for t, p in ctx.tools_in_play() if p is defender]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="70780b83-d4e1-53d2-a589-659092c8e98d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic", "Carvanha"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=318,
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Discard all Pok\u00e9mon Tool cards from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gnaw_through,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)