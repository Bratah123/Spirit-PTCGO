from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


async def _obsidian_fang(ctx):
    """Before doing damage, discard all Pokemon Tool cards attached to the
    Defending Pokemon."""
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        tools = [c for c in d.children
                 if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="93b354df-4191-559e-85ba-10ac9c34d686",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(
            title="Peck Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_obsidian_fang,
        ),
    ],
)