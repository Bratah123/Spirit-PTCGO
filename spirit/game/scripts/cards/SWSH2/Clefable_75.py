from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def prankish(ctx):
    opponent_active = ctx.opponent_active()
    if opponent_active is None or ctx.effects_blocked(opponent_active):
        return
    energies = ctx.attached_energies(opponent_active)
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Put an Energy attached to your opponent's Active Pokémon on top of their deck?"
    ):
        return
    energy = energies[0]
    if len(energies) > 1:
        picks = await ctx.choose_cards(
            energies, 1,
            prompt="Choose an Energy to put on top of your opponent's deck.",
        )
        if not picks:
            return
        energy = picks[0]
    await ctx.put_on_top_of_deck(energy)


card = PokemonCardDef(
    guid="b8e5eaa2-4d4a-5d3b-a319-685fe1dc4497",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Prankish",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put an Energy attached to your opponent's Active Pok\u00e9mon on top of their deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=prankish,
        ),
        Attack(
            title="Moon Kick",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)