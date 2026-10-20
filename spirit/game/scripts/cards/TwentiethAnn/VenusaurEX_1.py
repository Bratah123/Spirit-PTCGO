from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus, condition_attack


card = PokemonCardDef(
    guid="c5810a9f-0770-547f-9255-fa7f101c6b4e",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    display_name="Venusaur-EX",
    searchable_by=["Venusaur-EX", "Basic", "EX", "VenusaurEX"],
    subtypes=["Basic", "EX"],
    collector_number=1,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Frog Hop",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
        Attack(
            title="Poison Impact",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)