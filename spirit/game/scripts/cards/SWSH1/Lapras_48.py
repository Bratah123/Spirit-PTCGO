from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _aqua_wash(ctx):
    await ctx.deal_damage()
    active = ctx.opponent_active()
    energies = ctx.attached_energies(active) if active is not None else []
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Put 2 Energy attached to your opponent's Active Pokémon into their hand?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 2, prompt="Choose Energy to put into their hand"
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="cba31192-46f4-5951-9a4f-adb183dc5ebd",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Aqua Wash",
            game_text="You may put 2 Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 4},
            damage=70,
            effect=_aqua_wash,
        ),
    ],
)