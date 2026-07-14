from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def eruption_shot(ctx):
    top = ctx.deck_top(1)
    card = top[0] if top else None
    if card is not None and is_energy_card(card):
        await ctx.attach_energy(card, ctx.attacker)
        await ctx.deal_damage(130)
        return
    if card is not None:
        await ctx.discard_cards([card])
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="d2de967b-8d0f-5712-974c-36c138194fb2",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalVMAX.Name",
    display_name="Coalossal VMAX",
    searchable_by=["Coalossal VMAX", "VMAX", "CoalossalVMAX"],
    subtypes=["VMAX"],
    collector_number=189,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalV.Name",
    family_id=839,
    abilities=[
        Attack(
            title="Eruption Shot",
            game_text="Discard the top card of your deck. If that card is an Energy card, this attack does 90 more damage, and attach that card to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="+",
            effect=eruption_shot,
        ),
        Attack(
            title="G-Max Boulder",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)