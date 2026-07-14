from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def assault_gate(ctx):
    """If this Pokemon didn't move Bench->Active this turn, this attack does nothing; damage ignores Weakness."""
    if not ctx.entered_active_this_turn(ctx.attacker):
        return
    await ctx.deal_damage(ignore_weakness=True)

card = PokemonCardDef(
    guid="28c53b5c-0eb1-5a20-8faf-e532e7ef419e",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=720,
    abilities=[
        Attack(
            title="Assault Gate",
            game_text="If this Pok\u00e9mon didn't move from the Bench to the Active Spot this turn, this attack does nothing. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=90,
            effect=assault_gate,
        ),
    ],
)