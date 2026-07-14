from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def aqua_wash(ctx):
    """120 damage; you may put 2 Energy from the opponent's Active into their hand."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Put 2 Energy attached to your opponent's Active Pokémon into their hand?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, min(2, len(energies)), minimum=1,
        prompt="Choose Energy to put into your opponent's hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="5e510fa4-522a-553f-906f-2eb5ff40ca67",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2", "Samurott"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Swaddling Leaves",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Aqua Wash",
            game_text="You may put 2 Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=aqua_wash,
        ),
    ],
)