from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="98ac9c3d-876b-5c73-951d-d7584a51d64e",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=39,
    abilities=[
        Attack(
            title="Lullaby",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
