from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import energy_conversion


card = PokemonCardDef(
    guid="18af30a1-e8d9-5be4-b3a7-95132e2414ee",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Energy Conversion",
            game_text="Put up to 2 Energy cards from your discard pile into your hand. Gastly does 10 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=energy_conversion,
        ),
    ],
)
