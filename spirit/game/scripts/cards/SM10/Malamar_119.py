from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack

from spirit.game.card_effects.sm10 import (
    hypnotic_reign,
)

card = PokemonCardDef(
    guid="1bc0cca6-d0b6-50b6-991c-0566a8b15203",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Hypnotic Reign",
            game_text="Your opponent reveals their hand. You may discard a Pok\u00e9mon you find there and use one of that Pok\u00e9mon's non-GX attacks as this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=hypnotic_reign
        ),
        Attack(
            title="Dark Pressure",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=mill_attack(1),
        ),
    ],
)