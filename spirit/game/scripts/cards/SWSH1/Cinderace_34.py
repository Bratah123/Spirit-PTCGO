from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def libero(ctx):
    """Once per turn, on move to Active: you may attach up to 2 Fire Energy from discard."""
    fire_energy = [c for c in ctx.discard_pile() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    if not fire_energy:
        return
    if not await ctx.ask_yes_no("Attach up to 2 Fire Energy cards from your discard pile to Cinderace?"):
        return
    picks = await ctx.choose_cards(
        fire_energy, 2, minimum=1,
        prompt="Choose up to 2 Fire Energy cards to attach.",
    )
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="9a908f80-98fe-5529-aeb7-aa5aaf67fdbe",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Cinderace"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Ability(
            title="Libero",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may attach up to 2 Fire Energy cards from your discard pile to it.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=libero,
        ),
        Attack(
            title="Flare Striker",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)