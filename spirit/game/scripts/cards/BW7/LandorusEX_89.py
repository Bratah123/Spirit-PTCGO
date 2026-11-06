from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _lands_judgment(ctx):
    """You may discard all Fighting Energy attached to this Pokemon; if you do, +70."""
    fighting = [e for e in ctx.attached_energies(ctx.attacker) if _is_fighting_energy(e)]
    bonus = 0
    if fighting and await ctx.ask_yes_no("Discard all Fighting Energy for 70 more damage?"):
        await ctx.discard_cards(fighting)
        bonus = 70
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="2e5d208b-d544-51df-9508-5c784a705da5",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LandorusEX.Name",
    display_name="Landorus-EX",
    searchable_by=["Landorus-EX", "Basic", "EX", "LandorusEX"],
    subtypes=["Basic", "EX"],
    collector_number=89,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=645,
    abilities=[
        Attack(
            title="Hammerhead",
            game_text="Does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=snipe_attack(30, pool='bench', count=1, also_base=True),
        ),
        Attack(
            title="Land's Judgment",
            game_text="You may discard all Fighting Energy attached to this Pok\u00e9mon. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_lands_judgment,
        ),
    ],
)