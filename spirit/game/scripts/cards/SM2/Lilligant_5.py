from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.attacks_common import flip_damage


from spirit.game.attributes import SpecialConditions


async def _confuse_self(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="429b93bc-63ea-5d83-9140-1fb891c23b82",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Petal Blizzard",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 40 damage for each heads. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(3, per_heads=40, also=_confuse_self),
        ),
    ],
)