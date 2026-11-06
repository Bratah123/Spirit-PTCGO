from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import has_typed_basic_energy, recover_discarding_energy


card = PokemonCardDef(
    guid="8fda80c1-defd-53b2-a31b-133d866eaa42",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Recover",
            game_text="Discard 1 Water Energy card attached to Tentacool in order to use this attack. Remove all damage counters from Tentacool.",
            cost={PokemonTypes.WATER: 1},
            condition=has_typed_basic_energy(PokemonTypes.WATER),
            effect=recover_discarding_energy(PokemonTypes.WATER),
        ),
    ],
)
