from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_per, count_energy, lock_defender_attacks,
)


async def iron_breaker(ctx):
    """80. Defending Pokemon can't attack during opponent's next turn."""
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="a689caad-6c2a-581d-bba5-5c54e027176f",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="BW3",
    rarity=Rarities.RareUltra,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title="Energy Press",
            game_text="Does 20 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20, base=20),
        ),
        Attack(
            title="Iron Breaker",
            game_text="The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=iron_breaker,
        ),
    ],
)
