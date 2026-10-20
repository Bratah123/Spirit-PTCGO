from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import recoil_attack, condition_attack


card = PokemonCardDef(
    guid="8290bf41-0414-50f2-8db8-a363f1388118",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "ThundurusEX"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=642,
    abilities=[
        Attack(
            title="Headlock",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=condition_attack(flip=True, heads_bonus_damage=30,
                                    tails_conditions=(SpecialConditions.PARALYZED,)),
        ),
        Attack(
            title="Voltage Rush",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=recoil_attack(50),
        ),
    ],
)