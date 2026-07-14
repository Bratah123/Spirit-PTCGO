from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card


async def azure_pulse(ctx):
    """Once per turn: you may discard your hand and draw 3 cards."""
    if not await ctx.ask_yes_no("Discard your hand and draw 3 cards?"):
        return
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(3)


def _is_basic_type(card, type_value):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and type_value in types


async def max_burst(ctx):
    """You may discard any amount of basic Fire or Lightning Energy from
    this Pokemon; +80 damage for each card discarded this way."""
    attached = [
        e for e in ctx.attached_energies(ctx.attacker)
        if _is_basic_type(e, PokemonTypes.FIRE.value)
        or _is_basic_type(e, PokemonTypes.LIGHTNING.value)
    ]
    picks = []
    if attached:
        picks = await ctx.choose_cards(
            attached, len(attached), minimum=0,
            prompt="Discard any amount of basic Fire or Lightning Energy from this Pokémon.",
        )
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(20 + 80 * len(picks))


card = PokemonCardDef(
    guid="9f19a7bc-b348-5b1d-8a80-731200fb445c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaVMAX.Name",
    display_name="Rayquaza VMAX",
    searchable_by=["Rayquaza VMAX", "VMAX", "Rapid Strike", "RayquazaVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=217,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    family_id=384,
    abilities=[
        Ability(
            title="Azure Pulse",
            game_text="Once during your turn, you may discard your hand and draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=azure_pulse,
        ),
        Attack(
            title="Max Burst",
            game_text="You may discard any amount of basic Fire Energy or any amount of basic Lightning Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=max_burst,
        ),
    ],
)