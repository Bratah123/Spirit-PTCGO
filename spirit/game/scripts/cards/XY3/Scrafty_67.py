from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_damage


async def _confuse_self(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="e4962497-84e0-54b2-baa0-bbe58007d1db",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Machine Gun Headbutt",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(3, per_heads=50, also=_confuse_self),
        ),
    ],
)