from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.pokemon import energy_provides_type


async def g_max_centiferno(ctx):
    """40 more damage for each Fire Energy attached to this Pokémon. If you did any damage, you may attach a Fire Energy card from your discard pile to this Pokémon."""
    amount = 40 * count_energy("self", energy_type=PokemonTypes.FIRE)(ctx)
    dealt = await ctx.deal_damage(amount) if amount > 0 else 0
    if dealt <= 0:
        return
    if not await ctx.ask_yes_no("Attach a Fire Energy card from your discard pile to this Pokémon?"):
        return
    energies = [c for c in ctx.discard_pile() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Fire Energy card to attach to this Pokémon.")
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="06fa105d-71b2-594c-a3b3-6406411a3320",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchVMAX.Name",
    display_name="Centiskorch VMAX",
    searchable_by=["Centiskorch VMAX", "VMAX", "CentiskorchVMAX"],
    subtypes=["VMAX"],
    collector_number=34,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    family_id=851,
    abilities=[
        Attack(
            title="G-Max Centiferno",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pok\u00e9mon. If you did any damage with this attack, you may attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=g_max_centiferno,
        ),
    ],
)