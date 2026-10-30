from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ec305222-9b84-546f-9f80-b515b16f7bf2",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu",
    searchable_by=["Natu", "Basic", "Natu"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=177,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
