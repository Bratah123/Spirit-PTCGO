from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack, count_energy, flip_damage,
)


card = PokemonCardDef(
    guid="10560f9f-4cd0-5961-a062-5987414ca8ce",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage and the Defending Pok\u00e9mon is now Paralyzed. If tails, this attack does 10 damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True, heads_bonus_damage=20),
        ),
        Attack(
            title="Spike Barrage",
            game_text="Flip a number of coins equal to the number of Water Energy attached to Omastar. This attack does 20 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 3},
            damage=20,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", energy_type=PokemonTypes.WATER),
                bonus_per_heads=20,
            ),
        ),
    ],
)
