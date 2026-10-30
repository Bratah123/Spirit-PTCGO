from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="61a14d5e-19d3-54bd-800c-8557df8ee9d7",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Confusion Wave",
            game_text="Both Psyduck and the Defending Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(
                SpecialConditions.CONFUSED, both_actives=True,
            ),
        ),
    ],
)
