from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def shining_arcana(ctx):
    if not await ctx.ask_yes_no("Look at the top 2 cards of your deck?"):
        return
    top = ctx.deck_top(2)
    if not top:
        return
    energies = [c for c in top if is_basic_energy_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        energies, max(len(energies), 1), minimum=0,
        prompt="Choose basic Energy cards to attach to your Pokémon.",
        display_cards=top,
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    remaining = [c for c in top if c not in picks]
    if remaining:
        await ctx.put_in_hand(remaining, reveal=False)


card = PokemonCardDef(
    guid="a40159a4-cfe1-5475-8c4d-ead32f6ed1f0",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Shining Arcana",
            game_text="Once during your turn, you may look at the top 2 cards of your deck and attach any number of basic Energy cards you find there to your Pok\u00e9mon in any way you like. Put the other cards into your hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=shining_arcana,
        ),
        Attack(
            title="Brainwave",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.PSYCHIC), 30, base=60),
        ),
    ],
)