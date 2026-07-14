from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def malevolent_charge(ctx):
    def is_darkness_energy(c):
        return is_energy_card(c) and energy_provides_type(c, PokemonTypes.DARKNESS.value)
    matches = [c for c in ctx.hand() if is_darkness_energy(c)]
    if not matches:
        return
    if not await ctx.ask_yes_no(
            "Attach up to 2 Darkness Energy cards from your hand to this Pokémon?"):
        return
    picks = await ctx.choose_cards(
        matches, 2, minimum=0,
        prompt="Choose up to 2 Darkness Energy cards to attach",
    )
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="55dce45d-bc5d-5ae3-993d-143d6bb8a1c0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMoltres.Name",
    display_name="Galarian Moltres",
    searchable_by=["Galarian Moltres", "Basic", "GalarianMoltres"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=146,
    abilities=[
        Ability(
            title="Malevolent Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Darkness Energy cards from your hand to this Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=malevolent_charge,
        ),
        Attack(
            title="Fiery Wrath",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 50, base=20),
        ),
    ],
)