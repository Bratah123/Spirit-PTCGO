from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_team_plasma_card


async def _giga_drain(ctx):
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)


async def _solar_transporter(ctx):
    """Reveal the top 5 cards of your deck; put all Team Plasma cards there into
    your hand and discard the others."""
    top = ctx.deck_top(5)
    if not top:
        return
    await ctx.reveal_cards(top)
    keep = [c for c in top if is_team_plasma_card(c)]
    rest = [c for c in top if c not in keep]
    if keep:
        await ctx.put_in_hand(keep, reveal=False)
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="d1e23c5e-d043-5eda-9f00-d5e9fb434c7f",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Team Plasma", "Volcarona"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=13,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Solar Transporter",
            game_text="Reveal the top 5 cards of your deck and put all Team Plasma cards you find there into your hand. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_solar_transporter,
        ),
        Attack(
            title="Leech Life",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_giga_drain,
        ),
    ],
)