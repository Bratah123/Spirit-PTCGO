from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import is_energy_card


async def _diamond_gift(ctx):
    """20; attach 2 Energy cards from your discard pile to 1 of your Fighting Pokemon."""
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play()
               if PokemonTypes.FIGHTING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    if not pool or not targets:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(targets, "Attach to which Fighting Pokémon?")
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy cards")
    for e in picks or []:
        await ctx.attach_energy(e, target or targets[0])


card = PokemonCardDef(
    guid="3e8b309d-5687-553e-bb7b-d1f7d55149fa",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CarbinkBREAK.Name",
    display_name="Carbink BREAK",
    searchable_by=["Carbink BREAK", "BREAK", "CarbinkBREAK"],
    subtypes=["BREAK"],
    collector_number=51,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    family_id=703,
    abilities=[
        Attack(
            title="Diamond Gift",
            game_text="Attach 2 Energy cards from your discard pile to 1 of your Fighting Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=_diamond_gift,
        ),
    ],
)