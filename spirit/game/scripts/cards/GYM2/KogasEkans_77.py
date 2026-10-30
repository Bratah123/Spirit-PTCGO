from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="07f19b35-8498-5516-9e78-a69969cb2ee1",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasEkans.Name",
    display_name="Koga's Ekans",
    searchable_by=["Koga's Ekans", "Basic", "KogasEkans"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=23,
    abilities=[
        Attack(
            title="Fast-Acting Poison",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(
                SpecialConditions.CONFUSED, SpecialConditions.POISONED,
                flip=True, coins=2, min_heads=2,
            ),
        ),
    ],
)
