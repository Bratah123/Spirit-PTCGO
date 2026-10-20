from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def acid_spray(ctx):
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Acid Spray"))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard from the Defending Pokémon",
    )


card = PokemonCardDef(
    guid="57dfb61a-a525-52d4-a750-ec5f7cd0079e",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Accelgor"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=acid_spray,
        ),
        Attack(
            title="Slashing Strike",
            game_text="This Pok\u00e9mon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            locks_next_turn=True,
        ),
    ],
)
