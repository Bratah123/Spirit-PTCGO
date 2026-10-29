from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.passives_common import apply_defender_attack_cost_raise, apply_defender_retreat_cost_raise


async def chomp_chomp_hold(ctx):
    """During your opponent's next turn, the Defending Pokemon's attacks
    cost [C] more, and its Retreat Cost is [C] more."""
    await ctx.deal_damage()
    await apply_defender_attack_cost_raise(ctx, 1)
    await apply_defender_retreat_cost_raise(ctx, 1)


card = PokemonCardDef(
    guid="e04a6d25-0e82-578a-a14a-fcf644993d6a",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name",
    display_name="Araquanid",
    searchable_by=["Araquanid", "Stage 1", "Araquanid"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    family_id=751,
    abilities=[
        Attack(
            title="Tangle Drag",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Sticky Web",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=chomp_chomp_hold,
        ),
    ],
)