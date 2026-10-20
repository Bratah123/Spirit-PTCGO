from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_metal_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


async def _metal_rain(ctx):
    """Discard any Metal Energy; for each, 30 to 1 of your opponent's Pokemon (no W/R)."""
    metal = [e for e in ctx.attached_energies(ctx.attacker) if _is_metal_energy(e)]
    picks = await ctx.choose_cards(metal, len(metal), minimum=0,
                                   prompt="Discard any number of Metal Energy") if metal else []
    n = len(picks or [])
    if not n:
        return
    await ctx.discard_cards(picks)
    for _ in range(n):
        opp = ctx.opponent_pokemon_in_play()
        if not opp:
            break
        target = opp[0] if len(opp) == 1 else await ctx.choose_pokemon(opp, "Do 30 damage to which Pokémon?")
        if target is not None:
            await ctx.deal_damage(30, target=target, ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="f9802e5e-17df-5b87-9a03-1045154fecb3",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BronzongBREAK.Name",
    display_name="Bronzong BREAK",
    searchable_by=["Bronzong BREAK", "BREAK", "BronzongBREAK"],
    subtypes=["BREAK"],
    collector_number=62,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Metal Rain",
            game_text="Discard as many Metal Energy attached to this Pok\u00e9mon as you like. For each Energy card discarded in this way, choose 1 of your opponent's Pok\u00e9mon and do 30 damage to it. Don't apply Weakness and Resistance. (You may choose the same Pok\u00e9mon more than once.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=_metal_rain,
        ),
    ],
)