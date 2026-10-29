from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    captivating_salsa,
    opponent_benched,
)

card = PokemonCardDef(
    guid="6ee2b98b-b49c-5cc2-8767-67b7b7ab3f07",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title="Captivating Salsa",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=captivating_salsa,
            condition=opponent_benched,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)