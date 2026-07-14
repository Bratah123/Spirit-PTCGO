from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.attacks_common import count_energy, damage_per


async def jamming_attachment(ctx):
    discard = [c for c in ctx.discard_pile(ctx.opponent_id) if is_energy_card(c)]
    if not discard:
        return
    if not await ctx.ask_yes_no(
        "Attach up to 3 Energy cards from your opponent's discard pile to "
        "your opponent's Pokémon in any way you like?"
    ):
        return
    picks = await ctx.choose_cards(
        discard, 3, minimum=0,
        prompt="Choose up to 3 Energy cards to attach.",
    )
    candidates = ctx.opponent_pokemon_in_play()
    if not picks or not candidates:
        return
    await distribute_energy(ctx, picks, candidates)


card = PokemonCardDef(
    guid="a1069e17-851c-5fd0-a33f-c5248c8df9f1",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Jamming Attachment",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach up to 3 Energy cards from your opponent's discard pile to your opponent's Pok\u00e9mon in any way you like.",
            trigger=Triggers.ON_EVOLVE,
            effect=jamming_attachment,
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=30),
        ),
    ],
)