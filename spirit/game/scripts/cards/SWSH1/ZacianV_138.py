from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_metal_energy_card


async def intrepid_sword(ctx):
    """Once per turn: look at the top 3, attach any Metal Energy found there
    to this Pokémon, the rest to hand. Ends your turn."""
    top = ctx.deck_top(3)
    if not top:
        return
    metal = [c for c in top if is_metal_energy_card(c)]
    picks = []
    if metal:
        picks = await ctx.choose_cards(
            metal, len(metal), minimum=0,
            prompt="Attach any number of Metal Energy cards to this Pokémon.",
            display_cards=top,
        )
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.put_in_hand(rest, reveal=False)


card = PokemonCardDef(
    guid="b370c27e-c08b-5d0f-ab21-42fafe1a3e32",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=138,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Ability(
            title="Intrepid Sword",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Metal Energy cards you find there to this Pok\u00e9mon. Put the other cards into your hand. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=intrepid_sword,
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 3},
            damage=230,
            locks_next_turn=True,
        ),
    ],
)