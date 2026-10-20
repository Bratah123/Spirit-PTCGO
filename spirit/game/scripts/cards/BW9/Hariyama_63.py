from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _PivotThrowPassive(Passive):
    """During your opponent's next turn, damage done to this Pokemon by
    attacks is increased by 20 (after Weakness and Resistance)."""

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.target is carrier_pokemon(carrier) and calc.amount > 0:
            calc.amount += 20


async def _pivot_throw(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _PivotThrowPassive())


card = PokemonCardDef(
    guid="59ac1950-0b4e-56d4-b03a-8ea143b989ed",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Pivot Throw",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is increased by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_pivot_throw,
        ),
    ],
)