from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def jungle_rising(ctx):
    """100. You may attach up to 2 basic Energy cards from your hand to your
    Benched Pokémon in any way you like. If you attached Energy to a Pokémon
    this way, heal all damage from that Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no(
        "Attach up to 2 basic Energy cards from your hand to your Benched Pokémon?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 basic Energy cards to attach"
    )
    if not picks:
        return
    attached = await distribute_energy(ctx, picks, bench)
    healed = set()
    for _, target in attached:
        if target.entity_id in healed:
            continue
        healed.add(target.entity_id)
        heal_amount = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
        if heal_amount > 0:
            await ctx.heal(heal_amount, target)

card = PokemonCardDef(
    guid="99a969ba-e5ee-5e63-a00e-4335f4d5008b",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZarudeV.Name",
    display_name="Zarude V",
    searchable_by=["Zarude V", "Basic", "V", "ZarudeV"],
    subtypes=["Basic", "V"],
    collector_number=167,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Jungle Rising",
            game_text="You may attach up to 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like. If you attached Energy to a Pok\u00e9mon in this way, heal all damage from that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            effect=jungle_rising,
        ),
    ],
)