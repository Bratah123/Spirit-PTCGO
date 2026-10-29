from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import luminous_sign
from spirit.game.data_utils import Triggers


from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.session.passives import effective_max_hp


async def energy_drive(ctx):
    """20 times Energy on both Actives; ignore Weakness and Resistance."""
    n = count_energy()(ctx) + count_energy("defender")(ctx)
    if n > 0:
        await ctx.deal_damage(20 * n, ignore_weakness=True, ignore_resistance=True)


async def tapu_cure_gx(ctx):
    """Heal all damage from 2 of your Benched Pokémon."""
    damaged = [p for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    picks = await ctx.choose_cards(
        damaged, min(2, len(damaged)), minimum=0,
        prompt="Choose Benched Pokémon to heal",
    )
    for pokemon in picks:
        await ctx.heal(ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0), pokemon)


card = PokemonCardDef(
    guid="b95990f8-b700-53f7-9345-d39287089c84",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLeleGX.Name",
    display_name="Tapu Lele-GX",
    searchable_by=["Tapu Lele-GX", "Basic", "GX", "TapuLeleGX"],
    subtypes=["Basic", "GX"],
    collector_number=60,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=786,
    abilities=[
        Ability(
            title="Wonder Tag",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=luminous_sign,
        ),
        Attack(
            title="Energy Drive",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=energy_drive,
        ),
        Attack(
            title="Tapu Cure-GX",
            game_text="Heal all damage from 2 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tapu_cure_gx,
        ),
    ],
)