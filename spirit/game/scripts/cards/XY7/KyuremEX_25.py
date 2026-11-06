from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents, lock_defender_attacks


async def _cryofreeze(ctx):
    """Printed damage; discard an Energy from this Pokemon. The Defending
    Pokemon can't attack during your opponent's next turn."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(ctx.attacker, 1, minimum=1)
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="c798f7c2-aef4-50b4-a037-c56093e05fdf",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremEX.Name",
    display_name="Kyurem-EX",
    searchable_by=["Kyurem-EX", "Basic", "EX", "KyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=25,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Glaciate",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(30),
        ),
        Attack(
            title="Icecalibur",
            game_text="Discard an Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_cryofreeze,
        ),
    ],
)