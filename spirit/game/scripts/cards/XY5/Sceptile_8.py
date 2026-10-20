from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _nurture_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_grass_energy(c) for c in hand.children)


async def _nurture_and_heal(ctx):
    """Attach a Grass Energy card from your hand to 1 of your Pokemon; heal 30 from it."""
    cards = [c for c in ctx.hand() if _is_grass_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Grass Energy card")
    if not picks:
        return
    mine = ctx.my_pokemon_in_play()
    target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach it to which Pokémon?")
    target = target or mine[0]
    await ctx.attach_energy(picks[0], target)
    await ctx.heal(30, target)


card = PokemonCardDef(
    guid="3d09f31d-0f9a-5144-874a-da8f24b55ef3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Nurture and Heal",
            game_text="Once during your turn (before your attack), you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you do, heal 30 damage from that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_nurture_condition,
            effect=_nurture_and_heal,
        ),
        Attack(
            title="Jungle Edge",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)