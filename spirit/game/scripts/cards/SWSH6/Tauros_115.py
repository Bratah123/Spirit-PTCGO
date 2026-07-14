from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    damage_per, damage_counters_on, recoil_attack,
)


async def _raging_bull_confuse(ctx):
    """After the hit: this Pokémon becomes Confused."""
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="11ab1ba9-c5f4-5876-86fa-18e0d14fd0d7",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Single Strike", "Tauros"],
    subtypes=["Basic", "Single Strike"],
    collector_number=115,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Bull",
            game_text="This attack does 20 more damage for each damage counter on this Pok\u00e9mon. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 20, base=20,
                              also=_raging_bull_confuse),
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=recoil_attack(30),
        ),
    ],
)