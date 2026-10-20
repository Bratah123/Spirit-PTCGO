from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _serene_grace(ctx):
    """On evolve: you may look at the top 8 cards of your deck and attach any
    basic Energy there to your Pokemon in any way; shuffle the rest back."""
    top = ctx.deck_top(8)
    if not top or not await ctx.ask_yes_no("Use Serene Grace?"):
        return
    pool = [c for c in top if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0, display_cards=top,
                                   prompt="Choose basic Energy to attach") if pool else []
    for energy in picks or []:
        mine = ctx.my_pokemon_in_play()
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach the Energy to which Pokémon?")
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d3c91cd1-3b7f-5f4f-a6d6-41009bd3043f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Serene Grace",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may look at the top 8 cards of your deck. Choose any basic Energy cards you find there and attach them to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=_serene_grace,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)