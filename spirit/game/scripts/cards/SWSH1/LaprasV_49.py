from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_energy_card


def _is_water_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


async def body_surf(ctx):
    """Attach a Water Energy from hand to this Pokémon; if you do, switch it with a Benched Pokémon."""
    hand_water = [c for c in ctx.hand() if _is_water_energy(c)]
    if not hand_water:
        return
    picks = await ctx.choose_cards(
        hand_water, 1, minimum=0,
        prompt="Attach a Water Energy card from your hand to this Pokémon?",
    )
    if not picks:
        return
    if not await ctx.attach_energy(picks[0], ctx.source, counts_as_attachment=True):
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to switch with this Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def ocean_loop(ctx):
    """210 damage, then put 2 Water Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    attached = [c for c in ctx.attached_energies(ctx.source) if _is_water_energy(c)]
    if not attached:
        return
    picks = await ctx.choose_cards(
        attached, 2, prompt="Choose 2 Water Energy to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="d5306e12-72c2-5791-ae88-201d2806c2b8",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LaprasV.Name",
    display_name="Lapras V",
    searchable_by=["Lapras V", "Basic", "V", "LaprasV"],
    subtypes=["Basic", "V"],
    collector_number=49,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Body Surf",
            game_text="Attach a Water Energy card from your hand to this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=body_surf,
        ),
        Attack(
            title="Ocean Loop",
            game_text="Put 2 Water Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=ocean_loop,
        ),
    ],
)