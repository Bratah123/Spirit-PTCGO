from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def pitch_a_pyukumuku(ctx):
    """From hand: you may reveal this and put it on the bottom of the deck,
    then draw a card."""
    if not await ctx.ask_yes_no("Reveal this Pokémon and put it on the bottom of your deck?"):
        return
    await ctx.reveal_cards([ctx.source])
    if await ctx.put_on_bottom_of_deck(ctx.source):
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="95ee77dc-dd7e-56af-b800-bcd502432ae7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name",
    display_name="Pyukumuku",
    searchable_by=["Pyukumuku", "Basic", "Pyukumuku"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=771,
    abilities=[
        Ability(
            title="Pitch a Pyukumuku",
            game_text="Once during your turn, if this Pok\u00e9mon is in your hand, you may reveal it and put it on the bottom of your deck. If you do, draw a card. You can't use more than 1 Pitch a Pyukumuku Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            shared_once_per_turn="Pitch a Pyukumuku",
            effect=pitch_a_pyukumuku,
        ),
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)