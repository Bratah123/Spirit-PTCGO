from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import healing_pollen


card = PokemonCardDef(
    guid="db11af23-94ef-54c3-a57d-4d2a9732a82f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasVenomoth.Name",
    display_name="Sabrina's Venomoth",
    searchable_by=["Sabrina's Venomoth", "Stage 1", "SabrinasVenomoth"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasVenonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Healing Pollen",
            game_text="Flip 3 coins. For each heads, remove 1 damage counter from each of your Pok\u00e9mon. If a Pok\u00e9mon has fewer damage counters than the number of heads, remove all of them.",
            cost={PokemonTypes.GRASS: 1},
            effect=healing_pollen,
        ),
        Attack(
            title="Sonic Distortion",
            game_text="Flip 2 coins. If 1 or both of them are heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True, coins=2, min_heads=1),
        ),
    ],
)
