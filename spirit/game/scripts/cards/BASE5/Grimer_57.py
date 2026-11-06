from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="154d38b4-ccdf-59a5-bf05-249347cd7869",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Poison Gas",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Sticky Hands",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage and the Defending Pok\u00e9mon is now Paralyzed; if tails, this attack does 10 damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True, heads_bonus_damage=20),
        ),
    ],
)
