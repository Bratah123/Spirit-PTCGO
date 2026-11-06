from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="cd519857-ff12-5951-bc4b-ef6484514df1",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=175,
    abilities=[
        Attack(
            title="Poison Barb",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
