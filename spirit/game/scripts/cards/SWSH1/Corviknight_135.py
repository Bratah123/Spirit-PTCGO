from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_protection


async def iron_wings(ctx):
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if len(energies) >= 2 and await ctx.ask_yes_no(
        "Discard 2 Energy from this Pokémon?"
    ):
        picks = await ctx.discard_energy_from(ctx.attacker, 2)
        if picks:
            await apply_protection(ctx, reduce=100)


card = PokemonCardDef(
    guid="b5520748-df6e-54f8-a8c2-37f749adb4db",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name",
    display_name="Corviknight",
    searchable_by=["Corviknight", "Stage 2", "Corviknight"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Iron Wings",
            game_text="You may discard 2 Energy from this Pok\u00e9mon. If you do, during your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=iron_wings,
        ),
    ],
)