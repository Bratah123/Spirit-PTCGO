from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

from spirit.game.card_effects.sm10 import (
    strong_cheer_passive,
)

card = PokemonCardDef(
    guid="ff86edea-6d3c-59e6-9f37-795e495299b1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name",
    display_name="Incineroar",
    searchable_by=["Incineroar", "Stage 2", "Incineroar"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Strong Cheer",
            game_text="Your Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance). You can't apply more than 1 Strong Cheer Ability at a time.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=strong_cheer_passive
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)