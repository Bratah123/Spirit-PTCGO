from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    flip_damage, flip_or_nothing, lock_all_attacks,
)


async def _cant_attack_next_turn(ctx):
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="1254275b-009d-5102-9738-770203909397",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Rush",
            game_text="Flip 5 coins. This attack does 10 damage times the number of heads. Hitmonchan can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=5, per_heads=10, also=_cant_attack_next_turn),
        ),
        Attack(
            title="Smash Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)
