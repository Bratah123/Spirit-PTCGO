from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="e6f79808-2df8-5b7c-b712-70c5a5f200f7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=207,
    abilities=[
        Attack(
            title="Irongrip",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Stinger",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.PARALYZED,),
            ),
        ),
    ],
)
