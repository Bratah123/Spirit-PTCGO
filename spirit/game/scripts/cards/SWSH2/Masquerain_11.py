from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def threatening_pattern(ctx):
    await ctx.deal_damage()
    if not ctx.effects_blocked(ctx.defender):
        ctx.restrict_attachments(ctx.defender)


card = PokemonCardDef(
    guid="4426d1d4-82e3-532c-8651-80381702db30",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Threatening Pattern",
            game_text="During your opponent's next turn, Energy can't be attached from your opponent's hand to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=threatening_pattern,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)