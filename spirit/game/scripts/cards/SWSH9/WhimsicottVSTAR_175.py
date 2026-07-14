from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.session.effects import is_special_energy


def _tool_or_special_energy(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value
    ) or is_special_energy(card)


async def trick_wind(ctx):
    """160. During your opponent's next turn, they can't play any Pokémon Tool or Special Energy cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _tool_or_special_energy)


async def fluffball_star(ctx):
    """VSTAR Power: 60 damage to 1 of your opponent's Pokémon for each Energy attached to this Pokémon. No W/R on Benched targets."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    amount = 60 * count_energy("self")(ctx)
    if amount <= 0:
        return
    await ctx.deal_damage(
        amount, target=target, apply_modifiers=(target is ctx.opponent_active())
    )

card = PokemonCardDef(
    guid="914cb40a-e940-5fda-b442-321cee34bdb3",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottVSTAR.Name",
    display_name="Whimsicott VSTAR",
    searchable_by=["Whimsicott VSTAR", "VSTAR", "WhimsicottVSTAR"],
    subtypes=["VSTAR"],
    collector_number=175,
    set_code="SWSH9",
    rarity=Rarities.RareRainbow,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottV.Name",
    family_id=547,
    abilities=[
        Attack(
            title="Trick Wind",
            game_text="During your opponent's next turn, they can't play any Pok\u00e9mon Tool or Special Energy cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=trick_wind,
        ),
        Attack(
            title="Fluffball Star",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon for each Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fluffball_star,
            vstar=True,
        ),
    ],
)