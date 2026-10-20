from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import has_tool
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _tools(p):
    return [c for c in p.children if c.get_attribute(AttrID.TRAINER_TYPE) in
            (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)]


def _drive_condition(board, player_id, pokemon=None):
    return pokemon is not None and has_tool(pokemon)


async def _drive_change(ctx):
    """Put a Pokemon Tool card attached to this Pokemon into your hand."""
    tools = _tools(ctx.source)
    if tools:
        pick = tools if len(tools) == 1 else await ctx.choose_cards(tools, 1, minimum=1, prompt="Choose a Tool")
        if pick:
            await ctx.put_in_hand(pick[:1], reveal=False)


def _is_metal_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


async def _rapid_blaster(ctx):
    """100+; discard any number of Metal Energy from this Pokemon; 20 more each."""
    metal = [e for e in ctx.attached_energies(ctx.attacker) if _is_metal_energy(e)]
    picks = await ctx.choose_cards(metal, len(metal), minimum=0,
                                   prompt="Discard any number of Metal Energy") if metal else []
    n = len(picks or [])
    if n:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(ctx.ability.damage + 20 * n)


card = PokemonCardDef(
    guid="37e4d0b2-4a80-5439-8bf9-59a0a23400da",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "GenesectEX"],
    subtypes=["Basic", "EX"],
    collector_number=120,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Ability(
            title="Drive Change",
            game_text="Once during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to this Pok\u00e9mon into your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_drive_condition,
            effect=_drive_change,
        ),
        Attack(
            title="Rapid Blaster",
            game_text="Discard as many Metal Energy attached to this Pok\u00e9mon as you like. This attack does 20 more damage for each Metal Energy you discarded.",
            cost={PokemonTypes.METAL: 3},
            damage=100,
            damage_operator="+",
            effect=_rapid_blaster,
        ),
    ],
)