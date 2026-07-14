from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, lock_all_attacks
from spirit.game.session.legal_actions import energy_provided_count


def _both_actives_energy(ctx):
    total = 0
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        for energy in ctx.attached_energies(pokemon):
            total += energy_provided_count(energy)
    return total


async def _deep_crush(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="2b73e21f-77dd-5462-8012-bea5eb1a13f1",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Aero Ball",
            game_text="This attack does 20 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(_both_actives_energy, 20),
        ),
        Attack(
            title="Deep Crush",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=_deep_crush,
        ),
    ],
)