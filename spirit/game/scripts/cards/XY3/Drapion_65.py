from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import bonus_if, defender_has_condition, condition_attack


card = PokemonCardDef(
    guid="9efecc3e-f8d9-59b8-a954-d85e0653f97d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name",
    display_name="Drapion",
    searchable_by=["Drapion", "Stage 1", "Drapion"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    family_id=451,
    abilities=[
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(defender_has_condition(SpecialConditions.POISONED), 40),
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)