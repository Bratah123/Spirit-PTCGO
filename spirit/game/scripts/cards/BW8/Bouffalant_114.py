from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


async def _gnaw_through(ctx):
    """Discard a Pokemon Tool card attached to the Defending Pokemon."""
    d = ctx.defender
    if d is None or ctx.effects_blocked(d):
        return
    tools = [c for c in d.children
             if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]
    if tools:
        await ctx.discard_cards(tools[:1])


card = PokemonCardDef(
    guid="32ff29b7-66cb-5e81-892d-d6b15cb1d232",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Team Plasma", "Bouffalant"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=114,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Tool Breaker",
            game_text="Discard a Pok\u00e9mon Tool card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gnaw_through,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 4},
            damage=70,
        ),
    ],
)