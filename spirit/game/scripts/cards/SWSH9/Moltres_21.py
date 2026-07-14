from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def inferno_wings(ctx):
    """20, +70 more if this Pokemon has any damage counters on it; not
    affected by Weakness."""
    has_damage = ctx.source.get_attribute(AttrID.HP, 0) < ctx.max_hp(ctx.source)
    amount = 20 + (70 if has_damage else 0)
    await ctx.deal_damage(amount, ignore_weakness=True)

card = PokemonCardDef(
    guid="8942b99f-e2bb-5195-bc27-5e5569161b58",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Attack(
            title="Inferno Wings",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=inferno_wings,
        ),
    ],
)