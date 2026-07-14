from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


card = PokemonCardDef(
    guid="ce991882-03ac-55cd-a73f-10955608854d",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Single Strike", "Electrode"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=88,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Sonic Boom",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=sonic_boom,
        ),
        Attack(
            title="Explosion",
            game_text="This Pok\u00e9mon also does 90 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(90),
        ),
    ],
)