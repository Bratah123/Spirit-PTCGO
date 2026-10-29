from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import weed_out, weed_out_condition

async def radiating_heat(ctx):
    """20 damage. You may discard an Energy from this Pokémon; if you do,
    discard an Energy from the opponent's Active Pokémon."""
    await ctx.deal_damage()
    if not ctx.attached_energies(ctx.attacker):
        return
    if not await ctx.ask_yes_no("Discard an Energy from this Pokémon?"):
        return
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.defender
    if defender is not None and ctx.attached_energies(defender) \
            and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="0ce390b2-5ae0-531d-9a13-d927e11a289c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Weed Out",
            game_text="Once during your turn (before your attack), you may choose 3 of your Benched Pok\u00e9mon. Then, discard your other Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=weed_out,
            activation=Activations.ONCE_PER_TURN,
            condition=weed_out_condition,
        ),
        Attack(
            title="Dark Destruction",
            game_text="You may discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=radiating_heat,
        ),
    ],
)