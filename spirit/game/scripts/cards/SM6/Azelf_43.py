from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm6 import psychic_abduction, psychic_abduction_condition

card = PokemonCardDef(
    guid="21801e35-e080-55bb-a28f-26ed45adc7cf",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Attack(
            title="Psychic Abduction",
            game_text="You can use this attack only if you go second, and only on your first turn. Shuffle 1 of your opponent's Benched Pok\u00e9mon and all cards attached to it into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=psychic_abduction_condition,
            effect=psychic_abduction,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
