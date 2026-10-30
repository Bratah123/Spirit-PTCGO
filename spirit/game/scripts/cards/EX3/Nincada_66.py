from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="abef63d6-3ad9-5420-a0c4-61509ffc9401",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    display_name="Nincada",
    searchable_by=["Nincada", "Basic", "Nincada"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=290,
    abilities=[
        Attack(
            title="Poison Breath",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)