from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

from spirit.game.card_effects.sm9 import (
    destiny_stinger,
    destiny_stinger_condition,
)

card = PokemonCardDef(
    guid="3c736293-103f-5ea5-a330-9f920bcc2033",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Destiny Stinger",
            game_text="You can use this attack only if this Pok\u00e9mon has any damage counters on it. Both Active Pok\u00e9mon are Knocked Out.",
            cost={PokemonTypes.GRASS: 1},
            effect=destiny_stinger,
            condition=destiny_stinger_condition,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=recoil_attack(10),
        ),
    ],
)