from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def live_painting(ctx):
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Reveal any number of basic Energy cards from your hand",
    )
    if not picks:
        return
    await ctx.reveal_cards(picks)
    types = set()
    for card in picks:
        types.update(card.get_attribute(AttrID.POKEMON_TYPES) or [])
    amount = 30 * len(types)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="229b1c9e-672b-545d-ae92-3c46649b9aec",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Live Painting",
            game_text="Reveal any number of basic Energy cards from your hand. This attack does 30 more damage for each type of basic Energy you revealed in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=live_painting,
        ),
    ],
)