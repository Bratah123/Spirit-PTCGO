from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def energy_loop(ctx):
    """120. Put an Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.source)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)

card = PokemonCardDef(
    guid="5a5bb12f-0e4f-5738-98f6-8324955741ac",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=140,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Energy Loop",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=energy_loop,
        ),
    ],
)