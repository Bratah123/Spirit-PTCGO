from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    bite_off,
    mining,
)

card = PokemonCardDef(
    guid="a4b517a3-2b29-5dc0-ab72-4dbbe747d561",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title="Mining",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. If that card is a Pok\u00e9mon Tool card, instead of putting it into your hand, you may attach it to 1 of your Pok\u00e9mon that doesn't already have a Pok\u00e9mon Tool attached to it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mining,
        ),
        Attack(
            title="Bite Off",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or a Pok\u00e9mon-EX, this attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bite_off,
        ),
    ],
)