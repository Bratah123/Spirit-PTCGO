from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_defender_debuff


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _parting_shot(ctx):
    """10; switch this Pokemon with 1 of your Benched; the Defending Pokemon's attacks do 60 less next turn."""
    await ctx.deal_damage()
    await apply_defender_debuff(ctx, 60)
    bench = ctx.my_bench()
    if bench and ctx.attacker is ctx.my_active():
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="f09ad9a7-6c9b-5925-8384-eb4849eb5558",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1", "Pangoro"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=674,
    abilities=[
        Attack(
            title="Parting Shot",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 60 (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=_parting_shot,
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=90,
            effect=feint,
        ),
    ],
)