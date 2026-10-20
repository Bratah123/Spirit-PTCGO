from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack


def _tools_on(pokemon):
    return [c for c in pokemon.children
            if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]


async def _misinformation(ctx):
    """Discard all Pokemon Tool cards attached to each of your opponent's Pokemon."""
    tools = [t for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
             for t in _tools_on(p)]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="89af03ee-1374-5f3d-9f1a-fb147a7bea92",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Team Plasma", "Chatot"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=77,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=441,
    abilities=[
        Attack(
            title="Misinformation",
            game_text="Discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_misinformation,
        ),
        Attack(
            title="Tone-Deaf",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)