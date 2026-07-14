from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def bug_transmission(ctx):
    """Whenever you attach an Energy card from your hand to this Pokémon
    during your turn, you may make your opponent's Active Pokémon Confused."""
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Confused?"):
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="6b4fde7b-7d08-5b05-ba8e-8ba7a5b8fd80",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=118,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Bug Transmission",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon during your turn, you may make your opponent's Active Pok\u00e9mon Confused.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=bug_transmission,
        ),
        Attack(
            title="Superbeam",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)