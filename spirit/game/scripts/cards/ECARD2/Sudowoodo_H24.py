from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.ecard import copy_defending_attack


card = PokemonCardDef(
    guid="d89806e7-782d-5b26-8310-7ff25f186546",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=174,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Copy",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Copy copies that attack. This attack does nothing if Sudowoodo doesn't have the Energy necessary to use that attack. (You must still do anything else required in order to use that attack.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_defending_attack(),
        ),
        Attack(
            title="Energy Draw",
            game_text="Search your deck for a basic Energy card and attach it to Sudowoodo. Shuffle your deck afterward.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, to_self=True),
        ),
    ],
)
