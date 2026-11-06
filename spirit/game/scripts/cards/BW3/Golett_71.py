from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="20fda90b-8a8f-57bf-a782-0ef4394f9a82",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic", "Golett"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=622,
    abilities=[
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=20,
            ),
        ),
    ],
)
