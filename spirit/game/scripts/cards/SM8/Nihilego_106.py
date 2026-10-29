from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    nightcap,
    nightcap_condition,
)

card = PokemonCardDef(
    guid="915286f6-1c33-57fc-a79d-4475a69c0fa9",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nihilego.Name",
    display_name="Nihilego",
    searchable_by=["Nihilego", "Basic", "Ultra Beast", "Nihilego"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=793,
    abilities=[
        Attack(
            title="Nightcap",
            game_text="You can use this attack only if your opponent has exactly 2 Prize cards remaining. Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=nightcap,
            condition=nightcap_condition,
        ),
        Attack(
            title="Void Tentacles",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)