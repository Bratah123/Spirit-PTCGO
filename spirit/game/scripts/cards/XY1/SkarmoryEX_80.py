from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


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
    guid="70ef0839-fc4e-5798-b068-4f8593cdde94",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkarmoryEX.Name",
    display_name="Skarmory-EX",
    searchable_by=["Skarmory-EX", "Basic", "EX", "SkarmoryEX"],
    subtypes=["Basic", "EX"],
    collector_number=80,
    set_code="XY1",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_obsidian_fang,
        ),
        Attack(
            title="Tailspin Piledriver",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(has_damage('defender'), 40, base=80),
        ),
    ],
)