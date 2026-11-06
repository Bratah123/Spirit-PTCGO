from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="62739036-a16f-57c8-accd-c6bebf574d8a",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Baby", "Igglybuff"],
    subtypes=["Baby"],
    collector_number=36,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=174,
    abilities=[
        Attack(
            title="Good Night Song",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
