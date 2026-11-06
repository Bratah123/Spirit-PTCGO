from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _dig_out(ctx):
    """10; discard the top card of your deck. If it is a Fighting Energy,
    attach it to this Pokemon."""
    await ctx.deal_damage()
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value):
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="d4ec40ca-defe-55f1-a28c-549ad23b2288",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    display_name="Rhyhorn",
    searchable_by=["Rhyhorn", "Basic", "Rhyhorn"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=111,
    abilities=[
        Attack(
            title="Dig Out",
            game_text="Discard the top card of your deck. If that card is a Fighting Energy, attach it to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=_dig_out,
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)