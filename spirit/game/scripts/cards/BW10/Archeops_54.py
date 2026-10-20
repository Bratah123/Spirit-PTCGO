from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage


async def _swift_dive(ctx):
    """If this Pokemon's remaining HP is 50 or less, base damage is 50."""
    low = ctx.attacker.get_attribute(AttrID.HP, 0) <= 50
    await ctx.deal_damage(50 if low else ctx.ability.damage)


card = PokemonCardDef(
    guid="6628961e-2c2a-5568-ba79-450a4158439c",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 1", "Archeops"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
        Attack(
            title="Swift Dive",
            game_text="If this Pok\u00e9mon's remaining HP is 50 or less, this attack's base damage is 50.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            effect=_swift_dive,
        ),
    ],
)