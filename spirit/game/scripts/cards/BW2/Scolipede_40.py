from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage

card = PokemonCardDef(
    guid="509addc8-8981-5bd6-910d-6235b9062954",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2", "Scolipede"],
    subtypes=["Stage 2"],
    collector_number=40,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Toxic Claws",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
        Attack(
            title="Wild Horn",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_damage(bonus_per_heads=20, coins=2),
        ),
    ],
)
