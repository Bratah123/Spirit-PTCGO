from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm9 import (
    adventurous_appetite,
)

card = PokemonCardDef(
    guid="46cb2411-6c65-543e-902d-886182c2807a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMuk.Name",
    display_name="Alolan Muk",
    searchable_by=["Alolan Muk", "Stage 1", "AlolanMuk"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Adventurous Appetite",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may look at the top 6 cards of your opponent's deck and discard any number of Item cards you find there. Your opponent shuffles the other cards back into their deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=adventurous_appetite,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Gunk Shot",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)