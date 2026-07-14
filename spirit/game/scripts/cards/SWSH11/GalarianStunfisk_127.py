from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def field_trap(ctx):
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is None or stadium.owning_player_id != ctx.opponent_id:
        return
    discarded = await ctx.discard_stadium()
    if discarded is None:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 2, prompt="Choose 2 Energy to discard from the Defending Pokémon"
    )


card = PokemonCardDef(
    guid="bafdf6dd-960c-5255-b2a8-8fdf3249a08a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfisk.Name",
    display_name="Galarian Stunfisk",
    searchable_by=["Galarian Stunfisk", "Basic", "GalarianStunfisk"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Attack(
            title="Field Trap",
            game_text="If your opponent has a Stadium in play, discard it. If you discarded a Stadium in this way, discard 2 Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=field_trap,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)