from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="98b3da25-02eb-5f82-8ae1-e5ba3efeebac",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Attack(
            title="Freezing Kiss Goodnight",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Strange Dance",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage and the Defending Pok\u00e9mon is now Confused. If tails, this attack does 20 damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=20),
        ),
    ],
)
