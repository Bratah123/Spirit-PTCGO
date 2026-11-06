from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import AttrID, PokemonTypes, Rarities, TrainerType
from spirit.game.session.passives import effective_max_hp


async def violent_rage(ctx):
    """Flip coins equal to damage counters on self; 10 damage times heads."""
    me = ctx.source
    hp = me.get_attribute(AttrID.HP, 0)
    max_hp = effective_max_hp(ctx.board, me)
    counters = max(0, (max_hp - hp) // 10)
    if counters <= 0:
        return
    results = await ctx.flip_coins(counters, "Violent Rage")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(amount=10 * heads)

_attack = Attack(
    title="Violent Rage",
    game_text="Flip a number of coins equal to the number of damage counters on this Pokémon. This attack does 10 damage times the number of heads.",
    cost={PokemonTypes.FIGHTING: 1},
    damage=0,
    effect=violent_rage,
    )

card = TrainerCardDef(
    guid="8f288a6d-2d07-553c-9a8c-63c0cfabd9a4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingCube01.Name",
    display_name="Fighting Cube 01",
    searchable_by=["Fighting Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=121,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.FIGHTING: pokemon_has_type(p, _t)
