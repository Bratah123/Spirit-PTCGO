from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _shadow_stitching(ctx):
    """40; until the end of your opponent's next turn, each of their Pokemon has no Abilities."""
    await ctx.deal_damage()
    opp = ctx.opponent_id
    ctx.add_global_passive(ability_lock_passive(lambda p, carrier: p.owning_player_id == opp),
                           ctx.session.turn_state.turn_number + 1)


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _moonlight_slash(ctx):
    """60+; you may return a Water Energy from this Pokemon to your hand for 20 more."""
    water = [e for e in ctx.attached_energies(ctx.attacker) if _is_water_energy(e)]
    if water and await ctx.ask_yes_no("Return a Water Energy to your hand for 20 more damage?"):
        pick = water if len(water) == 1 else await ctx.choose_cards(water, 1, minimum=1, prompt="Choose a Water Energy")
        if pick:
            await ctx.put_in_hand(pick[:1], reveal=False)
            await ctx.deal_damage(ctx.ability.damage + 20)
            return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="06835cae-fddd-51da-b8b5-68fa60dc121c",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja",
    searchable_by=["Greninja", "Stage 2", "Greninja"],
    subtypes=["Stage 2"],
    collector_number=40,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Shadow Stitching",
            game_text="Until the end of your opponent's next turn, each Pok\u00e9mon your opponent has in play, in his or her hand, and in his or her discard pile has no Abilities. (This includes cards that come into play on that turn.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_shadow_stitching,
        ),
        Attack(
            title="Moonlight Slash",
            game_text="You may return a Water Energy from this Pok\u00e9mon to your hand. If you do, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="+",
            effect=_moonlight_slash,
        ),
    ],
)