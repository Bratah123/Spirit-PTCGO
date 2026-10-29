from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dm import (
    charring_breath,
)

card = PokemonCardDef(
    guid="264cac51-6e4c-5770-b9b2-7918d1cb997f",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Charring Breath",
            game_text="If your opponent's Active Pok\u00e9mon isn't Burned, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=charring_breath,
        ),
    ],
)