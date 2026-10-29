from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm10 import (
    wicked_tentacles,
)

card = PokemonCardDef(
    guid="4d0fcae2-799f-5b10-a03d-d0b2c35cf7e0",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Wicked Tentacles",
            game_text="Move an Energy from 1 of your opponent's Pok\u00e9mon to another of their Pok\u00e9mon. If you do, put 3 damage counters on the Pok\u00e9mon you moved the Energy to.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wicked_tentacles
        ),
        Attack(
            title="Wrap",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)