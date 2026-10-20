from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _inferno_fang(ctx):
    """80+; you may discard all Fire Energy attached to this Pokemon for 80 more."""
    fire = [e for e in ctx.attached_energies(ctx.attacker) if _is_fire_energy(e)]
    if fire and await ctx.ask_yes_no("Discard all Fire Energy for 80 more damage?"):
        await ctx.discard_cards(fire)
        await ctx.deal_damage(ctx.ability.damage + 80)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="fa41bbc5-918f-5aec-8563-775d7239a96d",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MHoundoomEX.Name",
    display_name="M Houndoom-EX",
    searchable_by=["M Houndoom-EX", "MEGA", "EX", "MHoundoomEX"],
    subtypes=["MEGA", "EX"],
    collector_number=154,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name",
    family_id=229,
    abilities=[
        Attack(
            title="Inferno Fang",
            game_text="You may discard all Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=80,
            damage_operator="+",
            effect=_inferno_fang,
        ),
    ],
)