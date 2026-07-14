from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def spit_shot(ctx):
    """Discard all Energy from this Pokémon. 160 damage to 1 of your
    opponent's Pokémon (no W/R on a Benched target)."""
    await ctx.discard_energy_from(ctx.source, 99)
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(160, target=target)


card = PokemonCardDef(
    guid="ed9b3c3f-481f-58a4-820d-a5bb1b71d843",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CramorantV.Name",
    display_name="Cramorant V",
    searchable_by=["Cramorant V", "Basic", "V", "CramorantV"],
    subtypes=["Basic", "V"],
    collector_number=198,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Beak Catch",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(count=2, reveal=False, prompt="Choose up to 2 cards."),
        ),
        Attack(
            title="Spit Shot",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 160 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=spit_shot,
        ),
    ],
)