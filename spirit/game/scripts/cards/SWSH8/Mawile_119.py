from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import (
    apply_defender_attack_cost_raise, apply_defender_retreat_cost_raise,
)


async def chomp_chomp_hold(ctx):
    """During your opponent's next turn, the Defending Pokemon's attacks
    cost [C] more, and its Retreat Cost is [C] more."""
    await ctx.deal_damage()
    await apply_defender_attack_cost_raise(ctx, 1)
    await apply_defender_retreat_cost_raise(ctx, 1)


card = PokemonCardDef(
    guid="6f0fcd6d-eaa7-5e8f-8de2-4eb7e8d4c5cd",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Chomp Chomp Hold",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=chomp_chomp_hold,
        ),
    ],
)